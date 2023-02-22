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
            body {font-family: "Gill Sans", sans-serif;}
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown('''<style>
        * {font-family: \"Gill Sans\", sans-serif; font-size:20px}
        .featcategory1{
            background: rgba(90,197,194,0.3);
            border-radius: 15px 50px;
            text-align: left;
            font-size:28px;
            padding: 25px;
            color:black;
        }
        .featcategory2{
            background: rgba(90,197,194,0.3);
            border-radius: 50px 15px;
            text-align: left;
            font-size:28px;
            padding: 25px;
            color:black;
        }
        a, a:link, a:hover, a:visited, a:active {
            color: inherit;
            text-decoration: none;
        }
        </style>''',unsafe_allow_html=True)

image_logo = Image.open('images/VividHealth_Logo.png')
st.image(image_logo, width=407)


image_banner = Image.open('images/banner.png')
st.image(image_banner, use_column_width=True)
st.markdown('<p style= font-size: 22px;"> According to the World Health Organization, cervical cancer is the fourth most common cancer among women globally with about 600,000 new cases documented in 2020. '
            'Of these new cases, there were an estimated 342,000 deaths in 2020 alone. '
            'Yet, the CDC estimates that even today 93% of cervical cancer cases are preventable, when healthcare guidelines are followed<sup>1</sup>. '
            'To address this discrepancy between cervical cancer incidence and effectiveness of preventative measures, VividHealth has created this multifunctional and easy-to-use website.',
            unsafe_allow_html=True)
st.write("")

image_rib = Image.open('images/ribbon_transparent.png')
col1, mid, col2 = st.columns([3, 2, 20])
with col1:
    st.write("")
    st.write("")
    st.image(image_rib, use_column_width=True)
with col2:
    st.write("")
    st.write("")
    st.markdown(f'''<div class=featcategory1><a target ="_self" href="http://localhost:8501/Risk_Assessment">Personal Risk Assessment<p>Check your own cervical cancer risk on the Risk Assessment tab. Our easy-to-use platform will ask a series of questions that can be significant predictors for assessing if your risk of developing cervical cancer.</p></a></div>''', unsafe_allow_html=True)
    # st.markdown('<a target ="_self" href="http://localhost:8501/Risk_Assessment"><p style="font-size: 28px;"> <strong>Personal Risk Assessment</a>', unsafe_allow_html=True)
    # st.markdown('<p> Check your own cervical cancer risk on the Risk Assessment tab. Our easy to use platform will ask a series of questions that can be significant predictors for assessing if you '
    #             'are at risk of developing cervical cancer.', unsafe_allow_html=True)

image_map = Image.open('images/map.png')
col1, mid, col2 = st.columns([20, 0.5, 4])
with col1:
    st.write("")
    st.write("")
    st.markdown(f'''<div class=featcategory2><a target ="_self" href="http://localhost:8501/Find_A_Provider"> Find A Provider Near You<p>Use our Find A Provider tab to locate a healthcare professional near you who is qualified to work with you through your cervical cancer screenings and treatment.</p></a></div>''', unsafe_allow_html=True)
    #st.markdown('<a target ="_self" href="http://localhost:8501/Find_A_Provider"><p style="font-size: 28px;"> <strong>Find A Provider Near You</a>', unsafe_allow_html=True)
    #st.markdown('<p class=featcategory> Use our Find A Provider tab to locate a healthcare professional near you who is qualified to work with you through your cervical cancer screenings and treatment. ',
   #              unsafe_allow_html=True)
with col2:
    st.write("")
    st.write("")
    st.image(image_map, use_column_width=True)
st.write("")
st.write("")

image_health = Image.open('images/healthcare.png')
col1, mid, col2 = st.columns([3, 2, 20])
with col1:
    st.write("")
    st.write("")
    st.image(image_health, use_column_width=True)
with col2:
    st.write("")
    st.write("")
    st.markdown(f'''<div class=featcategory1><a target ="_self" href="http://localhost:8501/Sign_In">Patient and Provider Portal<p>Use our Sign In tab to access the patient and healthcare provider portal. This portal is where you will be able to communicate with your provider about recent test, questions, or any concerns.</p></a></div>''', unsafe_allow_html=True)
    # st.markdown('<a target ="_self" href="http://localhost:8501/Sign_In"><p style="font-size: 28px;"> <strong>Patient and Provider Portal</a>',unsafe_allow_html=True)
    # st.markdown('<p> Use our Sign In tab to access the patient and healthcare provider portal. This portal is where you will be able to communicate with your provider about recent test, questions, '
    #              'or any concerns.', unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
citation1 = '<p style="font-size: 14px;"> <sup>1</sup>https://www.cdc.gov/vitalsigns/cervical-cancer/index.html'
st.markdown(citation1, unsafe_allow_html=True)