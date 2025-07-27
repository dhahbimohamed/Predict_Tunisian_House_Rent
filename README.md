# 🇹🇳 Tunisian House Rent Price Predictor 🏠

This is a Machine Learning-powered web app that predicts the **monthly rent price of houses in Tunisia**, based on surface area, number of rooms, number of bathrooms, and city.

Built by a Tunisian CS student to explore real-world ML from end to end — from messy data cleaning to model training to web app deployment.

---

## 🚀 Live App

👉 [Click here to open the live app]([https://your-app-url.streamlit.app](https://predicttunisianhouserent-sdxmw825dhufuvl9vayeqd.streamlit.app/))  

---

## 📦 Features

- 🔍 Predicts rent price based on:
  - Surface (m²)
  - Rooms
  - Bathrooms
  - City (one-hot encoded)
- 📊 Trained on real scraped data from Tayara.tn
- 🎯 Supports Tunisian cities like Tunis, Sfax, Sousse, etc.
- 🌐 Deployed with Streamlit Cloud for public use

---

## 📁 Dataset

The dataset was scraped from [tayara.tn](https://www.tayara.tn) and cleaned manually:
- Removed entries with missing or inconsistent values
- Filtered unreasonable outliers (e.g., 0 rooms with 1000 TND)
- Encoded categorical data (cities) using One-Hot Encoding

Final dataset: **~1900 rental houses**

---

## 🧠 Model

We tested:
- Linear Regression
- Random Forest Regressor (best model ✅)

Final performance (after filtering outliers):
- **Linear Regression** (best model ✅)
- **MAE**: ~244 TND
- **RMSE**: ~302 TND

Model trained on features:
```python
['surface', 'rooms', 'bathrooms', 'city_Tunis', 'city_Sfax', ...]

## 👨‍💻 Author
**Mohamed Dhahbi** — CS student & aspiring ML engineer  
📧 mohameddhahbi56@gmail.com
