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
