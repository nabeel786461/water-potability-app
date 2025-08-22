import streamlit as st
import joblib
import pandas as pd

# -------------------------------
# Title & Description
# -------------------------------
st.set_page_config(page_title="Water Potability Predictor 💧", page_icon="💧", layout="centered")
st.title("💧 Water Potability Prediction App")
st.markdown("Enter the water quality parameters below and check whether the water is **Potable (Safe to Drink)** or **Not Potable (Unsafe)**.")



MODEL_ACCURACY = 0.82   # <- apna actual accuracy score daal do
st.info(f"📊 Model Accuracy: **{MODEL_ACCURACY*100:.2f}%**")



# -------------------------------
# Load the trained model
# -------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("rf_water_model_compressed.pkl")   # Model file must be in repo
    return data["model"], data["accuracy"]

model, accuracy = load_model()

# Show accuracy in UI
st.info(f"📊 Model Accuracy: **{accuracy*100:.2f}%**")

# -------------------------------
# User Input Form
# -------------------------------
st.header("🔹 Enter Water Quality Parameters")

with st.form("input_form"):
    ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=7.0)
    hardness = st.number_input("Hardness", min_value=0.0, value=150.0)
    solids = st.number_input("Solids", min_value=0.0, value=20000.0)
    chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0)
    sulfate = st.number_input("Sulfate", min_value=0.0, value=333.0)
    conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0)
    organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=10.0)
    trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=66.0)
    turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)
    
    submitted = st.form_submit_button("🔮 Predict Potability")

# -------------------------------
# Prediction
# -------------------------------
if submitted:
    input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity,
                                organic_carbon, trihalomethanes, turbidity]],
                                columns=["ph", "Hardness", "Solids", "Chloramines", "Sulfate", 
                                         "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"])
    
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("✅ Water is **Potable (Safe to Drink)**")
    else:
        st.error("⚠️ Water is **Not Potable (Unsafe to Drink)**")
