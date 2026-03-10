import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go

# Load trained model
model = joblib.load("heart_disease_model.pkl")

st.set_page_config(
    page_title="Heart Disease AI",
    page_icon="❤️"
)

st.title("❤️ Heart Disease Risk Analyzer")
st.caption("AI-powered clinical decision support system")

st.divider()

st.subheader("Patient Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 40)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", [0,1,2,3])
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
    chol = st.number_input("Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120", [0,1])

with col2:
    restecg = st.selectbox("Rest ECG", [0,1,2])
    thalach = st.number_input("Max Heart Rate", 60, 220, 150)
    exang = st.selectbox("Exercise Induced Angina", [0,1])
    oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0)
    slope = st.selectbox("Slope", [0,1,2])
    ca = st.selectbox("Major Vessels", [0,1,2,3])

sex = 1 if sex == "Male" else 0

# Create feature array
features = np.array([[age, sex, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak,
                      slope, ca]])

st.divider()

if st.button("Analyze Heart Disease Risk"):

    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1] * 100

    st.subheader("AI Prediction Result")

    st.metric("Risk Probability", f"{probability:.2f}%")

    # ---------------- Risk Gauge ----------------
    color = "green" if probability < 30 else "orange" if probability < 60 else "red"
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability,
        title={'text': "Heart Disease Risk %"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': color},
            'steps': [
                {'range': [0,30], 'color': "green"},
                {'range': [30,60], 'color': "yellow"},
                {'range': [60,100], 'color': "red"}
            ]
        }
    ))

    st.plotly_chart(gauge, use_container_width=True)

    # ---------------- Probability Bar Chart ----------------
    healthy_prob = 100 - probability

    bar_chart = go.Figure(data=[
        go.Bar(name="Healthy", x=["Prediction"], y=[healthy_prob]),
        go.Bar(name="Heart Disease Risk", x=["Prediction"], y=[probability])
    ])

    bar_chart.update_layout(title="Prediction Confidence")

    st.plotly_chart(bar_chart, use_container_width=True)

    # ---------------- Result Text ----------------
    if prediction[0] == 1:
        st.error("⚠ High Risk of Heart Disease. Please consult a doctor.")
    else:
        st.success("✅ Heart condition appears normal.")

    # ---------------- Medical Interpretation ----------------
    st.divider()

    st.subheader("Medical Interpretation")

    if probability < 30:
        st.info("Low cardiovascular risk detected. Maintain healthy lifestyle and regular checkups.")

    elif probability < 60:
        st.warning("Moderate cardiovascular risk detected. Consider medical consultation and lifestyle improvements.")

    else:
        st.error("High cardiovascular risk detected. Immediate medical consultation recommended.")

    # ---------------- Disclaimer ----------------
    st.caption("⚠ Disclaimer: This AI tool estimates heart disease risk and is not a medical diagnosis.")