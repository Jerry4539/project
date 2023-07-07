import pickle
from PIL import Image
import streamlit as st
from streamlit.elements import button
from htbuilder.funcs import rgba, rgbs
from htbuilder.units import percent, px
from streamlit_option_menu import option_menu
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# cred = credentials.Certificate('C:/Users/Sahua/Documents/projects/Ashwini/Web-Interface/firebase/ash-project.json')
# firebase_admin.initialize_app(cred)

# //////////////////////////////////////////// #
# TitleBar Code #
# //////////////////////////////////////////// #

# configure the Icons && title of the website
im = Image.open("assets/icons.png")
st.set_page_config(
    page_title="Ashwini HealthCare",
    page_icon=im,
    layout="wide",
)

# //////////////////////////////////////////// #
# Module Import #
# //////////////////////////////////////////// #

# Loading the Saved Models 
dia_model = pickle.load(open(r'C:/Users/Sahua/Documents/projects/Ashwini/Web-Interface/Models/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open(r'C:/Users/Sahua/Documents/projects/Ashwini/Web-Interface/Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(r'C:/Users/Sahua/Documents/projects/Ashwini/Web-Interface/Models/parkinsons_model.sav', 'rb'))

# //////////////////////////////////////////// #
# Css Code #
# //////////////////////////////////////////// #

def app():
    st.markdown(
        """
        <style>
        .title {
            color: black;
            text-align: center;
            padding: 1rem;
            font-size: 2.5rem;
        }

        .sidebar {
            background-color: #F0F8FF;
            padding: 2rem;
        }

        .container {
            margin-top: 5rem;
            text-align: center;
        }

        .stButton button {
            border-color: blue !important;
        }

        .stProgress > div > div {
            background-color: blue !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# //////////////////////////////////////////// #
# MenuBar Code #
# //////////////////////////////////////////// #

# Sidebar for Navigation
with st.sidebar:
    selected = option_menu('Health Care System',
                           ['Home',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Settings'],
                           icons=['house-fill',
                                  'clipboard2-pulse-fill',
                                  'heart-fill',
                                  'person-fill',
                                  'gear-fill'],
                           menu_icon='hospital-fill',
                           default_index=4)

# //////////////////////////////////////////// #
# Home Page Code #
# //////////////////////////////////////////// #

if selected == 'Home':
    st.write("# Welcome to :orange[HealthCare System].")
    st.markdown("""
    I am **Ashwini**, A Finnal Year Student Of BscIT form **Valia College**.
    I Made this Health Care System using Completely **Python**.
    I use machine learning techknowledge for making this module, Which Predict some Big Desises, Like. **'*Diabetes', 'Heart' and 'Parkinson's*'**
        
        ### What i used ?
        - I use [*Google Colab*](colab.research.google.com/) for Developing The Modules. 
        - I used Some Python [*Pre-build Modules also*](https://docs.streamlit.io).
        - I also Take help of [*StackOverFlow*](https://stackoverflow.com/).
        - And At Last my College Guide.  
        
        ## Thank you all to help me in make this Done.  
    """)

# //////////////////////////////////////////// #
# Diabetes Page Code #
# //////////////////////////////////////////// #

if selected == 'Diabetes Prediction':
    # Css for Module
    st.markdown(
        """
        <style>
        .btn-2 {
            border-radius: 1rem;
            color: #ffffff;
            background-color: #00A4CC;
            border: none;
            display: inline-block;
            padding: 0.5rem 1rem;
            font-size: 1.5rem;
            margin-top: 1rem;
            transition-duration: 0.4s;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Module Title
    st.markdown("<h1 class='title'> Diabetes Prediction </h1>", unsafe_allow_html=True)

    # Form
    st.write("<hr/>", unsafe_allow_html=True)
    st.markdown("<h2 class='title'> Features: </h2>", unsafe_allow_html=True)

    # Getting the Features from the User
    Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=17, value=3)
    Glucose = st.number_input("Glucose", min_value=0, max_value=200, value=127)
    BloodPressure = st.number_input("BloodPressure", min_value=0, max_value=122, value=70)
    SkinThickness = st.number_input("SkinThickness", min_value=0, max_value=99, value=26)
    Insulin = st.number_input("Insulin", min_value=0, max_value=846, value=94)
    BMI = st.number_input("BMI", min_value=0.0, max_value=67.1, value=27.3)
    DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction", min_value=0.078, max_value=2.42, value=0.527)
    Age = st.number_input("Age", min_value=0, max_value=81, value=31)

    # Predict Button
    if st.button("Predict"):
        features = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        prediction = dia_model.predict([features])[0]
        if prediction == 0:
            st.error("The person is not likely to have diabetes.")
        else:
            st.success("The person is likely to have diabetes.")

# //////////////////////////////////////////// #
# Heart Disease Page Code #
# //////////////////////////////////////////// #

if selected == 'Heart Disease Prediction':
    # Css for Module
    st.markdown(
        """
        <style>
        .btn-2 {
            border-radius: 1rem;
            color: #ffffff;
            background-color: #00A4CC;
            border: none;
            display: inline-block;
            padding: 0.5rem 1rem;
            font-size: 1.5rem;
            margin-top: 1rem;
            transition-duration: 0.4s;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Module Title
    st.markdown("<h1 class='title'> Heart Disease Prediction </h1>", unsafe_allow_html=True)

    # Form
    st.write("<hr/>", unsafe_allow_html=True)
    st.markdown("<h2 class='title'> Features: </h2>", unsafe_allow_html=True)

    # Getting the Features from the User
    age = st.number_input("Age", min_value=0, max_value=120, value=54)
    sex = st.selectbox("Sex", ['Male', 'Female'])
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=125)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, value=210)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=250, value=170)
    exang = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.6)
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

    # Predict Button
    if st.button("Predict"):
        # Preprocessing the Features
        if sex == 'Male':
            sex = 1
        else:
            sex = 0

        features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        prediction = heart_model.predict([features])[0]
        if prediction == 0:
            st.error("The person is not likely to have heart disease.")
        else:
            st.success("The person is likely to have heart disease.")

# //////////////////////////////////////////// #
# Parkinson's Page Code #
# //////////////////////////////////////////// #
if selected == 'Parkinsons Prediction':
    # Css for Module
    st.markdown(
        """
        <style>
        .btn-2 {
            border-radius: 1rem;
            color: #ffffff;
            background-color: #00A4CC;
            border: none;
            display: inline-block;
            padding: 0.5rem 1rem;
            font-size: 1.5rem;
            margin-top: 1rem;
            transition-duration: 0.4s;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Module Title
    st.markdown("<h1 class='title'> Parkinson's Disease Prediction </h1>", unsafe_allow_html=True)

    # Form
    st.write("<hr/>", unsafe_allow_html=True)
    st.markdown("<h2 class='title'> Features: </h2>", unsafe_allow_html=True)

    # Getting the Features from the User
    MDVP_Fo = st.number_input("MDVP:Fo (Hz)", min_value=0.0, max_value=300.0, value=119.992)
    MDVP_Fhi = st.number_input("MDVP:Fhi (Hz)", min_value=0.0, max_value=300.0, value=157.302)
    MDVP_Flo = st.number_input("MDVP:Flo (Hz)", min_value=0.0, max_value=300.0, value=74.997)
    MDVP_Jitter = st.number_input("MDVP:Jitter", min_value=0.0, max_value=2.0, value=0.00784)
    MDVP_Jitter_Abs = st.number_input("MDVP:Jitter(Abs)", min_value=0.0, max_value=2.0, value=0.00003)
    RAP = st.number_input("MDVP:RAP", min_value=0.0, max_value=2.0, value=0.00370)
    PPQ = st.number_input("MDVP:PPQ", min_value=0.0, max_value=2.0, value=0.00554)
    DDP = st.number_input("Jitter:DDP", min_value=0.0, max_value=2.0, value=0.01109)
    MDVP_Shimmer = st.number_input("MDVP:Shimmer", min_value=0.0, max_value=2.0, value=0.04374)
    shimmer_dB = st.number_input("MDVP:Shimmer(dB)", min_value=0.0, max_value=35.0, value=0.426)
    APQ3 = st.number_input("Shimmer:APQ3", min_value=0.0, max_value=25.0, value=0.02971)
    APQ5 = st.number_input("Shimmer:APQ5", min_value=0.0, max_value=25.0, value=0.03130)
    APQ = st.number_input("MDVP:APQ", min_value=0.0, max_value=25.0, value=0.02971)
    DDA = st.number_input("Shimmer:DDA", min_value=0.0, max_value=50.0, value=0.08868)
    NHR = st.number_input("NHR", min_value=0.0, max_value=2.0, value=0.01393)
    HNR = st.number_input("HNR", min_value=0.0, max_value=35.0, value=21.0)
    RPDE = st.number_input("RPDE", min_value=0.0, max_value=3.0, value=0.414783)
    DFA = st.number_input("DFA", min_value=0.0, max_value=3.0, value=0.815285)
    spread1 = st.number_input("spread1", min_value=-10.0, max_value=10.0, value=-4.813031)
    spread2 = st.number_input("spread2", min_value=-10.0, max_value=10.0, value=0.266482)
    D2 = st.number_input("D2", min_value=0.0, max_value=10.0, value=2.301442)
    PPE = st.number_input("PPE", min_value=0.0, max_value=10.0, value=0.284654)

    # Predict Button
    if st.button("Predict"):
        features = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, RAP, PPQ, DDP,
                    MDVP_Shimmer, shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        prediction = parkinsons_model.predict([features])[0]
        if prediction == 0:
            st.error("The person is not likely to have Parkinson's disease.")
        else:
            st.success("The person is likely to have Parkinson's disease.")


# //////////////////////////////////////////// #
# Settings Page Code #
# //////////////////////////////////////////// #

if selected == 'Settings':
    st.write("# This is the Settings page.")
    st.write("You can customize your preferences here.")

# //////////////////////////////////////////// #
# Initialize the App #
# //////////////////////////////////////////// #

app()
