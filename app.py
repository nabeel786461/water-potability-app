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
# Title & Subtitle
# -------------------------------
st.title("💧 Water Potability Prediction App")
st.markdown("Enter the water quality parameters below and check if the water is **Potable (Drinkable)** or not.")

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load_model():
    return joblib.load("rf_water_model_compressed.pkl")

model = load_model()

# -------------------------------
# Layout
# -------------------------------
col1, col2 = st.columns([1,3])

with col1:
    st.markdown("""
    <div class="info-box">
        <h3>Created by Numair Amin</h3>
        <p>⚡ <b>Model Accuracy:</b> 69.05%</p>
        <p>🧠 <b>Algorithm:</b> Random Forest</p>
        <p>🌱 <b>Balancing:</b> SMOTE</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    c1, c2, c3 = st.columns(3)

    with c1:
        ph = st.slider("pH Value", 0.0, 14.0, 7.0)
        chloramines = st.slider("Chloramines", 0.0, 15.0, 8.0)
        organic_carbon = st.slider("Organic Carbon", 0.0, 50.0, 10.0)

    with c2:
        hardness = st.slider("Hardness", 0.0, 400.0, 200.0)
        sulfate = st.slider("Sulfate", 0.0, 500.0, 333.0)
        trihalomethanes = st.slider("Trihalomethanes", 0.0, 150.0, 66.0)

    with c3:
        solids = st.slider("Solids", 0.0, 50000.0, 20000.0)
        conductivity = st.slider("Conductivity", 0.0, 2000.0, 400.0)
        turbidity = st.slider("Turbidity", 0.0, 10.0, 4.0)

    # Prediction button
    if st.button("🔍 Check Potability"):
        input_data = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity,
                                    organic_carbon, trihalomethanes, turbidity]],
                                    columns=["ph", "Hardness", "Solids", "Chloramines", "Sulfate", 
                                             "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"])
        
        prediction = model.predict(input_data)[0]
        if prediction == 1:
            st.success("✅ Water is **Potable (Safe to Drink)**")
        else:
            st.error("⚠️ Water is **Not Potable (Unsafe to Drink)**")
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
# Sidebar - About Me Section
# -------------------------------
st.sidebar.header("👨‍💻 About Me")
st.sidebar.write("""
**Your Name Here**  
Data Science Enthusiast 💻 | ML Developer 🤖  

📧 Email: yourname@email.com  
🌐 GitHub: [yourusername](https://github.com/yourusername)  
""")

# -------------------------------
# Input Form in Three Columns
# -------------------------------
st.header("🔹 Enter Water Quality Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    ph = st.number_input("pH Value", min_value=0.0, max_value=14.0, value=7.0)
    hardness = st.number_input("Hardness", min_value=0.0, value=150.0)
    solids = st.number_input("Solids", min_value=0.0, value=20000.0)

with col2:
    chloramines = st.number_input("Chloramines", min_value=0.0, value=7.0)
    sulfate = st.number_input("Sulfate", min_value=0.0, value=333.0)
    conductivity = st.number_input("Conductivity", min_value=0.0, value=400.0)

with col3:
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
