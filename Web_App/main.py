import streamlit as st
from PIL import Image
# from collections import namedtuple
# import altair as alt
# import pandas as pd

im = Image.open('favicon.png')
st.set_page_config(
    page_title="VividHealth",
    page_icon=im, #not actually working for some reason...
    layout="wide"
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

image_logo = Image.open('VividHealth_Logo.png')
st.image(image_logo, width=407)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "About Us", "Risk Assessment", "Find A Provider", "Sign In"])

with tab1:
    image_banner = Image.open('banner.png')
    st.image(image_banner, use_column_width=True)
    st.markdown('<p style="font-family:sans serif; font-size: 22px;"> According to the World Health Organization, cervical cancer is the fourth most common cancer among women globally with about 600,000 new cases documented in 2020. '
                'Of these new cases, there were an estimated 342,000 deaths in 2020 alone. '
                'Yet, the CDC estimates that even today 93% of cervical cancer cases are preventable, when healthcare guidelines are followed <sup>1</sup>. '
                'To address this discrepancy between cervical cancer incidence and effectiveness of preventative measures, VividHealth has created this multifunction and easy to use website.',
                unsafe_allow_html=True)
    st.write("")

    image_rib = Image.open('ribbon.png')
    col1, mid, col2 = st.columns([1, 2, 20])
    with col1:
        st.image(image_rib, width=150)
    with col2:
        st.write("")
        st.write("")
        risk_assessment = '<p style="font-family:sans serif; font-size: 28px;"> <strong>Personal Risk Assessment'
        st.markdown(risk_assessment, unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans serif; font-size: 20px;"> Check your own cervical cancer risk on the Risk Assessment tab. Our easy to use platform will ask a series of questions that can be significant predictors for assessing if you '
                    'are at risk of developing cervical cancer.', unsafe_allow_html=True)
    st.write("")

    image_map = Image.open('map.png')
    col1, mid, col2 = st.columns([20, 0.5, 4])
    with col1:
        st.write("")
        st.write("")
        provider = '<p style="font-family:sans serif; font-size: 28px;"> <strong>Find A Healthcare Provider Near You'
        st.markdown(provider, unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans serif; font-size: 20px;"> Use our Find A Provider tab to locate a healthcare professional near you who is qualified to work with you through your cervical cancer screenings and treatment. ',
                 unsafe_allow_html=True)
    with col2:
        st.image(image_map, use_column_width=True)
    st.write("")

    image_health = Image.open('healthcare.png')
    col1, mid, col2 = st.columns([1, 2, 20])
    with col1:
        st.image(image_health, width=150)
    with col2:
        st.write("")
        st.write("")
        portal = '<p style="font-family:sans serif; font-size: 28px;"> <strong>Patient and Provider Portal'
        st.markdown(portal, unsafe_allow_html=True)
        st.markdown('<p style="font-family:sans serif; font-size: 20px;"> Use our Sign In tab to access the patient and healthcare provider portal. This portal is where you will be able to communicate with your provider about recent test, questions, '
                 'or any concerns.', unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    citation1 = '<p style="font-family:sans serif; font-size: 14px;"> <sup>1</sup>https://www.cdc.gov/vitalsigns/cervical-cancer/index.html'
    st.markdown(citation1, unsafe_allow_html=True)

with tab2:
    st.header("VividHealth Team")
    st.markdown('<p style="font-family:sans serif; font-size: 20px;"> VividHealth is a leading medical technology consulting firm that focuses on improving patient outcomes by incorporating new technologies into existing healthcare systems to aid with diagnosis, prevention, and outreach. '
                'We have partnered with Epic, an EMR company, to add new diagnostic capabilities into Epic’s Comprehensive Health Record software. '
                'We are passionate about delivering diagnostic information to assist clinical judgment and building interactive tools to enable patients to take control of their health. '
                'We created VividHealth out of our desire to make healthcare more accessible and cost effective. '
                'Having a positive impact in our community and helping others obtain necessary care motivates us to continue our current work. ',
                unsafe_allow_html=True)
    st.write("")
    st.write("")
    image_M = Image.open('Mona.jpg')
    col1, mid, col2 = st.columns([3, 1, 15])
    with col1:
        st.image(image_M, use_column_width=True)
    with col2:
        st.markdown('<p style="font-family:sans serif; font-size: 20px;"> <u><strong>Mona Ascha</strong></u> is a doctor and working surgeon with six years of postgraduate clinical training in surgery. '
                    'She is an accomplished academic researcher with over 40 PubMed indexed peer reviewed articles. '
                    'She brings her medical expertise and prior experience with machine learning applications using healthcare data to cervical cancer image detection. '
                    'She seeks projects that intersect her passions for medicine and analytics.',
                    unsafe_allow_html=True)
    st.write("___________________")
    image_J = Image.open('Julia.jpg')
    col1, mid, col2 = st.columns([3, 1, 15])
    with col1:
        st.image(image_J, use_column_width=True)
    with col2:
        st.markdown('<p style="font-family:sans serif; font-size: 20px;"> <u><strong>Julia Ma</strong></u> is a software engineer with two years of professional experience in the government sector. '
                    'She has a diverse skill set including hardware simulation, signal processing, data engineering, data visualization, and NLP. '
                    'Her work with the government has given her an interest in data privacy and explainable AI.',
                    unsafe_allow_html=True)
    st.write("___________________")
    image_E = Image.open('Erin.JPG')
    col1, mid, col2 = st.columns([3, 1, 15])
    with col1:
        st.image(image_E, use_column_width=True)
    with col2:
        st.markdown('<p style="font-family:sans serif; font-size: 20px;"> <u><strong>Erin McMahon</strong></u> brings seven years of healthcare experience working in various hospital settings and in the community as a 911 EMT. '
                    'She is able to combine her knowledge of healthcare to her more recent work as a Project Manager and Data Scientist to address cervical cancer risk assessment. '
                    'As someone who has been able to beat cervical cancer due to successful preventative measures, screenings, and early treatment, she is passionate about assisting others to have a similar or better experience.',
                     unsafe_allow_html=True)
    st.write("___________________")
    image_S = Image.open('Sarah.jpeg')
    col1, mid, col2 = st.columns([3, 1, 15])
    with col1:
        st.image(image_S, use_column_width=True)
    with col2:
        st.markdown('<p style="font-family:sans serif; font-size: 20px;"> <u><strong>Sarah Rodenbeck</strong></u> is an AI professional specializing in natural language processing, AI-aided engineering, and responsible AI with experience in both industry and academia. '
                    'Leveraging her technical background in computer science with years of professional experience in data science, she supports the full lifecycle of analytics projects from algorithmic design all the way through deployment. '
                    'Sarah also brings expertise in AI ethics, governance, and privacy, and is passionate about human- and privacy-first designs that support positive changes in communities.',
                    unsafe_allow_html=True)
    st.write("___________________")
    image_R = Image.open('Rachel.jpg')
    col1, mid, col2 = st.columns([3, 1, 15])
    with col1:
        st.image(image_R, use_column_width=True)
    with col2:
        st.markdown('<p style="font-family:sans serif; font-size: 20px;"> <u><strong>Rachel Sickler</strong></u> is an ML engineer specializing in systems design and administration. '
                    'She has four years of experience as a technical business analyst eliciting, confirming and documenting requirements, seven years of experience architecting and administering data pipelines and databases and has been building software for four years. '
                    'Rachel brings experience working in health insurance, collaborating with state and federal agencies to ensure affordable coverage for patients in Vermont. '
                    'Her work in public safety is what drives her passion for data privacy and using AI to improve society.',
                    unsafe_allow_html=True)

with tab3:
    st.header("Assess Your Cervical Cancer Risk")
    st.markdown('<p style="font-family:sans serif; font-size: 20px;"> This page allows you to enter information about yourself in order to see what your overall risk for cervical cancer is currently. '
                'While some of these questions may seem very personal, they are necessary to accuretly determine your risk. If you are wondering why we are asking specific questions'
                'or if you do not understand, just take a look at the information icon below each question!',
                unsafe_allow_html=True)
    # Risk factor tool
    st.subheader("Risk Factor Calculator")

    #Age
    age_min = st.number_input("Age")
    # if age_min < 21:
    #     st.error("You are too young to use this tool!")
    # else:
    #     st.success("You are old enough to use this tool!")
    # not sure if this is needed since we have the info button now
    st.info("\n We are asking this because you must be at least 21 years of age to use this tool.", icon="ℹ️")

    #Smoking status
    #selected_class = st.radio("Smoking Status", ['Current smoker', 'Former Smoker', 'Never Smoker'])
    #st.write("Smoking Status:", selected_class)
    # st.write("Smoking Status Type:", type(selected_class))

    #Number of Years Smoked
    #The following should only appear if smoking status is current smoker or former smoker...need to write if statement
    smoke_years = st.number_input("Number of Years Smoking")
    if smoke_years < 0:
        st.error("Cannot be a negative number!")
    st.info("\n This will be used to calculate your smoking pack years.", icon="ℹ️")

    #Number of Packs Smoked per day
    ppd = st.number_input("Number of Packs Smoked Per Day")
    if ppd < 0:
        st.error("Cannot be a negative number!")
    st.info("\n This will be used to calculate your smoking pack years.", icon="ℹ️")

    #Pack Years calculator
    #Pack years = number of packs of cigarettes smoked per day multiplied by the number of years the person has smoked
    pack_years = ppd*smoke_years
    st.number_input("Pack Years",
                    value=pack_years, #Defaults to pack years
                    disabled=True) #User can't change it
    st.info("\n We are calculating this because smoking increases your risk of cervical cancer.", icon="ℹ️")

    #IUD Years
    iud_years = st.number_input("Number of Years with IUD", step=1)
    if iud_years < 0:
        st.error("Cannot be a negative number!")
    st.info("If you never had an IUD, write 0. Having an IUD can decrease your cervical cancer risk.", icon="ℹ️")

    #Age at first sexual intercourse
    age_first_sex = st.number_input("Age at First Sexual Intercourse", step=1)
    if age_first_sex < 0:
        st.error("Cannot be a negative number!")
    st.info("We are asking this because earlier age at first intercourse can increase your cervical cancer risk.", icon="ℹ️")

    #Contraception years
    contracept_years = st.number_input("Number of Years with Contraception", step=1)
    if contracept_years < 0:
        st.error("Cannot be a negative number!")
    st.info("If you never had contraception, write 0. Having contraception can decrease your cervical cancer risk.", icon="ℹ️")

    #Number of sexual partners
    num_sex_partners = st.number_input("Number of Lifetime Sexual Partners", step=1)
    if num_sex_partners < 0:
        st.error("Cannot be a negative number!")
    st.info("We are asking this because greater number of sexual partners can increase your cervical cancer risk.", icon="ℹ️")

    #Number of pregnancies
    num_pregnancies = st.number_input("Number of Lifetime Pregnancies", step=1)
    if num_pregnancies < 0:
        st.error("Cannot be a negative number!")
    st.info("We are asking this because greater number of pregnancies can increase your cervical cancer risk.", icon="ℹ️")

    #Number of STDs
    num_stds = st.number_input("Number of Lifetime STDs", step=1)
    if num_stds < 0:
        st.error("Cannot be a negative number!")
    st.info("We are asking this because greater number of STDs can increase your cervical cancer risk.", icon="ℹ️")

with tab4:
    st.header("Healthcare Near You")
    # Map
    st.markdown("This page allows you to find healthcare providers in your area who are qualified to perform cervical cancer screenings. ")
    # Requires a mapbox API access token? I signed up and got one...
    # Token: pk.eyJ1IjoibW9uYWFzY2hhIiwiYSI6ImNsZGFmaWkyeTBpbjMzcHBoanFrd3h2OG0ifQ.d1wdtlrj84uF--9OkL-o6w
    st.map()

with tab5:
    st.header("Patient and Provider Portal")

    def check_password():
        """Returns `True` if the user had a correct password."""

        def password_entered():
            """Checks whether a password entered by the user is correct."""
            if (
                    st.session_state["username"] in st.secrets["passwords"]
                    and st.session_state["password"]
                    == st.secrets["passwords"][st.session_state["username"]]
            ):
                st.session_state["password_correct"] = True
                del st.session_state["password"]  # don't store username + password
                del st.session_state["username"]
            else:
                st.session_state["password_correct"] = False

        if "password_correct" not in st.session_state:
            # First run, show inputs for username + password.
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            return False
        elif not st.session_state["password_correct"]:
            # Password not correct, show input + error.
            st.text_input("Username", on_change=password_entered, key="username")
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            st.error("😕 User not known or password incorrect")
            return False
        else:
            # Password correct.
            return True


    if check_password():
        st.subheader("The results of your cervical cancer risk assessment and pap smear are provided below:")
        st.write("waiting for categorization results from Mona and Julia to fill this one out :)")
        st.write("Upload image below")
        uploaded_file = st.file_uploader("Choose a file",
                                         type=None,
                                         accept_multiple_files=False,  # only accept one file at a time
                                         key=None,
                                         help=None,
                                         on_change=None,
                                         disabled=False,
                                         label_visibility="visible")
        if uploaded_file is not None:
            bytes_data = uploaded_file.getvalue()
            # To read file as bytes:
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)
            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)