Agriculture Intelligence Platform - README.md
🌱 Agriculture Intelligence Platform

An AI-powered Smart Farming Application built using Python, Streamlit, Machine Learning, Pandas, NumPy, and Scikit-learn. This platform helps farmers and agricultural researchers make data-driven decisions through crop yield prediction, fertilizer recommendations, crop suggestions, and farm analytics.

🚀 Features
1. Crop Yield Prediction
Predicts crop yield based on:
Rainfall
Temperature
Humidity
Soil pH
Uses a Random Forest Regressor Machine Learning model.
2. Fertilizer Recommendation

Provides fertilizer suggestions based on:

Soil pH
Rainfall
Humidity

Examples:

Acidic Soil → Lime + Organic Compost
Low Rainfall → Nitrogen Rich Fertilizer
High Humidity → Potassium Rich Fertilizer
3. Weather Advisory

Generates farming recommendations such as:

Heavy rainfall alerts
Irrigation support suggestions
Suitable weather notifications
4. Farm Analytics Dashboard

Displays:

Average Crop Yield
Average Rainfall
Average Temperature
5. Crop Recommendation System

Suggests crops based on:

Soil Type
Rainfall
Temperature

Supported Soil Types:

Clay
Sandy
Loamy
Black
Red
6. Crop Information Database

Provides detailed information about:

Wheat
Rice
Maize
Cotton
Sugarcane

Including:

Suitable Soil
Rainfall Requirement
Temperature Range
Humidity Requirement
Season
Soil pH
Growing Duration
7. Dataset Upload

Allows users to upload their own agriculture CSV datasets for analysis.

🛠️ Technologies Used
Python
Streamlit
Pandas
NumPy
Scikit-learn
Random Forest Regression
📂 Project Structure
Agriculture-Intelligence-Platform/
│
├── app.py
├── README.md
├── requirements.txt
└── dataset.csv (optional)
📦 Installation
Clone Repository
git clone https://github.com/yourusername/agriculture-intelligence-platform.git
cd agriculture-intelligence-platform
Install Dependencies
pip install -r requirements.txt

Or install manually:

pip install streamlit pandas numpy scikit-learn
▶️ Run Application
streamlit run app.py

Open the browser and navigate to:

http://localhost:8501
🤖 Machine Learning Model
Algorithm Used

Random Forest Regressor

Input Features
Rainfall
Temperature
Humidity
Soil pH
Output
Predicted Crop Yield (tons/hectare)
Evaluation Metric
Mean Absolute Error (MAE)
📊 Sample Dataset Attributes
Feature	Description
Rainfall	Annual rainfall in mm
Temperature	Temperature in °C
Humidity	Humidity percentage
Soil pH	Soil acidity/alkalinity
Yield	Crop yield (tons/hectare)
🎯 Future Enhancements
Real-time weather API integration
Disease detection using Deep Learning
Satellite imagery analysis
Mobile application support
IoT sensor integration
Market price prediction
Multi-crop yield forecasting
