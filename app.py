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
# Info Card
# -------------------------------
st.markdown("""
<div class="card" style="max-width:500px; float:left; text-align:left;">
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

st.markdown("""
    <h3 style="text-align:left; color:#0066cc; font-family:Arial, sans-serif; margin-bottom:10px;">
        🔹 Enter Water Quality Parameters
    </h3>
""", unsafe_allow_html=True)


# -------------------------------
# Two Column Layout
# -------------------------------
left_col, right_col = st.columns([2,1])   # left column wider (2x), right smaller (1x)

with left_col:
    st.markdown("""
        <h3 style="text-align:left; color:#0066cc; font-family:Arial, sans-serif; margin-bottom:10px;">
            🔹 Enter Water Quality Parameters
        </h3>
    """, unsafe_allow_html=True)

    with st.form("input_form"):
        ph = st.number_input("pH Value (0 - 14)", min_value=0.0, max_value=14.0, value=7.0)
        hardness = st.number_input("Hardness", min_value=0.0, value=150.0)
        solids = st.number_input("Solids", min_value=0.0, value=20000.0)
        chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0)
        sulfate = st.number_input("Sulfate", min_value=0.0, value=333.0)
        conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0)
        organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=10.0)
        trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=66.0)
        turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)
        
        submitted = st.form_submit_button("🔮 Predict Potability")

with right_col:
    st.markdown("""
    <div class="card" style="max-width:400px; text-align:left; float:right;">
        <h3>👨‍💻 Created by <b>Nabeel Arshad</b></h3>
        ⚡ Model Accuracy: 69.05% <br>
        🧠 Algorithm: Random Forest <br>
        🌳 Balancing: SMOTE
    </div>
    """, unsafe_allow_html=True)


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
