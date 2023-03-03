import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import pickle
import os
import warnings
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
import sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import VotingClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

im = Image.open('images/favicon.png')
st.set_page_config(
    page_title="VividHealth",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded"
)

image_logo = Image.open('images/VividHealth_Logo.png')
st.image(image_logo, width=407)

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

tab1, tab2 = st.tabs(["Risk Assessment", "Learn More"])

with tab1:
    current_path = os.getcwd()

    # getting the current path
    model_path = os.path.join(current_path, 'final_risk_model.pkl')


    # loading model
    # with open(model_path, 'rb') as handle:
    #     model = pickle.load(handle)

    @st.cache_resource
    def load_model():
        return pickle.load(open(model_path, 'rb'))


    model = load_model()
    # Caching the model for faster loading
    # @st.cache

    st.header("Assess Your Cervical Cancer Risk")
    st.write(
        '<p class = "dynamicfont">This page allows you to enter information about yourself to see your risk of cervical cancer. '
        'Please fill out the following questions to calculate your risk. '
        'While some of these questions may seem very personal, they are necessary to accurately determine your risk.',
        unsafe_allow_html=True)

    st.subheader("Risk Factor Calculator")

    col1, mid, col2 = st.columns([3, 0.1, 3])
    with col1:
        # Age
        age = st.number_input("What is your age?",
                              help="You must be at least 21 years of age to use this tool because current guidelines state that anyone under the age of 21 does not "
                                   "need routine cervical cancer screening due to very low risk.")

        st.write("")
        st.write("")

        # smoker
        smoker = st.radio("Are you a current or former smoker?", options=('Yes', 'No'),
                          horizontal=True, help="Tobacco by-products are believed to damage the DNA "
                                                "of the cervix cells which can contribute to cervical cancer development. Smoking also "
                                                "decreases the ability of the immune system to fight off a HPV infection.")
        st.write("")
        st.write("")
        st.markdown("")
        if smoker == 'Yes':
            # Number of Years Smoked
            # The following should only appear if smoking status is current smoker or former smoker...need to write if statement
            smoke_years = st.number_input("How many years have you smoked?",
                                          help="This will be used to calculate your smoking pack years.")
            if smoke_years < 0:
                st.error("Cannot be a negative number!")

            st.write("")
            st.write("")

            # Number of Packs Smoked per day
            ppd = st.number_input("How many packs smoked per day?",
                                  help="This will be used to calculate your smoking pack years.")
            if ppd < 0:
                st.error("Cannot be a negative number!")

            st.write("")

            # Pack Years calculator
            # Pack years = number of packs of cigarettes smoked per day multiplied by the number of years the person has smoked
            pack_years = ppd * smoke_years

        else:
            pack_years = 0
            st.markdown("")
            st.markdown("")

        st.write("")

        # IUD Years
        iud_years = st.number_input("How many years have you had an IUD?", step=1,
                                    help="If you've never used an IUD, write 0. The number of years you have had an IUD can impact "
                                         "your cervical cancer risk.")
        if iud_years < 0:
            st.error("Cannot be a negative number!")

    with col2:
        # Age at first sexual intercourse
        first_sex = st.number_input("How old were you when you first had sexual intercourse?", step=1,
                                    help="Earlier age at first intercourse can lead to increased risk of HPV infection, "
                                         "which can increase cervical cancer risk.")
        if first_sex < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Contraception years
        contracept_years = st.number_input("How many years have you used contraception other than IUD?", step=1,
                                           help="If you've never used contraception, write 0. Contraception use, type, and length of use can "
                                                "all affect cervical cancer risk.")
        if contracept_years < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Number of sexual partners
        num_sex_partners = st.number_input("How many sexual partners have you had?", step=1,
                                           help="Greater number of sexual partners can increase your risk due to increased risk "
                                                "of HPV exposure.")
        if num_sex_partners < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Number of pregnancies
        num_preg = st.number_input("How many times have you been pregnant?", step=1,
                                   help="Total number of pregnancies to date, including full term, abortions, and/or miscarriages. Studies have shown that women who have had 3 or more pregnancies are "
                                        "at a higher risk of developing cervical cancer.")
        if num_preg < 0:
            st.error("Cannot be a negative number!")

        st.write("")
        st.write("")

        # Number of STDs
        stds_num = st.number_input("How many STDs have you tested positive for?", step=1,
                                   help="Total number of STDs contracted to date (even if fully treated). Increased number of STDs can decrease the immune response to other infections such as HPV, therefore increasing risk of contracting HPV.")
        if stds_num < 0:
            st.error("Cannot be a negative number!")

    # Define the prediction function
    warnings.filterwarnings("ignore")


    def predict(age, num_sex_partners, first_sex, num_preg, pack_years, contracept_years, iud_years, stds_num):
        # Predicting the price of the carat
        prediction_prob = model.predict_proba(pd.DataFrame(
            [[age, num_sex_partners, first_sex, num_preg, pack_years, contracept_years, iud_years, stds_num]]))
        risk_array = prediction_prob[:, 1]
        risk = risk_array.astype(float)
        if risk < 0.25:
            return 'LOW', '0,255,0', 'This risk category means that compared to other individuals at your age with similar ' \
                                     'characteristics, you are at a low risk for developing cervical cancer. Based on this information, ' \
                                     'you can continue to get screened at regular intervals outlined per USPSTF guidelines.', \
                'This is just a guideline, the VividHealth team encourages all individuals to discuss their risk ' \
                'with their healthcare provider.'
        elif (0.25 <= risk < 0.5):
            return 'LOW MODERATE', '255,255,51', 'This risk category means that compared to other individuals at your age with similar ' \
                                                 'characteristics, you are at a low-moderate risk for developing cervical cancer. Based on this information, ' \
                                                 'you may need to discuss how frequently you should get screened. ', \
                'This is just a guideline, the VividHealth team encourages all individuals to discuss their risk ' \
                'with their healthcare provider.'

        elif (0.5 <= risk < 0.75):
            return 'HIGH MODERATE', '255,128,0', 'This risk category means that compared to other individuals at your age with similar ' \
                                                 'characteristics, you are at a High-Moderate risk for developing cervical cancer. Based on this information, ' \
                                                 'you may need additional screenings or procedures performed. ', \
                'This is just a guideline, the VividHealth team encourages all individuals to discuss their risk ' \
                'with their healthcare provider.'
        else:
            return 'HIGH', '255,0,0', 'This risk category means that compared to other individuals at your age with similar ' \
                                      'characteristics, you are at a High risk for developing cervical cancer. Based on this information, ' \
                                      'you will most likely need additional screenings or procedures performed. ', \
                'This is just a guideline, the VividHealth team encourages all individuals to discuss their risk ' \
                'with their healthcare provider.'


    if st.button('Predict Risk'):
        category, color, guideline, comment = predict(age, num_sex_partners, first_sex, num_preg, pack_years,
                                                      contracept_years, iud_years, stds_num)
        st.markdown(f'''
        <style>
        .riskcat{{
            background: rgba({color},0.2);
            text-align: center;
            font-size:20px;
            padding: 25px;
            color: black;
        }}
        </style><div class=riskcat>Risk Category: <strong>{category}</strong> 
        {guideline}

        <strong>{comment}</strong></div>
        ''', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1.5, 5, 1])
        with col1:
            st.write("")
        with col2:
            st.image("images/recommendations2.png")
        with col3:
            st.write("")
        citation1 = '<p style="font-size: 10px; font-size:calc(10px + 0.3vw);text-align: center;"> https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/cervical-cancer-screening'
        st.markdown(citation1, unsafe_allow_html=True)

with tab2:
    st.header("Learn More About Cervical Cancer Risk")
    st.write("Our risk category predictions are created by feeding your information into an algorithm.")

    def get_data() -> pd.DataFrame:
        return pd.read_csv('../cleaned.csv')

    st.subheader("Cervical Cancer Risk by Age")
    st.write(
        "See how you compare to others in a similar or different age categories than you. For the age category you select, you will see others in that "
        "category exhibiting the following traits:")
    df = get_data()
    age_filter = st.selectbox("Select your age:", ['<18', '18-25', '26-35', '36-45', '46-55', '56+'])
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
    df = df[df["age"].between(min, max)]

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric(
        label="Hormonal Contraception (years)",
        value=round(float(df.loc[:, 'contracept_years'].astype(np.float16).mean(axis=0)), 1)
    )
    kpi2.metric(
        label="Smoking (packs/year)",
        value=round(float(df.loc[:, 'pack_years'].astype(np.float16).mean(axis=0)), 1)
    )
    kpi3.metric(
        label="IUD Years",
        value=round(float(df.loc[:, 'iud_years'].astype(np.float16).mean(axis=0)), 1)
    )
    kpi4.metric(
        label="Pregnancies",
        value=round(float(df.loc[:, 'num_preg'].astype(np.float16).mean(axis=0)), 1)
    )

    pie1, pie2 = st.columns(2)

    with pie1:
        fig2, ax2 = plt.subplots()
        no_smoke = len(df[df['smoker'] == False])
        smoke = len(df[df['smoker'] == True])
        ax2.pie([no_smoke, smoke], labels=['Non-Smokers', 'Smokers'], colors=['green', 'orange'])
        ax2.axis('equal')
        st.pyplot(fig2)

    with pie2:
        fig3, ax3 = plt.subplots()
        no_contraception = len(df[df['iud'] == False])
        contraception = len(df[df['iud'] == True])
        ax3.pie([no_contraception, contraception], labels=['IUD', 'No IUD'], colors=['green', 'orange'])
        ax3.axis('equal')
        st.pyplot(fig3)

    fig4, ax4 = plt.subplots()

    chart1, chart2 = st.columns(2)
    colors = {1: 'red', 0: 'blue'}

    with chart1:
        fig, ax = plt.subplots()

        ax.set_title("Age of First Sex vs. Current Age; Size is # of Sexual Partners")
        ax.set_xlabel("Age")
        ax.set_ylabel("Age of First Sex")
        scatter = ax.scatter(df['age'], df['first_sex'], s=df['num_sex_partners'], c=df['cancer'].map(colors))
        plt.legend((0, 1), ("No Cancer", "Cancer"))
        st.pyplot(fig)

    with chart2:
        fig1, ax1 = plt.subplots()
        ax1.set_title("Age vs. IUD Years")
        ax1.set_xlabel("Age")
        ax1.set_ylabel("IUD Years")
        scatter1 = ax1.scatter(df['age'], df['iud_years'], c=df['cancer'].map(colors))
        ax1.legend(*scatter1.legend_elements())
        st.pyplot(fig1)

    st.subheader("Cervical Cancer Statistics Across the United States")
    st.write("Overall number of cervical cancer cases and deaths from 1999 to 2019:")

    def get_cases_data() -> pd.DataFrame:
        return pd.read_csv('data/casestrends.csv')
    df_cases = get_cases_data()
    def get_deaths_data() -> pd.DataFrame:
        return pd.read_csv('data/deathtrends.csv')
    df_deaths = get_deaths_data()

    rate_number_filter = st.selectbox("Assess cervical cancer by rate or number of cases:", ['rate', 'number of cases'])

    if rate_number_filter == 'rate':
        col1, col2 = st.columns([4, 4])
        with col1:
            fig = px.line(df_cases, x="Year", y="per_100k", title="Annual Rate of New Cervical Cancer Cases", markers=True)
            fig.update_traces(line_color="#16c6e0")
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=True, gridcolor='LightGrey', title_text="Rate per 100,000 Women", range=[0, 11])
            fig.update_layout(plot_bgcolor="white", title_x=0.5)
            st.plotly_chart(fig, theme=None, use_container_width=True)
        with col2:
            fig = px.line(df_deaths, x="Year", y="per_100k", title="Annual Rate of New Cervical Cancer Deaths", markers=True)
            fig.update_traces(line_color="#22cbc7")
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=True, gridcolor='LightGrey', title_text="Rate per 100,000 Women", range=[0, 11])
            fig.update_layout(plot_bgcolor="white", title_x=0.5)
            st.plotly_chart(fig, theme=None, use_container_width=True)
    else:
        col3, col4 = st.columns([4,4])
        with col3:
            fig3 = px.bar(df_cases, x="Year", y="Case_Count", title="Annual Number of New Cervical Cancer Cases per Year")
            fig3.update_traces(marker_color="#16c6e0")
            fig3.update_xaxes(showgrid=False)
            fig3.update_yaxes(showgrid=True, gridcolor='LightGrey', title_text="Case Count", range=[0, 14000])
            fig3.update_layout(plot_bgcolor="white", title_x=0.5)
            st.plotly_chart(fig3, theme=None, use_container_width=True)
        with col4:
            fig4 = px.bar(df_deaths, x="Year", y="Death_Count", title="Annual Number of Cervical Cancer Deaths per Year")
            fig4.update_traces(marker_color="#22cbc7")
            fig4.update_xaxes(showgrid=False)
            fig4.update_yaxes(showgrid=True, gridcolor='LightGrey', title_text="Death Count", range=[0, 4500])
            fig4.update_layout(plot_bgcolor="white", title_x=0.5)
            st.plotly_chart(fig4, theme=None, use_container_width=True)

