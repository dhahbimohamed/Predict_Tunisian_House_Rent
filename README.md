# 🏠 Tunisian House Rent Price Predictor 🇹🇳

This project is a Machine Learning-powered web application that predicts the monthly rent price of houses in Tunisia based on features like surface area, number of rooms, bathrooms, and city. It is built with Streamlit and trained on real-world Tunisian housing data.

## 📊 Dataset
The dataset was scraped from a public source and cleaned manually. After cleaning and outlier removal, we retained:

📈 1,866 valid house entries  
🏙️ City: Mostly "Tunis" (add more if needed)  

### 🧹 Features used:
- surface (in m²)
- rooms
- bathrooms
- city (encoded)

## 🤖 ML Model Info
Trained with RandomForestRegressor and Linear Regression on selected features after:
- Removing outliers
- Filtering unrealistic entries (e.g., 0-room house at 1000 DT)
- Normalizing surface area range (50–300 m²)

## 👨‍💻 Author
**Mohamed Dhahbi** — CS student & aspiring ML engineer  
📧 mohameddhahbi56@gmail.com
