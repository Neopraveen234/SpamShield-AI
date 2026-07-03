import sqlite3
from datetime import datetime

from datetime import datetime
from src.database import get_connection



def save_prediction(message,prediction,spam_probability,ham_probability):
    """
    Save prediction into SQLite database.
    """

    conn=get_connection()
    cursor=conn.cursor()

    now=datetime.now()

    date=now.strftime("%Y-%m-%d")
    time=now.strftime("%H:%M:%S")

    cursor.execute(
        """
        INSERT INTO predictions
        (
        date,
        time,
        message,
        prediction,
        spam_probability,
        ham_probability
        )
        VALUES(?,?,?,?,?,?)
        """,
        (
            date,
            time,
            message,
            prediction,
            spam_probability,
            ham_probability
        )
    )

    conn.commit()
    conn.close()

def get_all_predictions():
    """
    Return all saved predictions.
    """

    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        SELECT * FROM predictions
        ORDER BY id DESC
    """)

    rows=cursor.fetchall()
    conn.close()
    return rows