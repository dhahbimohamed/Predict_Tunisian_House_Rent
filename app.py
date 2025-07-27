import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and city columns
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('city_columns.pkl', 'rb') as f:
    city_columns = pickle.load(f)

st.set_page_config(page_title="🏡 Tunisian House Rent Price Predictor")

st.title("🇹🇳 Tunisian Rent Price Predictor")
st.markdown("Predict rent prices in Tunisia based on house features.")

# --- Input fields ---
surface = st.slider("Surface (m²)", 50, 300, 100)
rooms = st.slider("Number of rooms", 0, 4, 2)
bathrooms = st.slider("Number of bathrooms", 0, 2, 1)
city = st.selectbox("City", sorted([col.replace("city_", "") for col in city_columns]))

# --- Prepare input ---
def preprocess_input(surface, rooms, bathrooms, city, city_columns):
    input_data = {
        'surface': surface,
        'rooms': rooms,
        'bathrooms': bathrooms
    }

    for col in city_columns:
        input_data[col] = 1 if col == f"city_{city}" else 0

    return pd.DataFrame([input_data])

# --- Prediction ---
if st.button("Predict"):
    input_df = preprocess_input(surface, rooms, bathrooms, city, city_columns)
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Rent: {int(prediction)} TND/month")
