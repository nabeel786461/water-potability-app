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
            width: 100%;
            background: linear-gradient(90deg, #0066ff, #00c6ff);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 10px 0;
            font-size: 14px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #00c6ff, #0066ff);
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title & Description
# -------------------------------
st.markdown("""
    <h2 style="text-align:left; color:#0066cc; font-family:Arial, sans-serif; margin-bottom:0;">
        💧 Water Potability Prediction App
    </h2>
    <p style="text-align:left; color:#333333; font-size:16px; margin-top:4px;">
        Check if your water is <b>safe to drink!</b>
    </p>
""", unsafe_allow_html=True)

# -------------------------------
# Layout with 4 Columns
# -------------------------------
col1, col2, col3, col4 = st.columns([1, 1.5, 1.5, 1.5])

# Info Card in col1
with col1:
    st.markdown("""
    <div class="card" style="max-width:400px; text-align:left;">
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
# Parameters Heading
# -------------------------------
st.markdown("""
    <h3 style="text-align:left; color:#0066cc; font-family:Arial, sans-serif; margin-bottom:10px;">
        🔹 Enter Water Quality Parameters
    </h3>
""", unsafe_allow_html=True)

# Parameters inside col2, col3, col4
with col2:
    ph = st.slider("pH Value (0 - 14)", 0.0, 14.0, 7.0)
    hardness = st.slider("Hardness (0 - 400)", 0.0, 400.0, 150.0)
    solids = st.slider("Solids (0 - 50000)", 0.0, 50000.0, 20000.0)

    # Prediction Button here only
    predict_btn = st.button("🔮 Predict Potability")

with col3:
    chloramines = st.slider("Chloramines (0 - 15)", 0.0, 15.0, 7.0)
    sulfate = st.slider("Sulfate (0 - 500)", 0.0, 500.0, 333.0)
    conductivity = st.slider("Conductivity (0 - 2000)", 0.0, 2000.0, 400.0)

with col4:
    organic_carbon = st.slider("Organic Carbon (0 - 50)", 0.0, 50.0, 10.0)
    trihalomethanes = st.slider("Trihalomethanes (0 - 150)", 0.0, 150.0, 66.0)
    turbidity = st.slider("Turbidity (0 - 10)", 0.0, 10.0, 4.0)

# -------------------------------
# Prediction Result (col3+col4)
# -------------------------------
if predict_btn:
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity,
                                organic_carbon, trihalomethanes, turbidity]],
                                columns=["ph", "Hardness", "Solids", "Chloramines", "Sulfate", 
                                         "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"])
    
    prediction = model.predict(input_data)[0]

    with col3, col4:
        if prediction == 1:
            st.markdown(
                """
                <div style="background:#e0f2ff; padding:12px; 
                            border-radius:10px; text-align:center; 
                            font-size:16px; font-weight:600;
                            border:1px solid #99d1ff;">
                    ✅ Water is Potable (Safe to Drink)
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div style="background:#ffe0e0; padding:12px; 
                            border-radius:10px; text-align:center; 
                            font-size:16px; font-weight:600;
                            border:1px solid #ff9999;">
                    ⚠️ Water is Not Potable (Unsafe)
                </div>
                """,
                unsafe_allow_html=True
            )
