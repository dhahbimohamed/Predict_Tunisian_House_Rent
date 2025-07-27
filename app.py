import streamlit as st
import joblib
import pandas as pd

# Load model and column structure
model = joblib.load('model.joblib')
city_columns = joblib.load('city_columns.joblib')

# App title
st.title("🏠 Tunisian Rent Price Predictor")

# Input fields
surface = st.number_input("Surface (m²)", min_value=10, max_value=300, value=100)
rooms = st.number_input("Number of rooms", min_value=0, max_value=10, value=2)
bathrooms = st.number_input("Number of bathrooms", min_value=0, max_value=5, value=1)
city = st.selectbox("City", [col.replace("city_", "") for col in city_columns if col.startswith("city_")])

# Predict button
if st.button("Predict Price"):
    # Build input vector
    input_data = {
        'surface': surface,
        'rooms': rooms,
        'bathrooms': bathrooms
    }
    for col in city_columns:
        input_data[col] = 1 if col == f"city_{city}" else 0

    X = pd.DataFrame([input_data])
    prediction = model.predict(X)[0]
    st.success(f"Estimated rent price: {int(prediction)} TND")
