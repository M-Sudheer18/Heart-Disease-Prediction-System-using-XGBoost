# ❤️ Heart Disease Prediction System using XGBoost

## 📌 Project Overview

The Heart Disease Prediction System is a Machine Learning-powered healthcare application that predicts whether a patient is at high risk or low risk of heart disease based on clinical and medical attributes.

The project uses the XGBoost (Extreme Gradient Boosting) algorithm, which was selected after evaluating multiple machine learning models such as:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* Bagging Classifier
* Other Ensemble Techniques

The final trained XGBoost model is deployed through a Streamlit web application, allowing users to enter patient information and instantly receive a prediction.

---

# 🎯 Problem Statement

Heart disease is one of the leading causes of death worldwide. Early detection can significantly improve treatment outcomes and reduce mortality rates.

This project aims to:

* Analyze patient health records.
* Identify patterns associated with heart disease.
* Predict disease risk using Machine Learning.
* Provide a simple and user-friendly interface for healthcare professionals and patients.

---

# 🚀 Features

### ✅ User-Friendly Interface

Built with Streamlit for easy interaction.

### ✅ Real-Time Prediction

Instantly predicts heart disease risk after entering patient details.

### ✅ Machine Learning Powered

Uses XGBoost, one of the most powerful gradient boosting algorithms.

### ✅ Cloud-Based Model Loading

Model is automatically downloaded from Hugging Face Hub.

### ✅ Medical Parameter Support

Accepts 13 clinical attributes commonly used in cardiovascular diagnosis.

### ✅ Lightweight Deployment

Can be deployed on:

* Hugging Face Spaces
* Streamlit Community Cloud
* AWS EC2
* Azure
* Google Cloud Platform

---

# 📊 Dataset Information

The project uses the Heart Disease Dataset containing patient medical information.

### Dataset Features

| Feature  | Description                              |
| -------- | ---------------------------------------- |
| age      | Age of patient                           |
| sex      | Gender                                   |
| cp       | Chest Pain Type                          |
| trestbps | Resting Blood Pressure                   |
| chol     | Serum Cholesterol                        |
| fbs      | Fasting Blood Sugar                      |
| restecg  | Resting ECG Results                      |
| thalach  | Maximum Heart Rate Achieved              |
| exang    | Exercise Induced Angina                  |
| oldpeak  | ST Depression                            |
| slope    | Slope of Peak Exercise ST Segment        |
| ca       | Number of Major Vessels                  |
| thal     | Thalassemia Type                         |
| target   | Heart Disease Presence (Target Variable) |

---

# 🏗️ Project Architecture

```text
                 ┌───────────────────┐
                 │   User Interface  │
                 │    (Streamlit)    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ User Inputs Data  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Data Formatting   │
                 │  Pandas DataFrame │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ XGBoost Model     │
                 │ Prediction Engine │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Prediction Result │
                 │ High / Low Risk   │
                 └───────────────────┘
```

---

# ☁️ Infrastructure Architecture

```text
                        ┌─────────────────────┐
                        │      End User       │
                        └──────────┬──────────┘
                                   │
                                   ▼
                    ┌──────────────────────────┐
                    │ Streamlit Web Application│
                    └──────────┬───────────────┘
                               │
                               ▼
                 ┌─────────────────────────────┐
                 │ Hugging Face Hub Repository │
                 │ heart_disease_xgb.pkl       │
                 └──────────┬──────────────────┘
                            │
                            ▼
                 ┌─────────────────────────────┐
                 │ XGBoost Prediction Model    │
                 └──────────┬──────────────────┘
                            │
                            ▼
                 ┌─────────────────────────────┐
                 │ Prediction Output           │
                 │ High Risk / Low Risk        │
                 └─────────────────────────────┘
```

---

# 🧠 Machine Learning Workflow

## Step 1: Data Collection

Patient health records are collected from the Heart Disease Dataset.

## Step 2: Data Preprocessing

Performed preprocessing tasks such as:

* Missing value checking
* Data cleaning
* Zero-value handling
* Feature preparation

## Step 3: Exploratory Data Analysis

Visualizations were created to understand:

* Disease distribution
* Age impact
* Cholesterol trends
* Heart rate relationships

## Step 4: Model Training

Multiple machine learning algorithms were trained:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* Bagging Classifier

## Step 5: Model Evaluation

Models were compared using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

## Step 6: Best Model Selection

XGBoost achieved the best overall performance and was selected for deployment.

## Step 7: Deployment

The trained model was exported as:

```python
heart_disease_xgb.pkl
```

and deployed using Streamlit.

---

# 🔧 Technologies Used

## Programming Language

* Python 3.x

## Machine Learning Libraries

* Scikit-Learn
* XGBoost
* NumPy
* Pandas

## Visualization Libraries

* Matplotlib
* Seaborn

## Deployment

* Streamlit
* Hugging Face Hub

---

# 📦 Installation

Clone Repository

```bash
git clone https://github.com/yourusername/heart-disease-prediction.git

cd heart-disease-prediction
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Application

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```text
Heart-Disease-Prediction/
│
├── app.py
├── heart_disease_xgb.pkl
├── heart.csv
├── notebook.ipynb
├── requirements.txt
├── README.md
│
└── assets/
```

---

# 🎯 Input Parameters

The application accepts:

```text
Age
Sex
Chest Pain Type
Resting Blood Pressure
Cholesterol
Fasting Blood Sugar
Resting ECG
Maximum Heart Rate
Exercise Induced Angina
Old Peak
Slope
CA
Thal
```

---

# 📈 Prediction Output

### High Risk

```text
⚠️ High Risk of Heart Disease
```

### Low Risk

```text
✅ Low Risk of Heart Disease
```

---

# 🔒 Future Enhancements

* Probability Score Prediction
* Risk Percentage Visualization
* Patient Report Generation
* Doctor Dashboard
* Historical Prediction Tracking
* Multi-Patient Batch Prediction
* Cloud Database Integration
* Mobile Application Support

---

# 🌟 Business Impact

* Early disease detection
* Reduced healthcare costs
* Improved patient monitoring
* Faster clinical decision-making
* Increased diagnostic efficiency

---

# 👨‍💻 Author

Sudheer Muthyala

B.Tech (Electronics & Communication Engineering)

Machine Learning & Full Stack Developer

GitHub: https://github.com/Sudheer17

---

# 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
