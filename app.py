import streamlit as st
import joblib
import pandas as pd

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Water Potability Predictor 💧", page_icon="💧", layout="wide")

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
    <style>
        .main {
            background: #ffffff;
            color: #000000;
        }
        h1, h2, h3 {
            text-align: center;
            font-family: 'Arial Black', sans-serif;
        }
        .card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
            margin: 15px 0;
        }
        .stButton>button {
            width: 50%;
            background: linear-gradient(90deg, #0066ff, #00c6ff);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 0;
            font-size: 18px;
            font-weight: bold;
            display: block;
            margin: auto;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #00c6ff, #0066ff);
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.markdown("<h1>💧 Water Potability Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<h3>Check if your water is safe to drink!</h3>", unsafe_allow_html=True)

# -------------------------------
# Info Card
# -------------------------------
st.markdown("""
<div class="card" style="text-align:right; max-width:500px; margin:auto;">
    <h3>👨‍💻 Created by <b>Nabeel Arshad</b></h3>
    ⚡ Model Accuracy: 69.05% <br>
    🧠 Algorithm: Random Forest <br>
    🌳 Balancing: SMOTE
</div>
""", unsafe_allow_html=True)


# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("rf_water_model_compressed.pkl")
    return model

model = load_model()

# -------------------------------
# User Inputs
# -------------------------------
st.markdown("<h2>🔹 Enter Water Quality Parameters</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    ph = st.slider("pH Value (0 - 14)", 0.0, 14.0, 7.0)
    hardness = st.slider("Hardness (0 - 400)", 0.0, 400.0, 150.0)
    solids = st.slider("Solids (0 - 50000)", 0.0, 50000.0, 20000.0)

with col2:
    chloramines = st.slider("Chloramines (0 - 15)", 0.0, 15.0, 7.0)
    sulfate = st.slider("Sulfate (0 - 500)", 0.0, 500.0, 333.0)
    conductivity = st.slider("Conductivity (0 - 2000)", 0.0, 2000.0, 400.0)

with col3:
    organic_carbon = st.slider("Organic Carbon (0 - 50)", 0.0, 50.0, 10.0)
    trihalomethanes = st.slider("Trihalomethanes (0 - 150)", 0.0, 150.0, 66.0)
    turbidity = st.slider("Turbidity (0 - 10)", 0.0, 10.0, 4.0)

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔮 Predict Potability"):
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity,
                                organic_carbon, trihalomethanes, turbidity]],
                                columns=["ph", "Hardness", "Solids", "Chloramines", "Sulfate", 
                                         "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"])
    
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.markdown('<div class="card" style="background:#c6f6d5;text-align:center;"><h2>✅ Water is Potable (Safe to Drink)</h2></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="card" style="background:#fed7d7;text-align:center;"><h2>⚠️ Water is Not Potable (Unsafe)</h2></div>', unsafe_allow_html=True)
