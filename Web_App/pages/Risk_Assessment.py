import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import pickle
import os
import warnings
import altair as alt

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import VotingClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

im = Image.open('images/favicon.png')
st.set_page_config(
    page_title="VividHealth",
    page_icon=im, #not actually working for some reason...
    layout="wide",
    initial_sidebar_state="expanded"
)

tab1, tab2 = st.tabs(["Risk Assessment", "Dashboard"])

with tab1: 
    st.header("Risk Assessment Tab")
    current_path = os.getcwd()

    # getting the current path
    model_path = os.path.join(current_path, 'final_risk_model.pkl')

    # loading model
    with open(model_path, 'rb') as handle:
        model = pickle.load(handle)

    #model = pickle.load(open('final_risk_model.pkl', 'rb'))

    #Caching the model for faster loading
    #@st.cache


    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    image_logo = Image.open('images/VividHealth_Logo.png')
    st.image(image_logo, width=407)

    st.header("Assess Your Cervical Cancer Risk")
    st.markdown('<p style="font-family:sans serif; font-size: 20px;"> This page allows you to enter information about yourself in order to see what your overall risk for cervical cancer is currently. '
                'While some of these questions may seem very personal, they are necessary to accuretly determine your risk. If you are wondering why we are asking specific questions'
                'or if you do not understand, just take a look at the information icon below each question!',
                unsafe_allow_html=True)

    st.subheader("Risk Factor Calculator")

    col1, mid, col2 = st.columns([3,0.1,3])
    with col1:
        # Age
        age = st.number_input("Age", help="You must be at least 21 years of age to use this tool.")

        st.write("")
        st.write("")

        # Number of Years Smoked
        # The following should only appear if smoking status is current smoker or former smoker...need to write if statement
        smoke_years = st.number_input("Number of Years Smoking", help="This will be used to calculate your smoking pack years.")
        if smoke_years < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Number of Packs Smoked per day
        ppd = st.number_input("Number of Packs Smoked Per Day", help="This will be used to calculate your smoking pack years.")
        if ppd < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Pack Years calculator
        # Pack years = number of packs of cigarettes smoked per day multiplied by the number of years the person has smoked
        pack_years = ppd * smoke_years
        st.number_input("Pack Years",
                        value=pack_years,  # Defaults to pack years
                        disabled=True,  # User can't change it
                        help="We are calculating this because smoking increases your risk of cervical cancer.")

        st.write("")
        st.write("")

        # IUD Years
        iud_years = st.number_input("Number of Years with IUD", step=1, help="Never used an IUD, write 0. Using an IUD can decrease your risk.")
        if iud_years < 0:
            st.error("Cannot be a negative number!")

    with col2:
        # Age at first sexual intercourse
        first_sex = st.number_input("Age at First Sexual Intercourse", step=1, help="Earlier age for first intercourse can increase your cervical cancer risk.")
        if first_sex < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Contraception years
        contracept_years = st.number_input("Number of Years with Contraception Other Than IUD", step=1, help="Never used contraception, write 0. Using contraception can decrease your risk.")
        if contracept_years < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Number of sexual partners
        num_sex_partners = st.number_input("Number of Lifetime Sexual Partners", step=1, help="Greater number of sexual partners can increase your risk.")
        if num_sex_partners < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Number of pregnancies
        num_preg = st.number_input("Number of Lifetime Pregnancies", step=1, help="Greater number of pregnancies can increase your risk.")
        if num_preg < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Number of STDs
        stds_num = st.number_input("Number of Lifetime STDs", step=1, help="Greater number of STDs can increase your risk.")
        if stds_num < 0:
            st.error("Cannot be a negative number!")


    # Define the prediction function
    warnings.filterwarnings("ignore")
    def predict(age,num_sex_partners,first_sex,num_preg,pack_years,contracept_years,iud_years,stds_num):
        #Predicting the price of the carat
        prediction_prob = model.predict_proba(pd.DataFrame([[age,num_sex_partners,first_sex,num_preg,pack_years,contracept_years,iud_years,stds_num]]))
        risk_array = prediction_prob[:, 1]
        risk = risk_array.astype(float)
        if risk < 0.25:
            print('Low Risk')
        elif (0.25 <= risk < 0.5):
            print('Low Moderate Risk')
        elif (0.5 <= risk < 0.75):
            print('High Moderate Risk')
        else:
            print('High Risk')

    if st.button('Predict Risk'):
        category = predict(age,num_sex_partners,first_sex,num_preg,pack_years,contracept_years,iud_years,stds_num)
        st.success("The predicted risk category for developing cervical cancer is {}".format(category))

#Someone else had the exact same problem but the answer was not helpful
#https://stackoverflow.com/questions/75127342/streamlit-app-showing-the-result-as-none-but-in-the-terminal-appears

with tab2: 
    st.header("Cervical Cancer Risk Dashboard")
    def get_data() -> pd.DataFrame: 
        return pd.read_csv('../cleaned.csv')
    
    shap = pd.DataFrame(data={'Feature': ['IUD','Age','First Sex', 'Contraception Years','Pregnancies','Sexual Partners','Smoking Rate', 'STDs'],'Importance':[.15,.12,.12,.08,.05,.05,.03,.01]})
    shap_bar = alt.Chart(shap).mark_bar().encode(
        x='Importance:Q',y='Feature:O')
    st.altair_chart(shap_bar, use_container_width=False)

    df = get_data()
    age_filter = st.selectbox("Select your age",['<18','18-25','26-35','36-45','46-55','56+'])
    if age_filter == '<18':
        min = 0
        max = 17
    elif age_filter == '18-25':
        min = 18
        max = 25
    elif age_filter == '26-35':
        min = 26
        max = 35
    elif age_filter == '36-45':
        min = 36
        max = 45
    elif age_filter == '46-55':
        min = 46
        max = 55
    else:
        min = 55
        max = 120
    

    placeholder = st.empty()
    df = df[df["age"].between(min,max)]


    kpi1, kpi2, kpi3 = st.columns(3)

    kpi1.metric(
        label = "Hormonal Contraception",
        value = round(df.loc[:,'contracept_years'].astype(np.float16).mean(axis=0),1)
    )
    kpi2.metric(
        label = "Smoking",
        value = round(df.loc[:,'pack_years'].astype(np.float16).mean(axis=0),1)
    )
    kpi3.metric(
        label = "IUD Years",
        value = round(df.loc[:,'iud_years'].astype(np.float16).mean(axis=0),1)
    )


    