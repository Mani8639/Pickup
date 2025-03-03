# Save this code as pickup_app.py
import streamlit as st
import pickle
import numpy as np

# Load the trained CatBoost model
model = pickle.load(open("model_pickup.pkl", "rb"))

st.title("ETA Prediction of Pickup")
st.write("Enter details to predict the Estimated Time of Arrival (ETA) for pickup.")

# Input fields
region_id = st.number_input("Region ID", value=0)
courier_id = st.number_input("Courier ID", value=0)
lng = st.number_input("Longitude", value=0.0)
lat = st.number_input("Latitude", value=0.0)
aoi_id = st.number_input("AOI ID", value=0)
aoi_type = st.number_input("AOI Type", value=0)
pickup_gps_lng = st.number_input("Pickup GPS Longitude", value=0.0)
pickup_gps_lat = st.number_input("Pickup GPS Latitude", value=0.0)
accept_gps_lng = st.number_input("Accept GPS Longitude", value=0.0)
accept_gps_lat = st.number_input("Accept GPS Latitude", value=0.0)
accept_hour_of_day = st.number_input("Accept Hour of Day", value=0)
accept_day_of_week = st.number_input("Accept Day of Week", value=0)
pickup_hour = st.number_input("Pickup Hour", value=0)
pickup_day_of_week = st.number_input("Pickup Day of Week", value=0)
pickup_distance = st.number_input("Pickup Distance", value=0.0)
log_pickup_distance = st.number_input("Log Pickup Distance", value=0.0)
pca1 = st.number_input("PCA1", value=0.0)
pca2 = st.number_input("PCA2", value=0.0)

# Prediction
if st.button("Predict ETA"):
    input_features = np.array([[region_id, courier_id, lng, lat, aoi_id, aoi_type, pickup_gps_lng, pickup_gps_lat, accept_gps_lng, accept_gps_lat,accept_hour_of_day, accept_day_of_week, pickup_hour, pickup_day_of_week, pickup_distance, log_pickup_distance, pca1, pca2]])
    prediction = model.predict(input_features)
    st.success(f"Predicted ETA: {prediction[0]:.2f} minutes")
