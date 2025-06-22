#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import joblib
import numpy as np


# In[2]:


st.title("🥑 Avocado Ripeness Predictor")
st.markdown("Predict ripeness based on avocado's physical characteristics.")


# In[3]:


# Load model and scaler
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")


# In[5]:


# Input fields for all 8 features
firmness = st.number_input("Firmness (0–100)", min_value=0.0, max_value=100.0, step=0.1)
hue = st.number_input("Hue (0–360)", min_value=0, max_value=360, step=1)
saturation = st.number_input("Saturation (0–100)", min_value=0, max_value=100, step=1)
brightness = st.number_input("Brightness (0–100)", min_value=0, max_value=100, step=1)

color_category = st.selectbox("Color Category", ["Black", "Green", "Dark Green", "Purple"])
color_dict = {"Black": 0, "Green": 1, "Dark Green": 2, "Purple": 3}
color_encoded = color_dict[color_category]

sound_db = st.number_input("Sound Level (dB)", min_value=0, max_value=150, step=1)
weight_g = st.number_input("Weight (g)", min_value=50, max_value=1000, step=10)
size_cm3 = st.number_input("Size (cm³)", min_value=10, max_value=2000, step=10)


# In[6]:


# Predict
if st.button("Predict Ripeness"):
    input_data = np.array([[firmness, hue, saturation, brightness,
                            color_encoded, sound_db, weight_g, size_cm3]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    # Ripeness label map with emoji and color
    ripeness_map = {
        0: ("Breaking", "🟠", "#FFA726"),
        1: ("Firm-Ripe", "🟢", "#66BB6A"),
        2: ("Hard", "🔵", "#42A5F5"),
        3: ("Pre-Conditioned", "🟡", "#FFEB3B"),
        4: ("Ripe", "🟣", "#AB47BC")
    }

    label, emoji, bg_color = ripeness_map[int(prediction)]

    # Display result
    st.markdown(
        f"""
        <div style='padding:10px; background-color:{bg_color}; border-radius:10px; text-align:center'>
            <h3 style='color:white;'>{emoji} Predicted Ripeness: <strong>{label}</strong></h3>
        </div>
        """,
        unsafe_allow_html=True
    )


# In[ ]:




