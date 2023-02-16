import streamlit as st
from PIL import Image

im = Image.open('images/favicon.png')
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

image_logo = Image.open('images/VividHealth_Logo.png')
st.image(image_logo, width=407)

st.header("VividHealth Team")
st.markdown('<p style="font-family:sans serif; font-size: 20px;"> VividHealth is a leading medical technology consulting firm that focuses on improving patient outcomes by incorporating new technologies into existing healthcare systems to aid with diagnosis, prevention, and outreach. '
            'We have partnered with Epic, an EMR company, to add new diagnostic capabilities into Epic’s Comprehensive Health Record software. '
            'We are passionate about delivering diagnostic information to assist clinical judgment and building interactive tools to enable patients to take control of their health. '
            'We created VividHealth out of our desire to make healthcare more accessible and cost effective. '
            'Having a positive impact in our community and helping others obtain necessary care motivates us to continue our current work. ',
             unsafe_allow_html=True)
st.write("")
st.write("")
image_M = Image.open('images/Mona.jpg')
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
image_J = Image.open('images/Julia.jpg')
col1, mid, col2 = st.columns([3, 1, 15])
with col1:
    st.image(image_J, use_column_width=True)
with col2:
    st.markdown('<p style="font-family:sans serif; font-size: 20px;"> <u><strong>Julia Ma</strong></u> is a software engineer with two years of professional experience in the government sector. '
                'She has a diverse skill set including hardware simulation, signal processing, data engineering, data visualization, and NLP. '
                'Her work with the government has given her an interest in data privacy and explainable AI.',
                unsafe_allow_html=True)
st.write("___________________")
image_E = Image.open('images/Erin.JPG')
col1, mid, col2 = st.columns([3, 1, 15])
with col1:
    st.image(image_E, use_column_width=True)
with col2:
    st.markdown('<p style="font-family:sans serif; font-size: 20px;"> <u><strong>Erin McMahon</strong></u> brings seven years of healthcare experience working in various hospital settings and in the community as a 911 EMT. '
                'She is able to combine her knowledge of healthcare to her more recent work as a Project Manager and Data Scientist to address cervical cancer risk assessment. '
                'As someone who has been able to beat cervical cancer due to successful preventative measures, screenings, and early treatment, she is passionate about assisting others to have a similar or better experience.',
                unsafe_allow_html=True)
st.write("___________________")
image_S = Image.open('images/Sarah.jpeg')
col1, mid, col2 = st.columns([3, 1, 15])
with col1:
    st.image(image_S, use_column_width=True)
with col2:
    st.markdown('<p style="font-family:sans serif; font-size: 20px;"> <u><strong>Sarah Rodenbeck</strong></u> is an AI professional specializing in natural language processing, AI-aided engineering, and responsible AI with experience in both industry and academia. '
                'Leveraging her technical background in computer science with years of professional experience in data science, she supports the full lifecycle of analytics projects from algorithmic design all the way through deployment. '
                'Sarah also brings expertise in AI ethics, governance, and privacy, and is passionate about human- and privacy-first designs that support positive changes in communities.',
                unsafe_allow_html=True)
st.write("___________________")
image_R = Image.open('images/Rachel.jpg')
col1, mid, col2 = st.columns([3, 1, 15])
with col1:
    st.image(image_R, use_column_width=True)
with col2:
    st.markdown('<p style="font-family:sans serif; font-size: 20px;"> <u><strong>Rachel Sickler</strong></u> is an ML engineer specializing in systems design and administration. '
                'She has four years of experience as a technical business analyst eliciting, confirming and documenting requirements, seven years of experience architecting and administering data pipelines and databases and has been building software for four years. '
                'Rachel brings experience working in health insurance, collaborating with state and federal agencies to ensure affordable coverage for patients in Vermont. '
                'Her work in public safety is what drives her passion for data privacy and using AI to improve society.',
                unsafe_allow_html=True)