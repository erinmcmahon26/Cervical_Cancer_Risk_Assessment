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


image = Image.open('VividHealth_Logo.png')
st.image(image, width = 600)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "About Us", "Risk Assessment", "Find A Provider", "Sign In"])

with tab1:
    image = Image.open('banner.png')
    st.image(image)
    st.markdown("According to the World Health Organization, cervical cancer is the fourth most common cancer among women globally with about 600,000 new cases documented in 2020. "
                "Of these new cases, there were an estimated 342,000 deaths in 2020 alone (WHO, 2022). "
                "Yet, cervical cancer is one of the most preventable cancers, when healthcare guidelines are followed. ")
with tab2:
    st.header("About Us")
    st.markdown("VividHealth is a leading medical technology consulting firm that focuses on improving patient outcomes by incorporating new technologies into existing healthcare systems to aid with diagnosis, prevention, and outreach. "
                "We have partnered with Epic, an EMR company, to add new diagnostic capabilities into Epic’s Comprehensive Health Record software. "
                "We are passionate about delivering diagnostic information to assist clinical judgment and building interactive tools to enable patients to take control of their health. "
                "We created VividHealth out of our desire to make healthcare more accessible and cost effective. "
                "Having a positive impact in our community and helping others obtain necessary care motivates us to continue our current work. ")

    image_M = Image.open('Mona.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_M, width=90)
    with col2:
        st.write("Mona Ascha is a doctor and working surgeon with six years of postgraduate clinical training in surgery. "
                 "She is an accomplished academic researcher with over 40 PubMed indexed peer reviewed articles. "
                 "She brings her medical expertise and prior experience with machine learning applications using healthcare data to cervical cancer image detection. "
                 "She seeks projects that intersect her passions for medicine and analytics.")
    image_J = Image.open('Julia.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_J, width=90)
    with col2:
        st.write("Julia Ma is a software engineer with two years of professional experience in the government sector. "
                 "She has a diverse skill set including hardware simulation, signal processing, data engineering, data visualization, and NLP. "
                 "Her work with the government has given her an interest in data privacy and explainable AI.")
    image_E = Image.open('Erin.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_E, width=90)
    with col2:
        st.write("Erin McMahon brings seven years of healthcare experience working in various hospital settings and in the community as a 911 EMT. "
                 "She is able to combine her knowledge of healthcare to her more recent work as a Project Manager and Data Scientist to address cervical cancer risk assessment. "
                 "As someone who has been able to beat cervical cancer due to successful preventative measures, screenings, and early treatment, she is passionate about assisting others to have a similar or better experience.")

    image_S = Image.open('Sarah.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_S, width=90)
    with col2:
        st.write(
            "Sarah Rodenbeck is an AI professional specializing in natural language processing, AI-aided engineering, and responsible AI with experience in both industry and academia. "
            "Leveraging her technical background in computer science with years of professional experience in data science, she supports the full lifecycle of analytics projects from algorithmic design all the way through deployment. "
            "Sarah also brings expertise in AI ethics, governance, and privacy, and is passionate about human- and privacy-first designs that support positive changes in communities.")

    image_R = Image.open('Rachel.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_R, width=90)
    with col2:
        st.write(
            "Rachel Sickler is an ML engineer specializing in systems design and administration. "
            "She has four years of experience as a technical business analyst eliciting, confirming and documenting requirements, seven years of experience architecting and administering data pipelines and databases and has been building software for four years. "
            "Rachel brings experience working in health insurance, collaborating with state and federal agencies to ensure affordable coverage for patients in Vermont. "
            "Her work in public safety is what drives her passion for data privacy and using AI to improve society.")

with tab3:
    st.header("Assess Your Cervical Cancer Risk")
    st.markdown("Explain what this tool is here!")
    # Risk factor tool
    st.subheader("Risk Factor Calculator")

    #Age
    age_min = st.number_input("Age")
    if age_min < 21:
        st.error("You are too young to use this tool!")
    else:
        st.success("You are old enough to use this tool!")

    #Smoking status
    selected_class = st.radio("Smoking Status", ['Current smoker', 'Former Smoker', 'Never Smoker'])
    st.write("Smoking Status:", selected_class)
    # st.write("Smoking Status Type:", type(selected_class))

    #Number of Years Smoked
    #The following should only appear if smoking status is current smoker or former smoker...need to write if statement
    smoke_years = st.number_input("Number of Years Smoking")
    if smoke_years < 0:
        st.error("Cannot be a negative number!")

    #Number of Packs Smoked per day
    ppd = st.number_input("Number of Packs Smoked Per Day")
    if ppd < 0:
        st.error("Cannot be a negative number!")

    #Pack Years calculator
    #Pack years = number of packs of cigarettes smoked per day multiplied by the number of years the person has smoked
    pack_years = ppd*smoke_years
    st.number_input("Pack Years",
                    value=pack_years, #Defaults to pack years
                    disabled=True) #User can't change it

    #HPV
    selected_class = st.radio("History of HPV", ['Yes', 'No'])
    st.write("History of HPV:", selected_class)

    #IUD
    selected_class = st.radio("IUD Present", ['Yes', 'No'])
    st.write("IUD Present:", selected_class)

    #IUD Years
    iud_years = st.number_input("Number of Years with IUD", step=1)
    if iud_years < 0:
        st.error("Cannot be a negative number!")

    #Age at first sexual intercourse
    age_first_sex = st.number_input("Age at First Sexual Intercourse", step=1)
    if age_first_sex < 0:
        st.error("Cannot be a negative number!")

    #Contraception years
    contracept_years = st.number_input("Number of Years with Contraception", step=1)
    if contracept_years < 0:
        st.error("Cannot be a negative number!")

    #Number of sexual partners
    num_sex_partners = st.number_input("Number of Lifetime Sexual Partners", step=1)
    if num_sex_partners < 0:
        st.error("Cannot be a negative number!")

    #Number of pregnancies
    num_pregnancies = st.number_input("Number of Lifetime Pregnancies", step=1)
    if num_pregnancies < 0:
        st.error("Cannot be a negative number!")

    #Number of STDs
    num_stds = st.number_input("Number of Lifetime STDs", step=1)
    if num_stds < 0:
        st.error("Cannot be a negative number!")

with tab4:
    st.header("Healthcare Near You")
    # Map
    st.markdown("This page allows you to find healthcare providers in your area who are qualified to perform cervical cancer screenings. ")
    # Requires a mapbox API access token? I signed up and got one...
    # Token: pk.eyJ1IjoibW9uYWFzY2hhIiwiYSI6ImNsZGFmaWkyeTBpbjMzcHBoanFrd3h2OG0ifQ.d1wdtlrj84uF--9OkL-o6w
    st.map()

with tab5:
    st.header("Patient and Healthcare Sign In")

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