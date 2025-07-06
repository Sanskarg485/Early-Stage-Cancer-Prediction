# app.py
import streamlit as st
import pickle
import numpy as np
import os

st.set_page_config(page_title="Cancer Prediction APP", layout="centered")

# Load the model
model_path = "Cancer_prediction.pkl"
if not os.path.exists(model_path):
    st.error("Model file not found: Cancer_prediction.pkl")
    st.stop()

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("🔬 Early Stage Cancer Prediction App")
st.write("Please enter the input values below (23 features):")

n_features = 23
features = []

for i in range(n_features):
    val = st.number_input(f"Feature {i+1}", key=f"feature_{i}")
    features.append(val)

if st.button("Predict"):
    try:
        input_data = np.array([features])
        prediction = model.predict(input_data)

        if prediction[0] == 0:
            st.success("🟢 Prediction: Non-Cancerous (Class 0)")
        else:
            st.warning("🔴 Prediction: Cancerous (Class 1)")
    except Exception as e:
        st.error(f"Prediction error: {e}")
