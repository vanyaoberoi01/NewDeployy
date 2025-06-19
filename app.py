import streamlit as st
import joblib

# Load the trained model
model = joblib.load('home_price_model.joblib')

st.title("🏠 Home Price Prediction App")

st.markdown("Enter the details below to predict the price of a house:")

# Input fields
area = st.number_input("Area (in square feet)", min_value=100, max_value=10000, value=1500)

# Prediction
if st.button("Predict Price"):
    input_data = [[area]]
    prediction = model.predict(input_data)
    st.success(f"🏡 Estimated Home Price: ₹{prediction[0]:,.2f}")
