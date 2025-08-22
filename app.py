
import streamlit as st
import joblib
import pandas as pd

# -------------------------------
# Page Config (Always first Streamlit command)
# -------------------------------
st.set_page_config(page_title="Water Potability Predictor 💧", page_icon="💧", layout="wide")

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #74ebd5 0%, #ACB6E5 100%);
        }
        h1 {
            color: #0a0a0a;
            font-weight: 800;
        }
        .info-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }
        .stButton>button {
            width: 100%;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 0;
            font-size: 18px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #0072ff, #00c6ff);
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title & Description
# -------------------------------
st.title("💧 Water Potability Prediction App")
st.markdown("Enter the water quality parameters below and check whether the water is **Potable (Drinkable)** or **Not Potable (Unsafe)**.")

# -------------------------------
# Info Box
# -------------------------------
st.markdown("""
<div class="info-box">
    <h3>👨‍💻 Created by <b>Nabeel Arshad</b></h3>
    ⚡ Model Accuracy: 67.3% <br>
    🧠 Algorithm: Random Forest <br>
    🌳 Balancing: SMOTE
</div>
""", unsafe_allow_html=True)

# -------------------------------
# Load the trained model
# -------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("rf_water_model_compressed.pkl")
    return model

model = load_model()

# -------------------------------
# User Input
# -------------------------------
st.header("🔹 Enter Water Quality Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    ph = st.slider("pH Value", 0.0, 14.0, 7.0)
    chloramines = st.slider("Chloramines", 0.0, 15.0, 7.0)
    organic_carbon = st.slider("Organic Carbon", 0.0, 50.0, 10.0)

with col2:
    hardness = st.slider("Hardness", 0.0, 400.0, 150.0)
    sulfate = st.slider("Sulfate", 0.0, 500.0, 333.0)
    trihalomethanes = st.slider("Trihalomethanes", 0.0, 150.0, 66.0)

with col3:
    solids = st.slider("Solids", 0.0, 50000.0, 20000.0)
    conductivity = st.slider("Conductivity", 0.0, 2000.0, 400.0)
    turbidity = st.slider("Turbidity", 0.0, 10.0, 4.0)

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("🔮 Check Potability"):
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity,
                                organic_carbon, trihalomethanes, turbidity]],
                                columns=["ph", "Hardness", "Solids", "Chloramines", "Sulfate", 
                                         "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"])
    
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ Water is **Potable (Safe to Drink)**")
    else:
        st.error("⚠️ Water is **Not Potable (Unsafe to Drink)**")
