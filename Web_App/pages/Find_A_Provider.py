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

st.header("Healthcare Near You")
st.markdown("This page allows you to find healthcare providers in your area who are qualified to perform cervical cancer screenings. ")