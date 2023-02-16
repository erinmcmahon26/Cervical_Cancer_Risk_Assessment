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

st.header("Assess Your Cervical Cancer Risk")
st.markdown('<p style="font-family:sans serif; font-size: 20px;"> This page allows you to enter information about yourself in order to see what your overall risk for cervical cancer is currently. '
            'While some of these questions may seem very personal, they are necessary to accuretly determine your risk. If you are wondering why we are asking specific questions'
            'or if you do not understand, just take a look at the information icon below each question!',
            unsafe_allow_html=True)
# Risk factor tool
st.subheader("Risk Factor Calculator")

#Age
age_min = st.number_input("Age")
st.info("\n We are asking this because you must be at least 21 years of age to use this tool.", icon="ℹ️")

#Number of Years Smoked
#The following should only appear if smoking status is current smoker or former smoker...need to write if statement
smoke_years = st.number_input("Number of Years Smoking")
if smoke_years < 0:
    st.error("Cannot be a negative number!")
st.info("\n This will be used to calculate your smoking pack years.", icon="ℹ️")

#Number of Packs Smoked per day
ppd = st.number_input("Number of Packs Smoked Per Day")
if ppd < 0:
    st.error("Cannot be a negative number!")
st.info("\n This will be used to calculate your smoking pack years.", icon="ℹ️")

#Pack Years calculator
#Pack years = number of packs of cigarettes smoked per day multiplied by the number of years the person has smoked
pack_years = ppd*smoke_years
st.number_input("Pack Years",
                value=pack_years, #Defaults to pack years
                disabled=True) #User can't change it
st.info("\n We are calculating this because smoking increases your risk of cervical cancer.", icon="ℹ️")

#IUD Years
iud_years = st.number_input("Number of Years with IUD", step=1)
if iud_years < 0:
    st.error("Cannot be a negative number!")
st.info("If you never had an IUD, write 0. Having an IUD can decrease your cervical cancer risk.", icon="ℹ️")

#Age at first sexual intercourse
age_first_sex = st.number_input("Age at First Sexual Intercourse", step=1)
if age_first_sex < 0:
    st.error("Cannot be a negative number!")
st.info("We are asking this because earlier age at first intercourse can increase your cervical cancer risk.", icon="ℹ️")

#Contraception years
contracept_years = st.number_input("Number of Years with Contraception", step=1)
if contracept_years < 0:
    st.error("Cannot be a negative number!")
st.info("If you never had contraception, write 0. Having contraception can decrease your cervical cancer risk.", icon="ℹ️")

#Number of sexual partners
num_sex_partners = st.number_input("Number of Lifetime Sexual Partners", step=1)
if num_sex_partners < 0:
    st.error("Cannot be a negative number!")
st.info("We are asking this because greater number of sexual partners can increase your cervical cancer risk.", icon="ℹ️")

#Number of pregnancies
num_pregnancies = st.number_input("Number of Lifetime Pregnancies", step=1)
if num_pregnancies < 0:
    st.error("Cannot be a negative number!")
st.info("We are asking this because greater number of pregnancies can increase your cervical cancer risk.", icon="ℹ️")

#Number of STDs
num_stds = st.number_input("Number of Lifetime STDs", step=1)
if num_stds < 0:
    st.error("Cannot be a negative number!")
st.info("We are asking this because greater number of STDs can increase your cervical cancer risk.", icon="ℹ️")