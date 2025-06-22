# 🥑 Avocado Ripeness Predictor

This Streamlit web app predicts the **ripeness stage of a Hass avocado** based on physical measurements like firmness, color, size, sound level, and more.

## 🔍 Features
- Enter 8 physical features manually
- Predicts ripeness: Hard, Firm-Ripe, Ripe, Pre conditioned, Breaking, etc.
- Built using Random Forest Classifier
- Styled interface with emojis and colors for easy readability

## 📊 Model Details
- Trained on a synthetic dataset with 240 samples
- 8 input features used:
  - firmness
  - hue
  - saturation
  - brightness
  - color_category
  - sound_db
  - weight_g
  - size_cm3

## 🚀 Live Demo
[Click here to try the app](https://your-deployed-link.streamlit.app)  ← *(replace after deploy)*

## 🛠️ Tech Stack
- Python
- Streamlit
- Scikit-learn
- NumPy / Pandas

## 🧠 How to Use
1. Clone the repo or upload your files to GitHub
2. Deploy on [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your `Avocado_app.py`, `rf_model.pkl`, `scaler.pkl`, and `requirements.txt`
4. Deploy and share the link!

## 📄 License
MIT License. Use freely with attribution.
