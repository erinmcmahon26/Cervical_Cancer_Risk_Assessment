import streamlit as st
import yaml
from yaml import SafeLoader
from PIL import Image
import streamlit_authenticator as stauth
import joblib
import numpy as np
import cv2
import os
from tensorflow import keras
from keras.applications.resnet import ResNet50
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

im = Image.open('images/favicon.png')
st.set_page_config(
    page_title="VividHealth",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(""" <style>*{font-family: "Optima", Optima;}</style>""", unsafe_allow_html=True)

image_logo = Image.open('images/VividHealth_Logo.png')
st.image(image_logo, width=407)
st.write("______________________")

st.header("Patient and Provider Portal")

config_file = 'config.yaml'
with open(config_file) as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

name, authentication_status, username = authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    st.subheader("The results of your cervical cancer risk assessment and pap smear are provided below:")
    st.write("waiting for categorization results from Mona and Julia to fill this one out :)")
    st.write("Upload image below")

    # Parameters: an array of images - should really be isolated to a single
    # type of cell for consistency with training data
    # Returns: array of scaled features

    uploaded_file = st.file_uploader("Choose a file",
                                     type=None,
                                     accept_multiple_files=True,
                                     key=None,
                                     help=None,
                                     on_change=None,
                                     disabled=False,
                                     label_visibility="visible")

    if uploaded_file:
        def preprocess_images_for_model(input_imgs):
            print("preprocessing images for the model")
            # print(input_imgs)
            data = []

            height = 64
            width = 64
            channels = 3
            classes = 43
            n_inputs = height * width * channels

            print("formatting images")
            for input_img in input_imgs:
                try:
                    # print(input_img)
                    image = cv2.imread(input_img)
                    image_from_array = Image.fromarray(image, 'RGB')
                    size_image = image_from_array.resize((height, width))
                    data.append(np.array(size_image))
                except AttributeError:
                    print("Something is wrong with the image(s)")

            # Converting data to ndarray
            print("converting images to array")
            data = np.array(data)

            print("shape", data.shape)

            # Loading ResNet50 with imagenet weights, include_top means that we're loading model without last fully connected layers
            print("starting resnet feature extraction")
            model_resnet = ResNet50(weights='imagenet', include_top=False)

            print("resnet feature predict")
            # print(data)
            features_resnet = model_resnet.predict(data, batch_size=32)
            print("features_resnet_shape:", features_resnet.shape)

            print("assembling resnet features")
            extracted_features = []

            for f_r in features_resnet:
                f_r = f_r.reshape(f_r.shape[0] * f_r.shape[1] * f_r.shape[2])
                f_r = np.append(f_r, 0)
                extracted_features.append(f_r)

            extracted_features = np.array(extracted_features)
            print("extracted features shape:", extracted_features.shape)

            # Normalization
            print("normalizing features")
            X = extracted_features[:, 0:-1]

            print("loading pipeline")
            pipeline = joblib.load('pipeline.pkl')
            print("transforming with pipeline")
            principal_X = pipeline.transform(X)

            return principal_X


        # Parameter: Array of unprocessed images with cells isolate
        # Returns: Array of predictions for inputted images

        def predict_imgs(input_images):
            print("starting predict_imgs function)")
            # make sure the model loads before you go to the trouble of pre-processing
            print("loading model")
            model = joblib.load('img_model.pkl')
            print("model:", model)

            # send the images away for preprocessing
            print("preprocessing images")
            X = preprocess_images_for_model(input_images)

            # inferences
            print("making predictions")
            print("X:", X)
            predictions = np.argmax(model.predict(X), axis=1)

            return predictions


        images = []
        for file in uploaded_file:
            bytes_data = file.read()
            path = os.getcwd()
            with open(os.path.join(path + "/pages/tempDir/", file.name), "wb") as f:
                f.write(bytes_data)
                # print("HERE", bytes_data)
            image_file = path + "/pages/tempDir/" + file.name
            images.append(image_file)
            # print(image_file)
            container = st.container()
            # cell_image = st.image(image_file, width=250)
            container.image(image_file, width=300)

        predictions = predict_imgs(images)
        for pred in predictions:
            if pred == 0:
                container.write('Dyskeratotic')
            elif pred == 1:
                st.write('Koilocytotic')
            elif pred == 2:
                st.write('Metaplastic')
            elif pred == 3:
                st.write('Parabasal')
            else:
                st.write('Superficial-Intermediate')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
