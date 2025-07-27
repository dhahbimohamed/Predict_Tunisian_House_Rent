import streamlit as st
import pickle
import pandas as pd

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load feature names
with open('model_features.pkl', 'rb') as f:
    feature_names = pickle.load(f)

# 🌍 Available cities (must match training)
available_cities = [col.replace('city_', '') for col in feature_names if col.startswith('city_')]

# 🧾 App Title
st.title("🏠 Tunisian House Rent Price Predictor")

# 📥 Input form
surface = st.number_input("Surface (m²)", min_value=10, max_value=500, value=100)
rooms = st.number_input("Number of rooms", min_value=0, max_value=10, value=2)
bathrooms = st.number_input("Number of bathrooms", min_value=0, max_value=5, value=1)
city = st.selectbox("City", available_cities)

# 🔍 Predict button
if st.button("Predict"):
    # One-hot encode the city
    city_encoded = {f'city_{c}': 0 for c in available_cities}
    city_encoded[f'city_{city}'] = 1

    # Construct input
    input_data = {
        'surface': surface,
        'rooms': rooms,
        'bathrooms': bathrooms,
        **city_encoded
    }

    # Align with training columns
    X = pd.DataFrame([input_data])
    X = X.reindex(columns=feature_names, fill_value=0)

    # Predict
    prediction = model.predict(X)[0]
    st.success(f"💰 Estimated Rent Price: {int(prediction)} TND/month")
