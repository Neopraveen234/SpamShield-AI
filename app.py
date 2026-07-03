import streamlit as st


from src.pages.home import home_page
from src.pages.history_page import history_page
from src.pages.statistics import statistics_page
from src.pages.about_model import about_model_page
from src.pages.about_developer import about_developer_page
from src.database import initialize_database

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="SpamShield AI",
    page_icon="🛡️",
    layout="wide"
)

initialize_database()


# -----------------------------
# Sidebar Navigation
# -----------------------------
page = st.sidebar.selectbox(
    "📂 Navigation",
    [
        "🏠 Home",
        "📊 Prediction History",
        "📈 Statistics",
        "⚙ About Model",
        "👨‍💻 About Developer"
    ]
)

# -----------------------------
# Routing
# -----------------------------
if page == "🏠 Home":
    home_page()

elif page == "📊 Prediction History":
    history_page()

elif page == "📈 Statistics":
    statistics_page()

elif page == "⚙ About Model":
    about_model_page()

elif page == "👨‍💻 About Developer":
    about_developer_page()