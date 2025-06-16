
import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open("model.pkl", "rb"))

st.title("📚 Student Performance Predictor")
st.write("Enter student details below to predict final exam score.")

# Input form
hours = st.slider("Hours Studied per Day", 0.0, 12.0, 2.0)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous_score = st.slider("Previous Exam Score (%)", 0, 100, 60)

if st.button("Predict Score"):
    features = np.array([[hours, attendance, previous_score]])
    prediction = model.predict(features)
    st.success(f"📈 Predicted Final Score: {prediction[0]:.2f}%")
