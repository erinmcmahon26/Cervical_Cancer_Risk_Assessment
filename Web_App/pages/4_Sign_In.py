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
st.markdown('''<style>
        * {font-family: Optima;}
        .dynamicfont{
            font-size:14px;
            font-size:calc(14px + 0.3vw);
        }
        </style>''', unsafe_allow_html=True)

image_logo = Image.open('images/VividHealth_Logo.png')
st.image(image_logo, width=407)

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

name, authentication_status, username = authenticator.login('Patient and Provider Portal', 'main')

if st.session_state["authentication_status"]:
    tab1, tab2 = st.tabs(["Results", "Messages"])
    authenticator.logout('Logout', 'main')
    with tab1:
        st.header(f'Welcome *{st.session_state["name"]}*')
        st.subheader("The results of your cervical cancer risk assessment and pap smear are provided below:")
        st.markdown(f'''
                <style>
                .riskcat{{
                    background: rgba(0,255,0,0.2);
                    text-align: center;
                    font-size:14px;
                    font-size:calc(14px + 0.3vw);
                    padding: 25px;
                    color: black;
                }}
                </style><div class="riskcat"> You are at a LOW risk of developing cervical cancer. The main demographic of concern is that you have just recently started smoking. While you are currently at a low risk, continuing to smoke could increase your risk in the future. Based on the USPSTF guidelines and your last appointment, I suggest we continue with routine examinations every 3 years. </div>
                ''', unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.subheader("Your Demographics")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.markdown('<p class = "dynamicfont"><strong>Age:</strong> 24', unsafe_allow_html=True)
            st.markdown('<p class = "dynamicfont"><strong>Current or Former Smoker:</strong> Yes', unsafe_allow_html=True)
        with col2:
            st.markdown('<p class = "dynamicfont"> <strong>Years Smoking:</strong> Less than 1', unsafe_allow_html=True)
            st.markdown('<p class = "dynamicfont"><strong>Packs Smoked per Day:</strong> 0.5', unsafe_allow_html=True)
        with col3:
            st.markdown('<p class = "dynamicfont"><strong>Years with IUD:</strong> 3', unsafe_allow_html=True)
            st.markdown('<p class = "dynamicfont"><strong>Age of First Sexual Intercourse:</strong> 4', unsafe_allow_html=True)
        with col4:
            st.markdown('<p class = "dynamicfont"><strong>Other Forms of Contraception:</strong> No', unsafe_allow_html=True)
            st.markdown('<p class = "dynamicfont"><strong>Number of Sexual Partners:</strong> 3', unsafe_allow_html=True)
        with col5:
            st.markdown('<p class = "dynamicfont"><strong>Number of Pregnancies:</strong> 1', unsafe_allow_html=True)
            st.markdown('<p class = "dynamicfont"><strong>Number of STDs:</strong> 1', unsafe_allow_html=True)


        # Parameters: an array of images - should really be isolated to a single
        # type of cell for consistency with training data
        # Returns: array of scaled features
        st. write("")
        st.subheader("Pap Smear Image Upload:")
        uploaded_file = st.file_uploader("",
                                         type=None,
                                         accept_multiple_files=True,
                                         key=None,
                                         help=None,
                                         on_change=None,
                                         disabled=False,
                                         label_visibility="visible")

        if uploaded_file:
            def preprocess_images_for_model(input_imgs):
                #print("preprocessing images for the model")
                # print("image outputs", input_imgs)
                data = []

                height = 64
                width = 64
                channels = 3
                classes = 43
                n_inputs = height * width * channels

                #print("formatting images")
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
                #print("converting images to array")
                data = np.array(data)

                #print("shape", data.shape)

                # Loading ResNet50 with imagenet weights, include_top means that we're loading model without last fully connected layers
                #print("starting resnet feature extraction")
                model_resnet = ResNet50(weights='imagenet', include_top=False)

                #print("resnet feature predict")
                # print(data)
                features_resnet = model_resnet.predict(data, batch_size=32)
                #print("features_resnet_shape:", features_resnet.shape)

                #print("assembling resnet features")
                extracted_features = []

                for f_r in features_resnet:
                    f_r = f_r.reshape(f_r.shape[0] * f_r.shape[1] * f_r.shape[2])
                    f_r = np.append(f_r, 0)
                    extracted_features.append(f_r)

                extracted_features = np.array(extracted_features)
                #print("extracted features shape:", extracted_features.shape)

                # Normalization
                #print("normalizing features")
                X = extracted_features[:, 0:-1]

                #print("loading pipeline")
                pipeline = joblib.load('pipeline.pkl')
                #print("transforming with pipeline")
                principal_X = pipeline.transform(X)

                return principal_X


            # Parameter: Array of unprocessed images with cells isolate
            # Returns: Array of predictions for inputted images

            def predict_imgs(input_images):
                #print("starting predict_imgs function)")
                # make sure the model loads before you go to the trouble of pre-processing
                #print("loading model")
                model = joblib.load('img_model.pkl')
                #print("model:", model)

                # send the images away for preprocessing
                #print("preprocessing images")
                X = preprocess_images_for_model(input_images)

                # inferences
                #print("making predictions")
                #print("X:", X)
                predictions = np.argmax(model.predict(X), axis=1)

                return predictions


            images = []
            for file in uploaded_file:
                bytes_data = file.read()
                path = os.getcwd()
                with open(os.path.join(path + "/pages/tempDir/", file.name), "wb") as f:
                    f.write(bytes_data)
                    # print("bytes data", bytes_data)
                image_file = path + "/pages/tempDir/" + file.name
                images.append(image_file)
                # print("image file", image_file)
                container = st.container()
                # cell_image = st.image(image_file, width=250)
                container.image(image_file, width=300)

            predictions = predict_imgs(images)
            for pred in predictions:
                if pred == 0:
                    container.write('Abnormal Pap Smear')
                elif pred == 1:
                    st.write('Abnormal Pap Smear')
                elif pred == 2:
                    st.write('Not Normal Pap Smear')
                elif pred == 3:
                    st.write('Not Normal Pap Smear')
                else:
                    st.write('Normal Pap Smear')
    with tab2:
        st.subheader("Message Board")
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
