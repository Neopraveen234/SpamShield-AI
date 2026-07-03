import streamlit as st
import pandas as pd
import plotly.express as px

from src.history import get_all_predictions


def statistics_page():

    # =====================================
    # Title
    # =====================================

    st.title("📊 SpamShield AI Analytics")

    st.write(
        """
Monitor prediction history, spam trends, and model performance.
This dashboard provides insights into all predictions made by SpamShield AI.
"""
    )

    st.divider()

    # =====================================
    # Load Data
    # =====================================

    rows = get_all_predictions()

    if len(rows) == 0:
        st.warning("No prediction history available.")
        return

    history = pd.DataFrame(
        rows,
        columns=[
            "ID",
            "Date",
            "Time",
            "Message",
            "Prediction",
            "Spam_Probability",
            "Ham_Probability"
        ]
    )

    # =====================================
    # Summary Statistics
    # =====================================

    total = len(history)

    spam = len(
        history[
            history["Prediction"] == "spam"
        ]
    )

    ham = len(
        history[
            history["Prediction"] == "ham"
        ]
    )

    spam_rate = (spam / total) * 100 if total > 0 else 0

    # =====================================
    # Dashboard Metrics
    # =====================================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📩 Total",
        total
    )

    col2.metric(
        "🚨 Spam",
        spam
    )

    col3.metric(
        "✅ Ham",
        ham
    )

    col4.metric(
        "📈 Spam Rate",
        f"{spam_rate:.1f}%"
    )

    st.divider()

    # =====================================
    # Average Confidence
    # =====================================

    st.subheader("🎯 Average Model Confidence")

    col1, col2 = st.columns(2)

    col1.metric(
        "Spam Confidence",
        f"{history['Spam_Probability'].mean():.2f}%"
    )

    col2.metric(
        "Ham Confidence",
        f"{history['Ham_Probability'].mean():.2f}%"
    )

    st.divider()

    # =====================================
    # Pie Chart
    # =====================================

    st.subheader("🥧 Spam vs Ham Distribution")

    fig = px.pie(
        names=["Spam", "Ham"],
        values=[spam, ham],
        title="Prediction Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    
    # =====================================
    # Prediction Activity by Selected Date
    # =====================================

    st.subheader("🕒 Daily Prediction Activity")

    # Get all available dates (Newest first)
    available_dates = sorted(
    history["Date"].unique(),
    reverse=True
)

    selected_date = st.selectbox(
    "📅 Select Date",
    available_dates
)

    # Filter history for selected date
    daily_history = history[
    history["Date"] == selected_date
].copy()

    # Extract Hour
    daily_history["Hour"] = pd.to_datetime(
    daily_history["Time"],
    format="%H:%M:%S"
).dt.strftime("%H:00")

    # Count predictions by hour
    hourly = (
    daily_history.groupby("Hour")
    .size()
    .reset_index(name="Predictions")
)

    # Create Bar Chart
    fig2 = px.bar(
    hourly,
    x="Hour",
    y="Predictions",
    text="Predictions",
    title=f"Prediction Activity - {selected_date}"
)

    fig2.update_traces(
    textposition="outside"
)

    fig2.update_layout(
    xaxis_title="Time",
    yaxis_title="Number of Predictions",
    xaxis=dict(
        categoryorder="category ascending"
    ),
    bargap=0.35,
    height=450
)

    st.plotly_chart(
    fig2,
    width="stretch"
)

    # =====================================
    # Daily Summary
    # =====================================

    total_today = len(daily_history)

    spam_today = len(
    daily_history[
        daily_history["Prediction"] == "spam"
    ]
)

    ham_today = len(
    daily_history[
        daily_history["Prediction"] == "ham"
    ]
)

    col1, col2, col3 = st.columns(3)

    col1.metric(
    "📩 Today's Predictions",
    total_today
)

    col2.metric(
    "🚨 Spam",
    spam_today
)

    col3.metric(
    "✅ Ham",
    ham_today
)
    # =====================================
    # Highest Risk Messages
    # =====================================

    st.subheader("⚠ Highest Risk Messages")

    top_spam = history.sort_values(
        by="Spam_Probability",
        ascending=False
    ).head(5)

    st.dataframe(
        top_spam[
            [
                "Date",
                "Message",
                "Prediction",
                "Spam_Probability"
            ]
        ],
        width="stretch",
        hide_index=True
    )

    st.divider()

    # =====================================
    # Dashboard Summary
    # =====================================

    st.subheader("📌 Dashboard Summary")

    st.success(
        f"""
📩 Total Predictions : {total}

🚨 Spam Messages : {spam}

✅ Ham Messages : {ham}

📈 Spam Rate : {spam_rate:.2f}%

🤖 Model Status : Active

🛡 Current Model : Linear SVM
"""
    )