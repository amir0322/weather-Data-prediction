import streamlit as st
import pickle
import numpy as np

# Load model
with open("svm_model.pkl", "rb") as file:
    model = pickle.load(file) 

st.title("🌧️ Rain Prediction App")

st.write("Enter weather conditions to predict if it will rain or not.")

# Example Inputs - replace with your real features
humidity = st.number_input("Humidity (%)", 0, 100, 50)
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0, value=10.0)
Cloud_Cover = st.number_input("Cloud Cover (%)", 0, 100, 50)
Pressure = st.number_input("Pressure (hPa)", min_value=900, max_value=1100, value=1013)
# Add more input fields as per your model's features

if st.button("Predict"):
    # Feature vector (order must match model input)
    input_data = np.array([[humidity, temperature, wind_speed, Cloud_Cover, Pressure]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🌧️ It will rain!")
    else:
        st.info("☀️ No rain expected.")
