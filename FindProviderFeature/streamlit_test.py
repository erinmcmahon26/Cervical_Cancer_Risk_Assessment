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
from streamlit_folium import folium_static
import folium
import numpy as np
from streamlit_js_eval import get_geolocation
import streamlit.components.v1 as components

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
        query = f'SELECT *\
                FROM npi_registry \
                ORDER BY "geom" <-> ST_MakePoint({lon_search},{lat_search})::geography\
                limit 20;'
        return pd.read_sql(query,engine)

    def populateMarkers(df,m):
        for i in df['geom'].unique():
            temp = df[df['geom']==i]
            li = temp.iloc[0].values.tolist()
            lon,lat = li[31],li[32]
            street_addr = li[7]+" "+li[8]
            city_state = li[9]+", "+li[10]+" "+str(li[11]//10000)
            phone = str(li[13])
            phone = phone[:3]+"-"+phone[3:6]+"-"+phone[6:]
            providers = f"Provider(s):<ul><li>{li[2]} {li[3]} {li[1]} {li[5]}, {li[6]} </li>"
            for i in range(1,len(temp)):
                li = temp.iloc[i].values.tolist()
                providers+=f"<li>{li[2]} {li[3]} {li[1]} {li[5]}, {li[6]} </li>"
            providers = providers.replace(",  ","").replace("  ", " ").replace(" ,",",")
            popuptext = f"<div style=\"font-family:verdana\">{street_addr}<br>{city_state}<br><br>Phone Number: {phone}<br><br>{providers}</ul></div>"
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

    st.header("Healthcare Near You")
    st.markdown("This page allows you to find healthcare providers in your area who are can provide cervical cancer screenings. ")
    col1,col2 = st.columns(2)
    flag = False
    with col1:
        st.write('')
        st.write('')
        check = st.checkbox("Use My Current Location",value=True) #False)
        if check: flag=True    
    with col2:
        addr_input = st.text_input(label="Or, Enter an Address Here:",value="633 Clark St, Evanston, IL 60208")
    
    if addr_input =="":
        st.error("Please enter a valid address")
    else:
        try: 
            if flag:
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

        except ValueError as err:
            st.error("Address not found! Please try another address.")
        except TypeError as err:
            st.error('You must enable location services to use this feature')

#TODO also display table with all providers?        
#TODO finish custom component
components.html("""
<script>
const doc = window.parent.document 
const textbox = doc.querySelector('[aria-label="Or, Enter an Address Here:"]');
const checkbox = doc.querySelector(.st-e0); 
const check = doc.querySelector('[aria-label="Use My Current Location"]'); 
console.log(textbox)
console.log(checkbox)
console.log(check)
textbox.addEventListener('keypress', function (event) {
    if (event.key === 'Enter') {
        console.log("Enter pressed")
        checkbox.classList.toggle('class');
        check.setAttribute("aria-checked","false")
    }
});
</script>
""", height=0, width=0)


        
    
        