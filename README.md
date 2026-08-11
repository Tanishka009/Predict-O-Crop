# 🌱 Predict-O-Crop

## Overview

Predict-O-Crop is a Machine Learning-based Crop Recommendation System that suggests the most suitable crop based on soil nutrients and environmental conditions.

The application uses a trained Random Forest Classifier and provides real-time predictions through an interactive Streamlit web interface.

---

## Features

* Crop recommendation based on soil and weather parameters
* Interactive Streamlit dashboard
* Real-time predictions
* Crop image display for selected crops
* User-friendly slider-based inputs

---

## Input Parameters

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH Level
* Rainfall

---

## Technologies Used

* Python
* Streamlit
* Scikit-Learn
* Pandas
* NumPy
* XGBoost

---

## Machine Learning Models Evaluated

* Decision Tree Classifier
* Random Forest Classifier
* Naive Bayes Classifier
* XGBoost Classifier

Random Forest was selected as the final model for deployment.

---

## Project Structure

```text
Predict-O-Crop/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   ├── rice.jpg
│   ├── maize.jpg
│   ├── banana.jpg
│   ├── cotton.jpg
│   ├── coffee.jpg
│   ├── apple.jpg
│   ├── mango.jpg
│   └── orange.jpg
│
├── models/
│   └── RandomForest.pkl
│
└── notebooks/
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move to the project directory:

```bash
cd Predict-O-Crop
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Future Enhancements

* Gemini API integration for AI-generated farming advice
* Fertilizer recommendation system
* Disease prediction module
* Weather API integration
* Advanced dashboard analytics

---

## Author

Tanishka Khandelwal

B.Tech Computer Science & Engineering

National Institute of Technology Hamirpur
