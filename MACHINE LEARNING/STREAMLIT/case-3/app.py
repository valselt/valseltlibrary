import streamlit as st
import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import plotly.express as px
from sklearn.datasets import fetch_california_housing

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)
X, y = housing.data, housing.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load model and scaler
@st.cache_resource
def load_model():
    model = lgb.LGBMRegressor()
    model.fit(X_train, y_train)
    return model

@st.cache_resource
def load_scaler():
    scaler = StandardScaler()
    scaler.fit(X_train)
    return scaler

def main():
    st.title("🏠 California House Price Predictor")
    st.write("Prediksi harga rumah berdasarkan dataset California Housing")

    # Create input form
    with st.form("prediction_form"):
        st.subheader("Input Features")
        
        col1, col2 = st.columns(2)
        
        with col1:
            MedInc = st.number_input("Median Income (10k USD)", min_value=0.0, max_value=20.0, value=3.0)
            HouseAge = st.slider("House Age (years)", min_value=1, max_value=52, value=20)
            AveRooms = st.number_input("Average Rooms", min_value=1.0, max_value=10.0, value=5.0)
        
        with col2:
            AveBedrms = st.number_input("Average Bedrooms", min_value=0.0, max_value=5.0, value=1.0)
            Population = st.number_input("Population", min_value=0, max_value=5000, value=1000)
            AveOccup = st.number_input("Average Occupancy", min_value=1.0, max_value=10.0, value=3.0)
            Latitude = st.slider("Latitude", min_value=32.0, max_value=42.0, value=34.0)
            Longitude = st.slider("Longitude", min_value=-124.0, max_value=-114.0, value=-118.0)
        
        submitted = st.form_submit_button("Predict Price")
    
    if submitted:
        # Prepare input data
        input_data = pd.DataFrame({
            'MedInc': [MedInc],
            'HouseAge': [HouseAge],
            'AveRooms': [AveRooms],
            'AveBedrms': [AveBedrms],
            'Population': [Population],
            'AveOccup': [AveOccup],
            'Latitude': [Latitude],
            'Longitude': [Longitude]
        })
        
        # Scale the input data
        scaler = load_scaler()
        input_data_scaled = scaler.transform(input_data)
        
        # Make prediction
        with st.spinner("Calculating..."):
            model = load_model()
            prediction = model.predict(input_data_scaled)[0]
            
            # Display prediction
            st.subheader("Prediction Results")
            st.metric("Predicted House Price", f"${prediction * 100000:.2f}")  # Adjust for dataset scaling
            
            # Feature importance plot
            importance = pd.DataFrame({
                'feature': X.columns,
                'importance': model.feature_importances_
            })
            
            fig = px.bar(importance, x='feature', y='importance', title='Feature Importance')
            st.plotly_chart(fig)

            # Additional insights
            st.subheader("Price Insights")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Price per Room", f"${prediction / AveRooms * 100000:.2f}")
            
            with col2:
                st.metric("Population Impact", f"+${Population * 10:.2f}")
            
            with col3:
                age_impact = 500 if HouseAge > 30 else 0
                st.metric("House Age Impact", f"+${age_impact:.2f}")

if __name__ == "__main__":
    main()
