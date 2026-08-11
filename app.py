import streamlit as st
import pickle
import numpy as np

# =====================================
# PAGE CONFIG
# =====================================
st.set_page_config(
    page_title="Predict-O-Crop",
    page_icon="🌱",
    layout="wide"
)

# =====================================
# LOAD MODEL
# =====================================
with open("models/RandomForest.pkl", "rb") as f:
    model = pickle.load(f)

# =====================================
# CROP IMAGES
# =====================================
crop_images = {
    "rice": "assets/rice.jpg",
    "maize": "assets/maize.jpg",
    "banana": "assets/banana.jpg",
    "cotton": "assets/cotton.jpg",
    "coffee": "assets/coffee.jpg",
    "apple": "assets/apple.jpg",
    "mango": "assets/mango.jpg",
    "orange": "assets/orange.jpg"
}

# =====================================
# SIDEBAR
# =====================================
st.sidebar.title("🌱 Predict-O-Crop")

st.sidebar.markdown("""
### About

This application recommends the most suitable crop based on:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

**Model:** Random Forest Classifier
""")

# =====================================
# HEADER
# =====================================
st.title("🌱 Predict-O-Crop")
st.markdown(
    "### AI-Powered Crop Recommendation System"
)

st.write(
    "Adjust the soil nutrient and weather parameters below to predict the most suitable crop."
)

st.divider()

# =====================================
# INPUT SECTION
# =====================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Soil Nutrients")

    N = st.slider(
        "Nitrogen (N)",
        min_value=0,
        max_value=200,
        value=90
    )

    P = st.slider(
        "Phosphorus (P)",
        min_value=0,
        max_value=200,
        value=42
    )

    K = st.slider(
        "Potassium (K)",
        min_value=0,
        max_value=200,
        value=43
    )

with col2:
    st.subheader("🌦️ Environmental Conditions")

    temperature = st.slider(
        "Temperature (°C)",
        min_value=0.0,
        max_value=50.0,
        value=20.8,
        step=0.1
    )

    humidity = st.slider(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=82.0,
        step=0.1
    )

    ph = st.slider(
        "pH Level",
        min_value=0.0,
        max_value=14.0,
        value=6.5,
        step=0.1
    )

    rainfall = st.slider(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=300.0,
        value=202.9,
        step=0.1
    )

st.divider()

# =====================================
# NPK METRICS
# =====================================
m1, m2, m3 = st.columns(3)

m1.metric("Nitrogen", N)
m2.metric("Phosphorus", P)
m3.metric("Potassium", K)

st.divider()

# =====================================
# PREDICTION
# =====================================
if st.button("🌾 Predict Crop", use_container_width=True):

    input_data = np.array([
        [N, P, K, temperature, humidity, ph, rainfall]
    ])

    prediction = model.predict(input_data)

    crop = prediction[0].lower()

    st.success(
        f"🌱 Recommended Crop: {crop.capitalize()}"
    )

    # Show image if available
    if crop in crop_images:
        st.image(
            crop_images[crop],
            caption=f"Recommended Crop: {crop.capitalize()}",
            width=500
        )

    

st.divider()

# =====================================
# FOOTER
# =====================================
st.markdown("""
### About the Project

Predict-O-Crop is a Machine Learning based crop recommendation system that helps farmers and agricultural enthusiasts identify the most suitable crop based on soil nutrients and environmental conditions.

**Technologies Used**
- Python
- Streamlit
- Scikit-Learn
- NumPy
- Random Forest Classifier

Developed as an end-to-end Machine Learning project.
""")