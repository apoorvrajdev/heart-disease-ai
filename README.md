# ❤️ Heart Disease Risk Prediction AI

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Healthcare AI](https://img.shields.io/badge/Healthcare-AI-red)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

This project builds an **AI-powered clinical decision support system** that predicts the **risk of heart disease** using machine learning.

The system analyzes medical parameters such as:

- Age
- Chest Pain Type
- Cholesterol
- Blood Pressure
- ECG Results
- Maximum Heart Rate
- ST Depression
- Major Vessels

and predicts the **probability of heart disease risk**.

The model is deployed as an **interactive Streamlit web application** where users can input patient data and instantly receive a prediction.

---

# 🚀 Live Demo

Run the AI prediction app locally: https://heart-disease-clinical-ai.streamlit.app

Users can input medical parameters and instantly receive:

- Risk probability
- Visual risk meter
- Medical interpretation

---

# 🧠 AI Prediction Interface

### Patient Input Interface

![Main Interface](results/high-risk-patient-main-page.png)

The application collects patient information including age, cholesterol level, blood pressure, ECG results, and other cardiovascular indicators.

---

# 🔬 Prediction Result

### AI Risk Prediction

![Prediction Result](results/high-risk-patient-prediction-result.png)

The AI model calculates a **heart disease risk probability** and displays the result using a visual **risk gauge meter**.

---

# 🏥 Medical Interpretation

![Medical Interpretation](results/high-risk-patient-medical-interpretation.png)

The system provides a **clinical interpretation** of the prediction to assist decision making.

⚠️ **Disclaimer:**  
This AI system estimates risk and **does not replace professional medical diagnosis.**

---

# 📊 Model Performance

### Accuracy of Machine Learning Models

![Model Accuracy](<img width="1115" height="576" alt="Model accuracy" src="https://github.com/user-attachments/assets/7ca75759-b053-45e1-bb6a-f543395fc680" />


| Model | Accuracy |
|------|------|
| KNN | 84.96% |
| Random Forest | 88.02% |
| SVM | 87.47% |

Random Forest performed the best among the individual models.

---

# 🤖 Ensemble & Boosted Models

![Ensemble Models](<img width="1061" height="592" alt="boosted model accuracy" src="https://github.com/user-attachments/assets/4b70e2e6-04c3-419c-bdcc-8084d03a6f34" />


| Model | Accuracy |
|------|------|
| Voting Ensemble | 86.35% |
| Boosted Model | **89.42%** |

Boosted models achieved the **highest accuracy**.

---

# 📈 K-Fold Cross Validation

![Cross Validation](<img width="1076" height="582" alt="cross validation " src="https://github.com/user-attachments/assets/1d0e6aa5-9ea3-4329-b3b1-31f17e91902c" />


To ensure model stability and reduce overfitting, **5-fold cross validation** was used.

Metrics evaluated:

- Accuracy
- Precision
- AUC Score

The results show **consistently high performance across folds**, indicating strong generalization capability.

---

# 📂 Dataset

The dataset used is the **UCI Heart Disease Dataset**, a well-known dataset used for cardiovascular risk prediction research.

Dataset characteristics:

- Number of samples: **303**
- Number of features: **14**
- Target variable: **Heart disease presence**

Each row represents a patient with various medical attributes.

---

# ⚙️ Machine Learning Pipeline

The project follows a complete machine learning workflow:

1. Data loading using Pandas
2. Exploratory Data Analysis (EDA)
3. Data visualization using Seaborn and Matplotlib
4. Feature scaling using StandardScaler
5. Train-test split
6. Model training
7. Model comparison
8. Ensemble modeling
9. Cross validation
10. Web application deployment using Streamlit

---

# 🧰 Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

---

# 📁 Project Structure
```
heart-disease-prediction
│
├── data
│   └── heart.csv
│
├── result
│   ├── Healthy patient
│   │   ├── Healthy patient_MAIN PAGE.png
│   │   ├── Healthy patient_MEDICAL INTERPRETATON.png
│   │   └── Healthy patient_PREDICTION RESULT.png
│   │
│   └── High risk patient
│       ├── High Risk patient_MAIN PAGE.png
│       ├── High Risk patient_MEDICAL INTERPRETATON.png
│       └── High Risk patient_PREDICTION RESULT.png
│
├── app.py                       # Streamlit web application
├── heart_disease_model.pkl      # Trained machine learning model
├── heart_disease_training.ipynb # Model training notebook
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation

```
## Installation

### Clone the repository

```
git clone (https://github.com/apoorvrajdev/heart-disease-ai.git)
```
### Install dependencies

```
pip install -r requirements.txt
```

### Run the application

```
streamlit run app.py
```

---

# 🚀 Future Improvements

Possible enhancements for the project:

- Use advanced models such as **XGBoost and LightGBM**
- Add **Explainable AI (SHAP)** for model transparency
- Deploy the system on **cloud infrastructure**
- Integrate with **electronic health record systems**
- Improve UI with **advanced medical visualization**

---

# 👨‍💻 Author

**Apoorv Raj**

Machine Learning & AI Engineer

---

⭐ If you found this project useful, consider giving it a **star** on GitHub.
