import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load Model
model = joblib.load("bitcoin_price_model.pkl")

# Page Configuration
st.set_page_config(page_title="Bitcoin Price Prediction", layout="centered", page_icon="💰")
st.title("📊 Bitcoin Price Prediction App")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.info("This app predicts the **Bitcoin Closing Price** based on historical market data.")
st.sidebar.markdown("---")
st.sidebar.write("### About Project")
st.sidebar.write("- Machine Learning Project")
st.sidebar.write("- Time Series Forecasting")
st.sidebar.write("- Built with **Streamlit** and **Random Forest Regressor**")

# Main Content
st.markdown("## Welcome to Bitcoin Price Predictor 💰")
st.markdown(
    "This app predicts the **Bitcoin Closing Price** based on the provided inputs such as Open Price, High Price, Low Price, and Volume.")
st.markdown("---")

# Collecting User Inputs
st.subheader("Enter the Market Parameters")
open_price = st.number_input("🔑 Open Price ($)", min_value=0.0, format="%.2f")
high_price = st.number_input("📈 High Price ($)", min_value=0.0, format="%.2f")
low_price = st.number_input("📉 Low Price ($)", min_value=0.0, format="%.2f")
volume = st.number_input("🔄 Volume", min_value=0.0, format="%.2f")

# Prediction Button
if st.button("Predict Price 💪"):
    if open_price == 0 or high_price == 0 or low_price == 0 or volume == 0:
        st.warning("Please enter all values before predicting.")
    else:
        data = [[open_price, high_price, low_price, volume]]
        prediction = model.predict(data)
        st.success(f"✅ Predicted Closing Price: **${round(prediction[0], 2)}**")

# Footer
st.markdown("---")
st.markdown(
    "Developed by **Vaibhav** | Data Science Intern 💻")
st.markdown("💡 Powered by Streamlit | Random Forest Regressor | Joblib")