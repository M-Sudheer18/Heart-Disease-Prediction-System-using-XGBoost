import streamlit as st
import pandas as pd
import joblib

# Inputs 
# --> age
# --> sex
# --> cp
# --> trestbps
# --> chol
# --> fbs
# --> restecg
# --> thalach
# --> exang
# --> oldpeak
# --> slope
# --> ca
# --> thal


# Load Model 
from huggingface_hub import hf_hub_download
import joblib

@st.cache_resource
def load_model():

    model_path = hf_hub_download(
        repo_id="Sudheer17/Heart_Disease_XGB_Model",
        filename="heart_disease_xgb.pkl"
    )

    model = joblib.load(model_path)

    return model

model = load_model()



st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Prediction")
st.write("Enter patient details below to predict heart disease risk.")


# Input Fields

# Age 
age = st.number_input("Age", min_value=1, max_value=90, value=50)


# Gender
gender = st.selectbox(
    "Sex",
    options=[0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

# Cp
cp = st.selectbox(
    "Chest Pain Type (cp)",
    options=[0, 1, 2, 3]
)

trestbps = st.number_input(
    "Resting Blood Pressure (trestbps)",
    min_value=50,
    max_value=250,
    value=120
)

chol = st.number_input(
    "Cholesterol (chol)",
    min_value=120,
    max_value=600,
    value=250
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl (fbs)",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

restecg = st.selectbox(
    "Resting ECG Results (restecg)",
    options=[0, 1, 2]
)

thalach = st.number_input(
    "Maximum Heart Rate Achieved (thalach)",
    min_value=50,
    max_value=250,
    value=150
)

exang = st.selectbox(
    "Exercise Induced Angina (exang)",
    options=[0, 1],
    format_func=lambda x: "No" if x == 0 else "Yes"
)

oldpeak = st.number_input(
    "ST Depression (oldpeak)",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

slope = st.selectbox(
    "Slope",
    options=[0, 1, 2]
)

ca = st.selectbox(
    "Number of Major Vessels (ca)",
    options=[0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Thal",
    options=[0, 1, 2, 3]
)


if st.button("Predict"):

    input_data = pd.DataFrame({
        'age': [age],
        'sex': [gender],
        'cp': [cp],
        'trestbps': [trestbps],
        'chol': [chol],
        'fbs': [fbs],
        'restecg': [restecg],
        'thalach': [thalach],
        'exang': [exang],
        'oldpeak': [oldpeak],
        'slope': [slope],
        'ca': [ca],
        'thal': [thal]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")












