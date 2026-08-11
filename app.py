import streamlit as st
import pandas as pd
import joblib


# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)


# --------------------------------
# Load Trained Model
# --------------------------------

model = joblib.load("models/house_price_model.pkl")


# --------------------------------
# Custom CSS
# --------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #f8fafc 0%,
        #eef2ff 100%
    );
}

.hero {
    padding: 35px 20px 25px 20px;
    text-align: center;
}

.hero h1 {
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero p {
    font-size: 18px;
    color: #64748b;
}

.section-title {
    font-size: 25px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 15px;
}

.result-card {
    padding: 30px;
    border-radius: 22px;
    background: white;
    text-align: center;
    box-shadow: 0 12px 35px rgba(0,0,0,0.10);
    margin-top: 25px;
}

.result-label {
    font-size: 18px;
    color: #64748b;
}

.result-price {
    font-size: 42px;
    font-weight: 800;
    margin-top: 8px;
}

div.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 52px;
    font-size: 18px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------
# Hero Section
# --------------------------------

st.markdown("""
<div class="hero">

<h1>🏠 House Price Predictor</h1>

<p>
Estimate the price of a house using Machine Learning
</p>

</div>
""", unsafe_allow_html=True)

st.divider()


# --------------------------------
# Property Details
# --------------------------------

st.markdown(
    '<div class="section-title">🏡 Property Details</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    area = st.number_input(
        "📐 Area (sq ft)",
        min_value=500,
        max_value=20000,
        value=5000,
        step=100
    )


with col2:

    bedrooms = st.number_input(
        "🛏️ Bedrooms",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )


with col3:

    bathrooms = st.number_input(
        "🛁 Bathrooms",
        min_value=1,
        max_value=10,
        value=2,
        step=1
    )


col1, col2, col3 = st.columns(3)


with col1:

    stories = st.number_input(
        "🏢 Stories",
        min_value=1,
        max_value=10,
        value=2,
        step=1
    )


with col2:

    parking = st.number_input(
        "🚗 Parking Spaces",
        min_value=0,
        max_value=5,
        value=1,
        step=1
    )


with col3:

    furnishingstatus = st.selectbox(
        "🛋️ Furnishing Status",
        [
            "furnished",
            "semi-furnished",
            "unfurnished"
        ]
    )


# --------------------------------
# Property Features
# --------------------------------

st.markdown(
    '<div class="section-title">✨ Property Features</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    mainroad = st.toggle(
        "🛣️ Main Road Access"
    )


with col2:

    guestroom = st.toggle(
        "🛏️ Guest Room"
    )


with col3:

    basement = st.toggle(
        "🏠 Basement"
    )


col1, col2, col3 = st.columns(3)


with col1:

    hotwaterheating = st.toggle(
        "🔥 Hot Water Heating"
    )


with col2:

    airconditioning = st.toggle(
        "❄️ Air Conditioning"
    )


with col3:

    prefarea = st.toggle(
        "📍 Preferred Area"
    )


st.write("")


# --------------------------------
# Prediction Button
# --------------------------------

predict_button = st.button(
    "✨ Predict House Price",
    type="primary"
)


# --------------------------------
# Prediction
# --------------------------------

# --------------------------------
# Prediction
# --------------------------------

if predict_button:

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "parking": [parking],

        "mainroad_yes": [mainroad],
        "guestroom_yes": [guestroom],
        "basement_yes": [basement],
        "hotwaterheating_yes": [hotwaterheating],
        "airconditioning_yes": [airconditioning],
        "prefarea_yes": [prefarea],

        "furnishingstatus_semi-furnished": [
            furnishingstatus == "semi-furnished"
        ],

        "furnishingstatus_unfurnished": [
            furnishingstatus == "unfurnished"
        ]
    })

    # Model prediction
    prediction = model.predict(input_data)[0]

    # Result
    st.success("Prediction completed successfully!")

    st.markdown("## 🏠 Estimated House Price")

    st.metric(
        label="Predicted Price",
        value=f"₹{prediction:,.0f}"
    )

    st.info(
        "This prediction is generated using the Linear Regression model."
    )