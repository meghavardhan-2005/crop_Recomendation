
import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load('crop_model.pkl')
encoder = joblib.load('label_encoder.pkl')

# Title
st.title("🌾 AI Crop Recommendation Agent")

st.write("Enter soil and weather conditions")

# User inputs
N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorus (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)

temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("pH Value")
rainfall = st.number_input("Rainfall (mm)")

# Predict button
if st.button("Recommend Crop"):

    input_data = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=[
            'N',
            'P',
            'K',
            'temperature',
            'humidity',
            'ph',
            'rainfall'
        ]
    )

    prediction = model.predict(input_data)

    crop = encoder.inverse_transform(prediction)

    st.success(f"Recommended Crop: {crop[0]}")

    # Fertilizer suggestions
    if crop[0] == "rice":
        st.info("Use nitrogen-rich fertilizers.")

    elif crop[0] == "banana":
        st.info("Ensure adequate potassium supply.")

    elif crop[0] == "cotton":
        st.info("Use balanced NPK fertilizers.")

    # Irrigation advice
    if rainfall < 100:
        st.warning("Irrigation is recommended.")
    else:
        st.success("Natural rainfall is sufficient.")
