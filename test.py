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

cred = credentials.Certificate('C:/Users/Sahua/Documents/projects/Ashwini/Web-Interface/firebase/ash-project.json')
firebase_admin.initialize_app(cred)


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
                                'Settings',],
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

        #### Learn Something about this Desises 🤔
        - **[*Parkinson's*](https://www.kaggle.com/datasets/vikasukani/parkinsons-disease-data-set) Data Set.**

        This dataset is composed of a range of biomedical voice measurements from 31 people, 23 with Parkinson's disease (PD).
        Each column in the table is a particular voice measure, and each row corresponds to one of 195 voice recordings from these individuals ("name" column). 
        The main aim of the data is to discriminate healthy people from those with PD, according to the "status" column which is set to 0 for healthy and 1 for PD.
        The data is in ASCII CSV format. The rows of the CSV file contain an instance corresponding to one voice recording. 
        There are around six recordings per patient, the name of the patient is identified in the first column.
        For further information or to pass on comments, please contact Max Little (little '@' robots.ox.ac.uk).

        Further details are contained in the following reference -- if you use this dataset, please cite:
        Max A. Little, Patrick E. McSharry, Eric J. Hunter, Lorraine O. 
        Ramig (2008), 'Suitability of dysphonia measurements for telemonitoring of Parkinson's disease', 
        IEEE Transactions on Biomedical Engineering (to appear).
    """)
            st.image('assets/parkinsons.jpg')

            st.markdown("""
            - **[*Diabetes*](https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset) Data Set.**

                This dataset is originally from the National Institute of Diabetes and Digestive and Kidney
            Diseases. The objective of the dataset is to diagnostically predict whether a patient has diabetes,
            based on certain diagnostic measurements included in the dataset. Several constraints were placed
            on the selection of these instances from a larger database. In particular, all patients here are females
            at least 21 years old of Pima Indian heritage.2
            From the data set in the (.csv) File We can find several variables, some of them are independent
            (several medical predictor variables) and only one target dependent variable (Outcome).

            """)
            st.image('assets/diabetes.jpg')

            st.markdown("""
            - **[*Heart*](https://www.kaggle.com/datasets/yasserh/heart-disease-dataset)  Disease Data Set.**
                This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. 
                In particular, the Cleveland database is the only one that has been used by ML researchers to
                this date. The "goal" field refers to the presence of heart disease in the patient. 
                It is integer-valued from 0 (no presence) to 4.

            **Objective:**
            - Understand the Dataset & cleanup (if required).
            - Build classification models to predict whether or not the patients have Heart Disease.
            - Also fine-tune the hyperparameters & compare the evaluation metrics of various classification algorithms.

            """)
            st.image('assets/Heart.png')



        # //////////////////////////////////////////// #
                    # Main Algorithm #
        # //////////////////////////////////////////// #


    # Diabetes Prediction Page
    if selected == 'Diabetes Prediction':
        # Page Title
        st.title('Diabetes Prediction using ML')

        # Getting the input data from the user
        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')

        with col2:
            Glucose = st.text_input('Glucose Level')

        with col3:
            BloodPressure = st.text_input('Blood Pressure value')

        with col1:
            SkinThickness = st.text_input('Skin Thickness value')

        with col2:
            Insulin = st.text_input('Insulin Level')

        with col3:
            BMI = st.text_input('BMI value')

        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

        with col2:
            Age = st.text_input('Age of the Person')

        # Code for Prediction
        diab_diagnosis = ''

        # Creating a button for Prediction
        if st.button('Diabetes Test Result'):
            diab_prediction = dia_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)


    # Heart Disease Prediction Page
    if selected == 'Heart Disease Prediction':
        # Page Title
        st.title('Heart Disease Prediction using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

        # Code for Prediction
        heart_diagnosis = ''

        # Creating a button for Prediction
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

        st.success(heart_diagnosis)


    # Parkinson's Prediction Page
    if selected == "Parkinsons Prediction":
        # Page Title
        st.title("Parkinson's Disease Prediction using ML")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')

        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')

        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')

        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')

        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

        with col1:
            RAP = st.text_input('MDVP:RAP')

        with col2:
            PPQ = st.text_input('MDVP:PPQ')

        with col3:
            DDP = st.text_input('Jitter:DDP')

        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')

        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')

        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')

        with col3:
            APQ = st.text_input('MDVP:APQ')

        with col4:
            DDA = st.text_input('Shimmer:DDA')

        with col5:
            NHR = st.text_input('NHR')

        with col1:
            HNR = st.text_input('HNR')

        with col2:
            RPDE = st.text_input('RPDE')

        with col3:
            DFA = st.text_input('DFA')

        with col4:
            spread1 = st.text_input('spread1')

        with col5:
            spread2 = st.text_input('spread2')

        with col1:
            D2 = st.text_input('D2')

        with col2:
            PPE = st.text_input('PPE')

        # Code for Prediction
        parkinsons_diagnosis = ''

        # Creating a button for Prediction
        if st.button("Parkinson's Test Result"):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)


        # //////////////////////////////////////////// #
                    # Setting Algorithm #
        # //////////////////////////////////////////// #

    if selected == 'Settings':
        head = st.write('# Profile :orange[Area] 😎')
        choise = st.selectbox("Login/Sign", ['Login', 'Sign Up'])
        if choise == 'Login':
            
            Lemail = st.text_input('Email Address', placeholder='laalbahadur@samplemail.com')
            Lpassword = st.text_input('Password', type='password', placeholder="It's Secrate 🤫")
            st.button("Login")

        else:
            fname = st.text_input("First Name", placeholder="Laal 😊")
            lname = st.text_input("Last Name", placeholder='Bahadur ')
            userName = st.text_input("User Name", placeholder='Laalu')
            Semail = st.text_input('Email Address', placeholder='laalbahadur@samplemail.com')
            Spassword = st.text_input('Password', type='password', placeholder="It's Secrate 🤫")
            rePassword = st.text_input('Re Enter Password', type='password',  placeholder="It's Secrate 🤫")
            
            if st.button("Sign Up"):
                user = auth.create_user(fname=fname, lname=lname, uid=userName, email=Semail, password=Spassword)
                st.success('Account Created Succesfully !')
                st.markdown('Please Login With your Email Id..')
                st.balloons()

        





        # //////////////////////////////////////////// #
                    # Footer Code #
        # //////////////////////////////////////////// #

        
def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
    # MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { bottom: 100px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1,
    )

    style_hr = styles(
        display="flex",
        margin=px(2, 2, "auto", "auto"),
        border_style="inset",
        border_width=px(1),
        color='pink'
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
        
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made ",
        " with ❤️ by ",
        link("https://github.com/Jerry4539", "@Jerry4539", color='orange'),

        # Code for auther Image
        # link('https://google.com', image('https://avatars.githubusercontent.com/u/91048755?v=4', width=px(15), height=px(15), margin=px(0,0,0,10))),
    ]
    layout(*myargs)


if __name__ == "__main__":
    app()
    footer()

        