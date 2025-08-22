import streamlit as st
import joblib
import pandas as pd

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Water Potability Predictor 💧", page_icon="💧", layout="wide")

# -------------------------------
# Custom CSS for Styling
# -------------------------------
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 24px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .result-card {
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title & Description
# -------------------------------
st.title("💧 Water Potability Prediction App")
st.markdown("This app predicts whether the given water sample is **Potable (Safe to Drink)** or **Not Potable (Unsafe)**.")

# -------------------------------
# Show Accuracy
# -------------------------------
MODEL_ACCURACY = 0.6905
st.info(f"📊 Model Accuracy: **{MODEL_ACCURACY*100:.2f}%**")

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("rf_water_model_compressed.pkl")
    return model

model = load_model()

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("⚙️ Input Settings")
st.sidebar.write("Adjust the water quality parameters here:")

# -------------------------------
# Input Form in Two Columns
# -------------------------------
st.header("🔹 Enter Water Quality Parameters")

col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=7.0)
    hardness = st.number_input("Hardness", min_value=0.0, value=150.0)
    solids = st.number_input("Solids", min_value=0.0, value=20000.0)
    chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0)
    sulfate = st.number_input("Sulfate", min_value=0.0, value=333.0)

with col2:
    conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0)
    organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=10.0)
    trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=66.0)
    turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("🔮 Predict Potability"):
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity,
                                organic_carbon, trihalomethanes, turbidity]],
                                columns=["ph", "Hardness", "Solids", "Chloramines", "Sulfate", 
                                         "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.markdown('<div class="result-card" style="background-color:#d4edda; color:#155724;">✅ Water is Potable (Safe to Drink)</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-card" style="background-color:#f8d7da; color:#721c24;">⚠️ Water is Not Potable (Unsafe to Drink)</div>', unsafe_allow_html=True)
