import streamlit as st


def about_developer_page():

    st.title("👨‍💻 About the Developer")

    st.write("""
Welcome to **SpamShield AI**.

This project was developed to demonstrate practical applications of
Machine Learning, Natural Language Processing, and Data Analytics
for detecting spam SMS messages.
""")

    st.divider()

    st.header("🎯 Project Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Project", "SpamShield AI")
        st.metric("Version", "1.0")
        st.metric("Status", "Stable")

    with col2:
        st.metric("Framework", "Streamlit")
        st.metric("Language", "Python")
        st.metric("Database", "SQLite")

    st.divider()

    st.header("🛠️ Technologies Used")

    st.success("""
• Python

• Streamlit

• Scikit-learn

• Pandas

• NumPy

• Plotly

• SQLite
""")

    st.divider()

    st.header("📚 Skills Demonstrated")

    st.info("""
✔ Machine Learning

✔ Natural Language Processing

✔ Data Preprocessing

✔ Feature Engineering

✔ Model Training

✔ Model Evaluation

✔ SQLite Database

✔ Data Visualization

✔ Streamlit Application Development
""")

    st.divider()

    st.header("🎓 Learning Outcomes")

    st.write("""
This project demonstrates:

• Data Preparation

• Machine Learning Model Development

• Data Analytics

• Database Integration

• Interactive Dashboard Design

• AI-powered Prediction System
""")

    st.divider()

    st.header("🗺️ Roadmap")

    st.markdown("""
### ✅ Version 1.0

- Spam Detection
- Prediction History
- Statistics Dashboard
- AI Explanation
- Risk Analysis

---

### 🚀 Version 2.0

- Android Application

- Live SMS Detection

- Sender Verification

- Modern Spam Dataset

- Model Retraining

---

### 🌍 Version 3.0

- Deep Learning Models

- Cloud Deployment

- Multi-language Support

- Real-time Threat Detection
""")

    st.divider()

    st.caption(
        "© 2026 SpamShield AI | Machine Learning Project"
    )