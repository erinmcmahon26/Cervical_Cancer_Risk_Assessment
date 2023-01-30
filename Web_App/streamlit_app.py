from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image
"""
"""

image = Image.open('Web_App/VividHealth_Logo.png')
st.image(image)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "About Us", "Risk Assessment", "Find A Provider", "Image Upload", "Sign In"])

with tab1:
    st.header("Welcome")
    st.markdown("Hundreds of thousands of women are diagnosed with cervical cancer in the United States every year. Even when not fatal, 88% of patients experience potentially debilitating long-term effects including fertility problems, fatigue, and urinary/bowel issues (Health Europa 2018). This adds up to billions in healthcare costs annually, despite advances in detection and prevention which have made cervical cancer one of the most preventable forms of cancer (National Cancer Institute 2022). While incidence rates in the United States initially plummeted with the introduction of vaccinations and screenings, rates have stagnated in the past decade (Figure 1). This stagnation is avoidable – the CDC estimates that even today 93% of cervical cancer cases are preventable (CDC 2020). This speaks to a need to decrease mortality by improving diagnosis, screening rates, and screening accessibility. VividHealth proposes to address this gap by introducing an algorithmic risk assessment tool that can be integrated into electronic medical record (EMR) software. The tool will serve three types of users: medical providers, current patients, and prospective/new patients. The provider view will allow medical professionals to upload images from cervical cancer screenings into our trained models to help diagnose precancerous or cancerous cells. We will display these results in conjunction with demographic risk factors from a patient’s chart in an intuitive cervical cancer risk analysis dashboard. The patient view will show the risk assessment results, guidelines, and any messages added by their providers. Finally, the tool will also have a public-facing feature so anyone can find providers near them who can perform cervical cancer screenings. Our tool will first be focused on the United States with the intention of expanding it to other countries. We believe that it is necessary to provide the healthcare community with more tools to efficiently and successfully perform their jobs and provide the public with easily accessible information in one place.")

with tab2:
    st.header("About Us")
    st.markdown("VividHealth is a leading medical technology consulting firm that focuses on improving patient outcomes by incorporating new technologies into existing healthcare systems to aid with diagnosis, prevention, and outreach. "
                "We have partnered with Epic, an EMR company, to add new diagnostic capabilities into Epic’s Comprehensive Health Record software. "
                "We are passionate about delivering diagnostic information to assist clinical judgment and building interactive tools to enable patients to take control of their health. "
                "We created VividHealth out of our desire to make healthcare more accessible and cost effective. "
                "Having a positive impact in our community and helping others obtain necessary care motivates us to continue our current work. ")
    image_M = Image.open('Web_App/Mona.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_M, width=90)
    with col2:
        st.write("Mona Ascha is a doctor and working surgeon with six years of postgraduate clinical training in surgery. "
                 "She is an accomplished academic researcher with over 40 PubMed indexed peer reviewed articles. "
                 "She brings her medical expertise and prior experience with machine learning applications using healthcare data to cervical cancer image detection. "
                 "She seeks projects that intersect her passions for medicine and analytics.")
    image_J = Image.open('Web_App/Julia.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_J, width=90)
    with col2:
        st.write("Julia Ma is a software engineer with two years of professional experience in the government sector. "
                 "She has a diverse skill set including hardware simulation, signal processing, data engineering, data visualization, and NLP. "
                 "Her work with the government has given her an interest in data privacy and explainable AI.")
    image_E = Image.open('Web_App/Erin.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_E, width=90)
    with col2:
        st.write("Erin McMahon brings seven years of healthcare experience working in various hospital settings and in the community as a 911 EMT. "
                 "She is able to combine her knowledge of healthcare to her more recent work as a Project Manager and Data Scientist to address cervical cancer risk assessment. "
                 "As someone who has been able to beat cervical cancer due to successful preventative measures, screenings, and early treatment, she is passionate about assisting others to have a similar or better experience.")

    image_S = Image.open('Web_App/Sarah.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_S, width=90)
    with col2:
        st.write(
            "Sarah Rodenbeck is an AI professional specializing in natural language processing, AI-aided engineering, and responsible AI with experience in both industry and academia. "
            "Leveraging her technical background in computer science with years of professional experience in data science, she supports the full lifecycle of analytics projects from algorithmic design all the way through deployment. "
            "Sarah also brings expertise in AI ethics, governance, and privacy, and is passionate about human- and privacy-first designs that support positive changes in communities.")

    image_R = Image.open('Web_App/Rachel.png')
    col1, mid, col2 = st.columns([1, 3, 20])
    with col1:
        st.image(image_R, width=90)
    with col2:
        st.write(
            "Rachel Sickler is an ML engineer specializing in systems design and administration. "
            "She has four years of experience as a technical business analyst eliciting, confirming and documenting requirements, seven years of experience architecting and administering data pipelines and databases and has been building software for four years. "
            "Rachel brings experience working in health insurance, collaborating with state and federal agencies to ensure affordable coverage for patients in Vermont. "
            "Her work in public safety is what drives her passion for data privacy and using AI to improve society.")

    # can't figure out how to get the markdown to work but the columns did so that's cool!
    # st.markdown("""
    # <style>
    # .container {
    #     display: flex;
    # }
    # .logo-text {
    #     font-weight:700 !important;
    #     font-size:50px !important;
    #     color: #f9a01b !important;
    #     padding-top: 75px !important;
    # }
    # .logo-img {
    #     float:right;
    # }
    # </style>
    # """, unsafe_allow_html=True)

with tab3:
    st.header("Assess Your Cervical Cancer Risk")

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
    iud_years = st.number_input("Number of Years with IUD")
    if iud_years < 0:
        st.error("Cannot be a negative number!")

    #Age at first sexual intercourse
    age_first_sex = st.number_input("Age at First Sexual Intercourse")
    if age_first_sex < 0:
        st.error("Cannot be a negative number!")

    #Contraception years
    contracept_years = st.number_input("Number of Years with Contraception")
    if contracept_years < 0:
        st.error("Cannot be a negative number!")

    #Number of sexual partners
    num_sex_partners = st.number_input("Number of Lifetime Sexual Partners")
    if num_sex_partners < 0:
        st.error("Cannot be a negative number!")

    #Number of pregnancies
    num_pregnancies = st.number_input("Number of Lifetime Pregnancies")
    if num_pregnancies < 0:
        st.error("Cannot be a negative number!")

    #Number of STDs
    num_stds = st.number_input("Number of Lifetime STDs")
    if num_stds < 0:
        st.error("Cannot be a negative number!")

with tab4:
    st.header("Find A Healthcare Provider Near You")
    # Map
    st.subheader("Find a Provider")
    # Requires a mapbox API access token? I signed up and got one...
    # Token: pk.eyJ1IjoibW9uYWFzY2hhIiwiYSI6ImNsZGFmaWkyeTBpbjMzcHBoanFrd3h2OG0ifQ.d1wdtlrj84uF--9OkL-o6w
    st.map()

with tab5:
    st.header("Upload an Image to Assess Cervical Cancer Risk")
    uploaded_file = st.file_uploader("Choose a file",
                                     type=None,
                                     accept_multiple_files=False, #only accept one file at a time
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

with tab6:
    st.header("Patient and Healthcare Sign In")

# selected_class = st.radio("Select User", ['Provider', 'Current Patient', 'New Patient'])
# st.write("Select User:", selected_class)
# st.write("Select User Type:", type(selected_class))
