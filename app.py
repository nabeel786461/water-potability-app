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
            background: linear-gradient(to right, #a1c4fd, #c2e9fb);
            color: #000000;
        }
        h1, h2, h3 {
            font-family: 'Arial Black', sans-serif;
        }
        .card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
            margin: 15px 0;
            width: 330px;
        }
        .stButton>button {
            width: 100%;
            background: linear-gradient(90deg, #0066ff, #00c6ff);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 10px 0;
            font-size: 13px;
            font-weight: bold;
            display: block;
            margin: auto;
            box-shadow: 0px 4px 10px rgba(0, 102, 255, 0.3);
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #00c6ff, #0066ff);
            transform: scale(1.05);
            box-shadow: 0px 8px 18px rgba(0, 102, 255, 0.5);
            color: black;
        }
    </style>
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
# Layout: Card (left) + Sliders (right)
# -------------------------------
col1, col2 = st.columns([1, 3])  # Left small card, Right wide for sliders

with col1:
    st.markdown("""
        <div class="card">
            <h3>👨‍💻 Created by <b>Nabeel Arshad</b></h3>
            ⚡ Model Accuracy: 69.05% <br>
            🧠 Algorithm: Random Forest <br>
            🌳 Balancing: SMOTE
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <h3 style="color:#004488; text-align:left; font-family:Arial;">
            🔹 Enter Water Quality Parameters
        </h3>
    """, unsafe_allow_html=True)

    col21, col22, col23 = st.columns(3)

    with col21:
        ph = st.slider("pH Value (0 - 14)", 0.0, 14.0, 7.0)
        hardness = st.slider("Hardness (0 - 400)", 0.0, 400.0, 150.0)
        solids = st.slider("Solids (0 - 50000)", 0.0, 50000.0, 20000.0)

    with col22:
        chloramines = st.slider("Chloramines (0 - 15)", 0.0, 15.0, 7.0)
        sulfate = st.slider("Sulfate (0 - 500)", 0.0, 500.0, 333.0)
        conductivity = st.slider("Conductivity (0 - 2000)", 0.0, 2000.0, 400.0)

    with col23:
        organic_carbon = st.slider("Organic Carbon (0 - 50)", 0.0, 50.0, 10.0)
        trihalomethanes = st.slider("Trihalomethanes (0 - 150)", 0.0, 150.0, 66.0)
        turbidity = st.slider("Turbidity (0 - 10)", 0.0, 10.0, 4.0)

    # Predict button under parameters
    predict_btn = st.button("🔮 Predict Potability")

# -------------------------------
# Prediction Result
# -------------------------------
if predict_btn:
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity,
                                organic_carbon, trihalomethanes, turbidity]],
                                columns=["ph", "Hardness", "Solids", "Chloramines", "Sulfate", 
                                         "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"])
    
    prediction = model.predict(input_data)[0]

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
