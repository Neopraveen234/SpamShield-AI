import streamlit as st


def about_model_page():

    st.title("🧠 About the AI Model")

    st.write(
        """
SpamShield AI uses a **Machine Learning** model to classify SMS
messages as **Spam** or **Ham**.

The application is designed to identify suspicious SMS messages
using Natural Language Processing (NLP) and Machine Learning.
"""
    )

    st.divider()

    st.header("📌 Model Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Algorithm", "Linear SVM")
        st.metric("Vectorizer", "TF-IDF")
        st.metric("Language", "English SMS")

    with col2:
        st.metric("Dataset", "SMS Spam Collection")
        st.metric("Database", "SQLite")
        st.metric("Prediction", "Spam / Ham")

    st.divider()

    st.header("⚙️ AI Workflow")

    st.markdown("""
    """)

    st.divider()

    st.header("✨ Features")

    st.success("""
✅ Spam Detection

✅ Ham Detection

✅ Confidence Score

✅ Risk Level

✅ AI Explanation

✅ Suspicious Keyword Detection

✅ Prediction History

✅ Statistics Dashboard
""")

    st.divider()

    st.header("⚠️ Model Limitations")

    st.warning("""
• Works best with English SMS messages.

• Modern scam messages may require additional training.

• Does not verify the sender's identity.

• Predictions depend on the quality of the training data.
""")

    st.divider()

    st.header("🚀 Future Improvements")

    st.info("""
Version 2 Goals

• Android Application

• Live SMS Monitoring

• Sender Verification

• Continuous Model Retraining

• Modern Scam Dataset

• Deep Learning Models
""")