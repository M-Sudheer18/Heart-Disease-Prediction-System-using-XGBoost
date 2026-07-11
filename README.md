


<div align="center">

# ❤️ Heart Disease Prediction System

### Early Detection of Heart Disease using Machine Learning & XGBoost

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![XGBoost](https://img.shields.io/badge/XGBoost-Machine%20Learning-orange?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-yellow?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-blue?style=for-the-badge&logo=numpy)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Model%20Hub-yellow?style=for-the-badge&logo=huggingface)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### 🌐 Live Demo

## 🚀 https://heart-disease-prediction-xgb.streamlit.app/

Predict the risk of heart disease instantly using a Machine Learning model trained with **Extreme Gradient Boosting (XGBoost)**.

</div>

---

# 📖 Overview

Heart disease remains one of the leading causes of death worldwide. Early diagnosis can significantly reduce mortality by enabling timely medical intervention.

This project presents an **end-to-end Machine Learning application** that predicts whether a patient is at **high risk** or **low risk** of heart disease using clinical parameters.

After evaluating multiple machine learning algorithms, **XGBoost** achieved the highest predictive performance and was selected for deployment.

The application is deployed using **Streamlit Community Cloud**, while the trained model is securely hosted on **Hugging Face Hub**.

---

# ✨ Key Features

- ❤️ Heart Disease Risk Prediction
- ⚡ Real-Time Prediction
- 🤖 XGBoost Machine Learning Model
- ☁️ Cloud-Based Model Loading from Hugging Face
- 📊 Interactive Streamlit Interface
- 📈 High Prediction Accuracy
- 🚀 One-Click Deployment Ready
- 🔒 Lightweight & Scalable Architecture

---

# 🌐 Live Application

## 🚀 Try it Here

### https://heart-disease-prediction-xgb.streamlit.app/

---

# 📂 Project Structure

```text
Heart-Disease-Prediction-System/
│
├── app.py
├── notebook.ipynb
├── heart.csv
├── requirements.txt
├── README.md
│
├── models/
│   └── heart_disease_xgb.pkl
│
└── assets/
    ├── screenshots/
    └── images/
```

---

# 🏗️ System Architecture

```text
                     Patient Information
                              │
                              ▼
                  Streamlit User Interface
                              │
                              ▼
                 Data Validation & Formatting
                              │
                              ▼
             Hugging Face Model Repository
                              │
                              ▼
             Trained XGBoost Prediction Model
                              │
                              ▼
                 Risk Prediction Engine
                              │
                              ▼
          ❤️ High Risk / ✅ Low Risk Result
```

---

# ☁️ Deployment Architecture

```text
                    ┌─────────────────────┐
                    │      End User       │
                    └──────────┬──────────┘
                               │
                               ▼
                 Streamlit Community Cloud
                               │
                               ▼
                Hugging Face Model Repository
                               │
                               ▼
                   XGBoost Prediction Model
                               │
                               ▼
                      Prediction Result
```

---

# 🚀 Machine Learning Workflow

```text
                Heart Disease Dataset
                         │
                         ▼
                 Data Cleaning
                         │
                         ▼
             Exploratory Data Analysis
                         │
                         ▼
              Feature Engineering
                         │
                         ▼
              Train-Test Split
                         │
                         ▼
      Multiple Model Training
(Logistic, Decision Tree, Random Forest,
      Bagging, XGBoost)
                         │
                         ▼
             Model Performance Comparison
                         │
                         ▼
          Best Model Selection (XGBoost)
                         │
                         ▼
         Save Trained Model (.pkl)
                         │
                         ▼
        Deploy with Streamlit Cloud
```

---

# 📊 Dataset Information

The project uses the **Heart Disease Dataset**, which contains clinical information about patients used to predict cardiovascular disease.

## Input Features

| Feature | Description |
|----------|-------------|
| Age | Age of Patient |
| Sex | Male / Female |
| Chest Pain Type | Chest Pain Category |
| Resting Blood Pressure | Blood Pressure |
| Cholesterol | Serum Cholesterol |
| Fasting Blood Sugar | Blood Sugar Level |
| Resting ECG | ECG Results |
| Maximum Heart Rate | Heart Rate Achieved |
| Exercise Induced Angina | Chest Pain During Exercise |
| Old Peak | ST Depression |
| Slope | ST Segment Slope |
| CA | Major Blood Vessels |
| Thal | Thalassemia |

### Target Variable

| Value | Meaning |
|-------|---------|
| **0** | Low Risk |
| **1** | High Risk |

---

# 📊 Exploratory Data Analysis

The project includes detailed EDA covering:

- 📈 Heart Disease Distribution
- 👨 Age-wise Analysis
- ❤️ Cholesterol Distribution
- 📊 Blood Pressure Analysis
- 📉 Correlation Heatmap
- 📦 Outlier Detection
- 📋 Feature Relationships

---

# 🤖 Machine Learning Models

Several machine learning algorithms were trained and compared.

| Model | Purpose |
|--------|----------|
| Logistic Regression | Baseline Model |
| Decision Tree | Tree-Based Learning |
| Random Forest | Ensemble Learning |
| Bagging Classifier | Bootstrap Ensemble |
| **XGBoost** | Final Selected Model ✅ |

---

# 📈 Model Evaluation

The models were evaluated using the following metrics:

| Metric | Description |
|---------|-------------|
| Accuracy | Overall Prediction Accuracy |
| Precision | Positive Prediction Quality |
| Recall | Disease Detection Capability |
| F1 Score | Precision-Recall Balance |
| ROC-AUC Score | Classification Performance |

> 🏆 **XGBoost achieved the best overall performance and was selected for deployment.**

---

# 🧠 Why XGBoost?

XGBoost was selected because it provides:

- High prediction accuracy
- Excellent generalization
- Faster training
- Built-in regularization
- Robust handling of tabular healthcare data
- Reduced overfitting compared to traditional tree models

---

# 💻 Technologies Used

| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| Machine Learning | XGBoost, Scikit-Learn |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit |
| Model Hosting | Hugging Face Hub |

---

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/M-Sudheer18/Heart-Disease-Prediction-System-using-XGBoost.git
```

Move into the project directory

```bash
cd Heart-Disease-Prediction-System-using-XGBoost
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Locally

```bash
streamlit run app.py
```

---

# ☁️ Deployment

The project is successfully deployed using **Streamlit Community Cloud**.

### 🌐 Live Demo

https://heart-disease-prediction-xgb.streamlit.app/

The trained XGBoost model is hosted securely on **Hugging Face Hub** and downloaded automatically during application startup.

---

# 📷 Application Preview

> Add screenshots here

Suggested screenshots:

- ❤️ Home Page
- 📝 Input Form
- ⚠️ High Risk Prediction
- ✅ Low Risk Prediction
- 📊 EDA Charts
- 📉 Correlation Heatmap

---

# 🎯 Input Parameters

The application accepts the following clinical parameters:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression (Old Peak)
- Slope
- Number of Major Vessels (CA)
- Thalassemia

---

# 📈 Prediction Output

### ⚠️ High Risk

```text
⚠️ High Risk of Heart Disease
```

### ✅ Low Risk

```text
✅ Low Risk of Heart Disease
```

---

# 🌍 Business Impact

This solution can assist healthcare professionals by:

- ❤️ Early Disease Detection
- 📊 Supporting Clinical Decisions
- ⏱️ Reducing Diagnosis Time
- 💰 Lowering Healthcare Costs
- 🏥 Improving Patient Monitoring
- 📈 Enhancing Preventive Healthcare

---

# 🚀 Future Enhancements

- 📊 Prediction Probability Score
- 📈 Risk Percentage Visualization
- 🩺 Doctor Dashboard
- 📄 PDF Medical Report Generation
- 👥 Multi-Patient Batch Prediction
- 🗄️ Cloud Database Integration
- 📱 Mobile Application
- 🤖 Explainable AI using SHAP
- 🔐 User Authentication
- 🌐 REST API with FastAPI

---

# 👨‍💻 Author

## **Sudheer Muthyala**

**B.Tech – Electronics and Communication Engineering**

**Aspiring Data Scientist | Machine Learning Engineer | Deep Learning Enthusiast | Python Developer**

### 🔗 Connect with Me

- **GitHub:** https://github.com/M-Sudheer18
- **LinkedIn:** https://www.linkedin.com/in/sudheer-muthyala-317180268

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork this repository

💬 Share your feedback

🤝 Contributions are always welcome!

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for educational and research purposes.

---

<div align="center">

# ❤️ If you found this project helpful, don't forget to ⭐ Star the Repository!

### Made with ❤️ by **Sudheer Muthyala**

</div>
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
