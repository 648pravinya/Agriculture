import streamlit as st
import os
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# -----------------------------------
# Agriculture Intelligence Platform
# Full Industry-Level Project
# -----------------------------------

# Features:
# 1. Crop Yield Prediction
# 2. Fertilizer Recommendation
# 3. Weather Insights
# 4. Soil Analysis
# 5. Dashboard Analytics
# 6. Dataset Visualization
#
# Run Command:
# streamlit run app.py

# -----------------------------------
# Sample Agriculture Dataset
# -----------------------------------

sample_data = {
    'rainfall': [120, 200, 150, 300, 250, 180, 100, 220, 270, 130, 160, 210],
    'temperature': [28, 30, 27, 32, 31, 29, 26, 33, 34, 25, 28, 30],
    'humidity': [70, 80, 65, 90, 85, 75, 60, 88, 92, 58, 72, 81],
    'soil_ph': [6.5, 7.0, 6.8, 5.9, 6.2, 6.7, 7.1, 6.0, 5.8, 7.2, 6.4, 6.9],
    'yield': [3.5, 4.2, 3.8, 5.0, 4.7, 4.0, 3.2, 5.1, 5.3, 3.0, 3.9, 4.4]
}

df = pd.DataFrame(sample_data)

# -----------------------------------
# Train Machine Learning Model
# -----------------------------------
X = df[['rainfall', 'temperature', 'humidity', 'soil_ph']]
y = df['yield']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

# -----------------------------------
# Fertilizer Recommendation Function
# -----------------------------------

def recommend_fertilizer(soil_ph, humidity, rainfall):
    if soil_ph < 6.0:
        return "Lime + Organic Compost"
    elif soil_ph > 7.5:
        return "Ammonium Sulfate"
    elif rainfall < 100:
        return "Nitrogen Rich Fertilizer"
    elif humidity > 85:
        return "Potassium Rich Fertilizer"
    else:
        return "Balanced NPK Fertilizer"

# -----------------------------------
# Streamlit UI
# -----------------------------------
st.set_page_config(page_title="Agriculture Intelligence Platform", layout="wide")

st.title("🌱 Agriculture Intelligence Platform")
st.markdown("### Smart Farming using AI and Machine Learning")
st.write("AI-powered crop yield prediction system")

# Sidebar Inputs
st.sidebar.header("Enter Farm Details")

rainfall = st.sidebar.slider("Rainfall (mm)", 50, 500, 150)
temperature = st.sidebar.slider("Temperature (°C)", 10, 45, 28)
humidity = st.sidebar.slider("Humidity (%)", 20, 100, 70)
soil_ph = st.sidebar.slider("Soil pH", 4.0, 9.0, 6.5)

# Sidebar Crop Selection
crop_type = st.sidebar.selectbox(
    "Select Crop",
    ["Rice", "Wheat", "Maize", "Tomato", "Cotton"]
)

# Prediction Button
if st.sidebar.button("Predict Crop Yield"):
    input_data = np.array([[rainfall, temperature, humidity, soil_ph]])
    predicted_yield = model.predict(input_data)[0]

    st.subheader("📈 Prediction Result")
    st.success(f"Estimated Crop Yield: {predicted_yield:.2f} tons/hectare")

    fertilizer = recommend_fertilizer(soil_ph, humidity, rainfall)

    st.subheader("🧪 Fertilizer Recommendation")
    st.info(f"Recommended Fertilizer: {fertilizer}")

    st.subheader("🌦 Weather Advisory")

    if rainfall > 250:
        st.warning("Heavy rainfall expected. Ensure proper drainage.")
    elif rainfall < 100:
        st.warning("Low rainfall expected. Use irrigation support.")
    else:
        st.success("Weather conditions are suitable for farming.")

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    st.caption(f"Prediction generated on: {current_time}")

# -----------------------------------
# Display Dataset
# -----------------------------------
# -----------------------------------
# Dashboard Metrics
# -----------------------------------

st.subheader("📌 Farm Analytics Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Average Yield", f"{df['yield'].mean():.2f} t/ha")

with col2:
    st.metric("Average Rainfall", f"{df['rainfall'].mean():.0f} mm")

with col3:
    st.metric("Average Temperature", f"{df['temperature'].mean():.1f} °C")

# -----------------------------------
# Charts
# -----------------------------------

st.subheader("📈 Agriculture Data Visualization")

st.write(df)
# -----------------------------------
# Dataset Section
# -----------------------------------

st.subheader("📊 Sample Agriculture Dataset")
st.dataframe(df)

# -----------------------------------
# Model Performance
# -----------------------------------
st.subheader("🤖 Model Performance")
st.write(f"Mean Absolute Error: {mae:.2f}")

# -----------------------------------
# Insights Section
# -----------------------------------
st.subheader("🌾 Farming Insights")

if rainfall < 100:
    st.warning("Low rainfall detected. Consider irrigation support.")

if humidity > 85:
    st.warning("High humidity may increase plant disease risk.")

if soil_ph < 6.0:
    st.warning("Soil is acidic. Consider lime treatment.")

if soil_ph > 7.5:
    st.warning("Soil is alkaline. Monitor nutrient availability.")

# -----------------------------------
#
# -----------------------------------
st.markdown("---")
st.caption("Built using Python, Streamlit, Scikit-learn, Pandas and NumPy")
soil_type = st.sidebar.selectbox(
    "Select Soil Type",
    ["Clay", "Sandy", "Loamy", "Black", "Red"]
)

def recommend_crop(soil_type, rainfall, temperature):
    
    recommendations = []

    if soil_type == "Clay":
        recommendations = ["Rice", "Wheat"]

    elif soil_type == "Sandy":
        recommendations = ["Groundnut", "Watermelon"]

    elif soil_type == "Loamy":
        recommendations = ["Sugarcane", "Cotton"]

    elif soil_type == "Black":
        recommendations = ["Cotton", "Soybean"]

    elif soil_type == "Red":
        recommendations = ["Millets", "Pulses"]

    # Weather-based improvements
    if rainfall > 250:
        recommendations.append("Banana")

    if temperature > 32:
        recommendations.append("Maize")

    return recommendations
recommended_crops = recommend_crop(
    soil_type,
    rainfall,
    temperature
)

st.subheader("🌾 Recommended Crops")

for crop in recommended_crops:
    st.success(crop)
crop_database = {

    "Wheat": {
        "soil": "Loamy Soil, Clay Loam",
        "rainfall": "50 - 100 mm",
        "temperature": "10°C - 25°C",
        "humidity": "50% - 60%",
        "season": "Winter",
        "ph": "6.0 - 7.5",
        "duration": "110 - 130 days"
    },

    "Rice": {
        "soil": "Clay Soil",
        "rainfall": "150 - 300 mm",
        "temperature": "20°C - 35°C",
        "humidity": "70% - 85%",
        "season": "Monsoon",
        "ph": "5.0 - 6.5",
        "duration": "90 - 150 days"
    },

    "Maize": {
        "soil": "Loamy Soil",
        "rainfall": "60 - 120 mm",
        "temperature": "18°C - 27°C",
        "humidity": "60% - 70%",
        "season": "Spring",
        "ph": "5.5 - 7.0",
        "duration": "80 - 120 days"
    },

    "Cotton": {
        "soil": "Black Soil",
        "rainfall": "60 - 100 mm",
        "temperature": "21°C - 30°C",
        "humidity": "50% - 65%",
        "season": "Summer",
        "ph": "5.8 - 8.0",
        "duration": "150 - 180 days"
    },

    "Sugarcane": {
        "soil": "Loamy Soil",
        "rainfall": "100 - 150 mm",
        "temperature": "20°C - 32°C",
        "humidity": "75% - 85%",
        "season": "Tropical",
        "ph": "6.0 - 7.5",
        "duration": "10 - 18 months"
    }
}
selected_crop = st.selectbox(
    "Select Crop",
    list(crop_database.keys())
)
crop_info = crop_database[selected_crop]

st.subheader("🌾 Crop Requirements")

st.success(f"Best Soil: {crop_info['soil']}")

st.info(f"Rainfall Needed: {crop_info['rainfall']}")

st.warning(f"Temperature: {crop_info['temperature']}")

st.write(f"Humidity: {crop_info['humidity']}")

st.write(f"Best Season: {crop_info['season']}")

st.write(f"Soil pH: {crop_info['ph']}")

st.write(f"Growing Duration: {crop_info['duration']}")
# -----------------------------------
# Optional Dataset Upload
# -----------------------------------

st.subheader("📂 Upload Agriculture Dataset")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write("Uploaded Dataset Preview")
    st.dataframe(uploaded_df)


