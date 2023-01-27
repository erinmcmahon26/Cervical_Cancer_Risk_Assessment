from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


"""
"""
st.title('VividHealth')
st.subheader("Streamlit Demo")

selected_class = st.radio("Select User", ['Provider', 'Current Patient', 'New Patient'])
st.write("Select User:", selected_class)
# st.write("Select User Type:", type(selected_class))

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

# Map
st.subheader("Find a Provider")
# Requires a mapbox API access token? I signed up and got one...
# Token: pk.eyJ1IjoibW9uYWFzY2hhIiwiYSI6ImNsZGFmaWkyeTBpbjMzcHBoanFrd3h2OG0ifQ.d1wdtlrj84uF--9OkL-o6w
st.map()
