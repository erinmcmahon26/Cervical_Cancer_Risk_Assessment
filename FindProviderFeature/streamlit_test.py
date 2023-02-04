import streamlit as st
#import streamlit_authenticator as stauth
import yaml
#from PIL import Image
# from collections import namedtuple
# import altair as alt
from yaml import SafeLoader

#imports needed for find provider feature
import pandas as pd
import requests
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import json
from streamlit_folium import folium_static
import folium
import numpy as np
from streamlit_js_eval import get_geolocation
from st_aggrid import GridOptionsBuilder, AgGrid, ColumnsAutoSizeMode, GridUpdateMode, DataReturnMode


st.set_page_config(
    page_title="VividHealth",
    layout="wide"
)

url = 'postgresql+psycopg2://postgres:password@localhost/npiProviders'
engine = create_engine(url)

tab1,tab4 = st.tabs(["Find A Provider","Home"])

with tab1:
    def searchAddr(addr_in):
        addr_input.replace(" ","+")
        addr_input.replace(",","")
        r = requests.get(f"https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address={addr_input}&benchmark=public_AR_Current&format=json")
        response = json.loads(r.text)
        if len(response['result']['addressMatches']) >0:
            lon_search = response["result"]["addressMatches"][0]["coordinates"]["x"]
            lat_search = response["result"]["addressMatches"][0]["coordinates"]["y"]
            return lon_search,lat_search
        else: raise ValueError("No address Found")

    def getLocation():
        loc = get_geolocation()
        if loc != None:
            lat_search = loc['coords']['latitude']
            lon_search = loc['coords']['longitude']
            return lon_search,lat_search
        else: raise TypeError("Location Blocked")

    def findProviders(lon_search,lat_search):
        query = f'SELECT *, ST_DISTANCE(ST_MakePoint({lon_search},{lat_search})::geography,"geom")/1609.344 as Distance\
                FROM npi_registry \
                ORDER BY Distance \
                limit 20;'
            # "geom" <-> ST_MakePoint({lon_search},{lat_search})::geography\

        return pd.read_sql(query,engine)

    def populateMarkers(df,m):
        for i in df['geom'].unique():
            temp = df[df['geom']==i]
            li = temp.iloc[0].values.tolist()
            lon,lat = li[1],li[2]
            street_addr = li[3]
            phone = str(li[7])     
            providers = f"Provider(s):<ul><li>{li[5]}</lu>"
            for i in range(1,len(temp)):
                li = temp.iloc[i].values.tolist()
                providers+=f"<li>{li[5]}</li>"    
            popuptext = f"<div style=\"font-family:verdana\">{street_addr}<br><br>Phone Number: {phone}<br><br>{providers}</ul></div>"
            popup = folium.Popup(folium.IFrame(popuptext),min_width=300,max_width=300)
            folium.Marker([lat, lon], popup=popup,icon=folium.Icon(color='red',prefix='fa',icon='stethoscope'),tooltip=tooltip).add_to(m)
        
    def bounds(df):
        lats = df[['LAT']].to_numpy().astype(float)
        lats = np.append(lats,lat_search)
        lons = df[['LON']].to_numpy().astype(float)
        lons = np.append(lons,lon_search)
        sw = [min(lats),min(lons)]
        ne = [max(lats),max(lons)]
        return sw,ne

    def toggle_addr():
        st.session_state.loc = False        
    def toggle_loc():
        if not check:
            st.session_state.loc = True 
        if check:
            st.session_state.loc = False  

    st.header("Healthcare Near You")
    st.markdown("This page allows you to find healthcare providers in your area who are can provide cervical cancer screenings. ")
    col1,col2 = st.columns(2)
    with col1:
        st.write('')
        st.write('')
        check = st.checkbox("Use My Current Location",value=False,key='loc',on_change=toggle_loc)
    with col2:
        addr_input = st.text_input(label="Or, Enter an Address Here:",key='addr',value="633 Clark St, Evanston, IL 60208",on_change=toggle_addr)
    if addr_input =="":
        st.error("Please enter a valid address")
    else:
        try: 
            if st.session_state.loc==True:
                lon_search,lat_search = getLocation()
            else:
                lon_search,lat_search= searchAddr(addr_input)
            df = findProviders(lon_search,lat_search)
            f = folium.Figure(width=2000, height=500)
            m = folium.Map(location=[lat_search,lon_search]).add_to(f)
            folium.Marker([lat_search, lon_search],icon=folium.Icon(color='blue',prefix='fa',icon='home')).add_to(m)
            tooltip = "Click for Provider Information"
            df = df.fillna("")
            populateMarkers(df,m)
            sw,ne = bounds(df)
            m.fit_bounds([sw, ne]) 
            folium_static(m)
            df_show = df[['distance','ProviderName','PrimarySpecialty','PracticePhoneNum','AddressFound','ProviderGender']]
            df_show['distance'] = df_show['distance'].round(2)
            df_show.columns = ['Distance (Miles)','Provider Name','Primary Specialty','Phone Number','Address','Provider Gender']
            st.markdown('#### Explore Providers Near You')
            st.dataframe(df_show)
        except ValueError as err:
            st.error("Address not found! Please try another address.")
        except TypeError as err:
            st.error('You must enable location services to use this feature')