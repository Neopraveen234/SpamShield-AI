import os

import pandas as pd
import streamlit as st

from src.history import get_all_predictions
def history_page():

    st.title("📜 Prediction History")

    rows=get_all_predictions()

    if len(rows)==0:
        st.info("No predictions history available.")
        return
    
    history=pd.DataFrame(
        rows,
        columns=[
            "ID",
            "Date",
            "Time",
            "Message",
            "Prediction",
            "Spam %",
            "Ham %"
        ]
    )
    
    st.dataframe(
        history,
        width='stretch',
        hide_index=True
    )

    
