import streamlit as st
from PIL import Image

im = Image.open('images/favicon.png')
st.set_page_config(
    page_title="VividHealth",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded"
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

st.header("Patient and Provider Portal")
def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.subheader("The results of your cervical cancer risk assessment and pap smear are provided below:")
    st.write("waiting for categorization results from Mona and Julia to fill this one out :)")
    st.write("Upload image below")
    uploaded_file = st.file_uploader("Choose a file",
                                    type=None,
                                    accept_multiple_files=False,  # only accept one file at a time
                                    key=None,
                                    help=None,
                                    on_change=None,
                                    disabled=False,
                                    label_visibility="visible")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        # To read file as bytes:
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)