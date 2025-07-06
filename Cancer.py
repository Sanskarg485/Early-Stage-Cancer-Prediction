# ✅ Step 1: Install required packages


# ✅ Step 2: Copy your uploaded model to correct filename
import shutil
shutil.copy(r"C:\Users\Sanskar Gupta\OneDrive\Desktop\Programimg\python.py\java\Cancer_prediction.pkl", "knn_model.pkl")



# ✅ Step 3: Create the Streamlit app code
app_code = """
import streamlit as st
import pickle
import numpy as np
import os

st.set_page_config(page_title="Cancer Prediction APP", layout="centered")

# Load the model
model_path = "knn_model.pkl"
if not os.path.exists(model_path):
    st.error("Model file not found: knn_model.pkl")
    st.stop()

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

st.title("🔍 Early Stage Cancer Prediction Prediction App")
st.write("Enter the input features (23 total) below:")

# Set number of features
n_features = 23
features = []

# Take 23 inputs from user
for i in range(n_features):
    val = st.number_input(f"Feature {i+1}", key=f"feature_{i}")
    features.append(val)

if st.button("Predict"):
    try:
        input_data = np.array([features])
        prediction = model.predict(input_data)
        if prediction[0] ==0:
          st.success(f"🎯 Predicted Class: class 0 - 'Non-Cancerous' ")
        else:
          st.info(f"🎯 Predicted Class: class 1 - 'Cancerous' ")
    except Exception as e:
        st.error(f"Prediction Error: {e}")
"""

# ✅ Step 4: Save the app to knn_app.py
with open("app.py", "w", encoding="utf-8") as f:
    f.write(app_code)


# ✅ Step 5: Start ngrok and run the Streamlit app
from pyngrok import ngrok
from IPython import get_ipython # Import get_ipython for shell commands

# Disconnect all existing ngrok tunnels
ngrok.kill() #Kill any existing tunnel under this session

# Set the authentication token BEFORE connecting
ngrok.set_auth_token("2waKO9TRS14m9CsKLqMoybFbPyp_aVrG77aV3XCuBmmeCQtr")

# This tries to connect and if fails, it kills all and then connects again.
try:
    tunnel = ngrok.connect(8501)
except Exception as e:
    print(f"An error occurred: {e}. Attempting to kill all sessions and reconnect.")
    get_ipython().system('pkill -f ngrok #Kill all ngrok instances') # Use get_ipython().system() for shell commands
    tunnel = ngrok.connect(8501)


print("🌐 Streamlit app is live at:", tunnel.public_url)

# ✅ Step 6: Launch the app
get_ipython().system('streamlit run knn_app.py &>/dev/null &') # Use get_ipython().system() for shell commands