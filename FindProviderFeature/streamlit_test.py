import streamlit as st
#import streamlit_authenticator as stauth
import yaml
#from PIL import Image
# from collections import namedtuple
# import altair as alt
import pandas as pd
from yaml import SafeLoader
import requests
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import json

st.set_page_config(
    page_title="VividHealth",
    layout="wide"
)

url = 'postgresql+psycopg2://postgres:password@localhost/npiProviders'
engine = create_engine(url)

tab1,tab4 = st.tabs(["Find A Provider","Home"])

with tab1:
    st.header("Healthcare Near You")
    # Map
    st.markdown("This page allows you to find healthcare providers in your area who are qualified to perform cervical cancer screenings. ")
    addr_input = st.text_input(label="Enter your address here",value="1600 Pennsylvania Ave Washington DC")
    addr_input.replace(" ","+")
    addr_input.replace(",","")
    r = requests.get(f"https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={addr_input}&benchmark=public_AR_Current&format=json")
    response = json.loads(r.text)
    if len(response['result']['addressMatches']) >0:
        lon = response["result"]["addressMatches"][0]["coordinates"]["x"]
        lat = response["result"]["addressMatches"][0]["coordinates"]["y"]
        query = f'SELECT *\
            FROM npi_registry \
            WHERE "ProviderGender"=\'F\'\
            ORDER BY "geom" <-> ST_MakePoint({lon},{lat})::geography\
            limit 10;'
        df = pd.read_sql(query,engine)
    else:
        st.text("Address not found!")
    # Requires a mapbox API access token? I signed up and got one...
    # Token: pk.eyJ1IjoibW9uYWFzY2hhIiwiYSI6ImNsZGFmaWkyeTBpbjMzcHBoanFrd3h2OG0ifQ.d1wdtlrj84uF--9OkL-o6w
    st.map(df)
