import streamlit as st
from PIL import Image
# from collections import namedtuple
# import altair as alt
# import pandas as pd

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


image_banner = Image.open('images/banner.png')
st.image(image_banner, use_column_width=True)
st.markdown('<p style="font-family:sans serif; font-size: 22px;"> According to the World Health Organization, cervical cancer is the fourth most common cancer among women globally with about 600,000 new cases documented in 2020. '
            'Of these new cases, there were an estimated 342,000 deaths in 2020 alone. '
            'Yet, the CDC estimates that even today 93% of cervical cancer cases are preventable, when healthcare guidelines are followed <sup>1</sup>. '
            'To address this discrepancy between cervical cancer incidence and effectiveness of preventative measures, VividHealth has created this multifunction and easy to use website.',
            unsafe_allow_html=True)
st.write("")

image_rib = Image.open('images/ribbon.png')
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

image_map = Image.open('images/map.png')
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

image_health = Image.open('images/healthcare.png')
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