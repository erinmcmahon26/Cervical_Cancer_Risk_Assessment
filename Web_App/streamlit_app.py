from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image
"""
"""

image = Image.open('VividHealth_Logo.png')
st.image(image)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "About Us", "Risk Assessment", "Find A Provider", "Sign In"])

with tab1:
    st.header("Will add something here soon")

with tab2:
    st.header("About Us")
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
    age_min = st.number_input("Age")
    if age_min < 21:
        st.error("You are too young to use this tool!")
    else:
        st.success("You are old enough to use this tool!")

    selected_class = st.radio("Smoking Status", ['Current smoker', 'Former Smoker', 'Never Smoker'])
    st.write("Smoking Status:", selected_class)
    # st.write("Smoking Status Type:", type(selected_class))

    selected_class = st.radio("History of HPV", ['Yes', 'No'])
    st.write("History of HPV:", selected_class)

with tab4:
    st.header("Find A Healthcare Provider Near You")
    # Map
    st.subheader("Find a Provider")
    # Requires a mapbox API access token? I signed up and got one...
    # Token: pk.eyJ1IjoibW9uYWFzY2hhIiwiYSI6ImNsZGFmaWkyeTBpbjMzcHBoanFrd3h2OG0ifQ.d1wdtlrj84uF--9OkL-o6w
    st.map()

with tab5:
    st.header("Patient and Healthcare Sign In")

# selected_class = st.radio("Select User", ['Provider', 'Current Patient', 'New Patient'])
# st.write("Select User:", selected_class)
# st.write("Select User Type:", type(selected_class))
