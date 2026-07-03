import streamlit as st
from datetime import datetime

from src.predict import predict_message
from src.history import save_prediction
from src.highlight import detect_keywords
from src.explain import explain_prediction


# ==========================================
# Session State
# ==========================================

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

if "message" not in st.session_state:
    st.session_state.message = ""

if "prediction_saved" not in st.session_state:
    st.session_state.prediction_saved = False


# ==========================================
# Home Page
# ==========================================

def home_page():

    st.title("🛡️ SpamShield AI")

    st.subheader("AI Powered SMS Spam Detection System")

    st.write(
        """
Detect whether an SMS message is **Spam** or **Ham**
using Machine Learning (Linear SVM + TF-IDF).
"""
    )

    st.divider()

    #initialize session state
    if"message"not in st.session_state:
        st.session_state.message=""

    message = st.text_area(
        "Enter your SMS Message",
        height=150
    )

    # ======================================
    # Prediction Button
    # ======================================

    if st.button("🔍 Predict Message"):

        if message.strip() == "":
            st.warning("Please enter a message.")
            return

        result = predict_message(message)

        st.session_state.prediction_result = result
        st.session_state.message = message
        st.session_state.prediction_saved = False

    # ======================================
    # Show Prediction
    # ======================================

    if st.session_state.prediction_result is None:
        return

    result = st.session_state.prediction_result
    message = st.session_state.message

    # Save only once
    if not st.session_state.prediction_saved:

        save_prediction(
            message,
            result["prediction"],
            result["spam_probability"],
            result["ham_probability"]
        )

        st.session_state.prediction_saved = True

    spam = result["spam_probability"]
    ham = result["ham_probability"]

    st.divider()

    st.subheader("Prediction")

    if result["prediction"] == "spam":
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Ham Message")

    # ======================================
    # Confidence
    # ======================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🚨 Spam Probability",
            f"{spam:.2f}%"
        )

        st.progress(spam / 100)

    with col2:

        st.metric(
            "✅ Ham Probability",
            f"{ham:.2f}%"
        )

        st.progress(ham / 100)

    confidence = max(spam, ham)

    st.info(
        f"🤖 Model Confidence : {confidence:.2f}%"
    )

    # ======================================
    # Risk Level
    # ======================================

    st.divider()

    st.subheader("🚦 Risk Level")

    if spam >= 90:

        st.error("🔴 Very High Risk")

    elif spam >= 70:

        st.warning("🟠 High Risk")

    elif spam >= 40:

        st.info("🟡 Medium Risk")

    else:

        st.success("🟢 Low Risk")

    # ======================================
    # AI Explanation
    # ======================================

    keywords = detect_keywords(message)

    reasons = explain_prediction(
        result["prediction"],
        spam,
        keywords
    )

    st.divider()

    st.subheader("🧠 AI Explanation")

    for reason in reasons:
        st.write(reason)

    st.subheader("🔍 Detected Suspicious Keywords")

    if keywords:

        for word in keywords:
            st.write(f"✔️ {word}")

    else:

        st.success("No suspicious keywords detected.")


    # ======================================
    # Recommendation
    # ======================================

    st.divider()

    st.subheader("💡 Recommendation")

    if result["prediction"] == "spam":

        st.warning(
            """
### 🚨 Security Tips

❌ Don't click suspicious links.

🔒 Never share your OTP or password.

📞 Verify the sender before responding.

🚫 Block and report suspicious numbers.

⚠️ Ignore offers that sound too good to be true.
"""
        )

    else:

        st.success(
            """
### ✅ Safe Message

✔️ This message appears to be legitimate.

📱 You can continue normally.

⚠️ Always stay cautious if personal or banking information is requested.
"""
        )

    
    # ======================================
    # Footer
    # ======================================

    st.divider()

    st.caption(
        "🛡️ SpamShield AI v1.0 | Powered by Linear SVM + TF-IDF | Developed using Streamlit"
    )