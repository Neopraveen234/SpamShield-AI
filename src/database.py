import sqlite3
import os

# =====================================
# Database Configuration
# =====================================

DB_FOLDER = "database"
DB_FILE = os.path.join(DB_FOLDER, "spamshield.db")


# =====================================
# Create Connection
# =====================================

def get_connection():
    """
    Returns a connection to the SQLite database.
    """

    os.makedirs(DB_FOLDER, exist_ok=True)

    return sqlite3.connect(DB_FILE)


# =====================================
# Initialize Database
# =====================================

def initialize_database():
    """
    Creates all required database tables.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # ---------------------------------
    # Prediction Table
    # ---------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date TEXT,

            time TEXT,

            message TEXT,

            prediction TEXT,

            spam_probability REAL,

            ham_probability REAL

        )
    """)

# =====================================
# Run Directly
# =====================================

if __name__ == "__main__":

    initialize_database()

    print("=" * 45)
    print("SpamShield AI Database Initialized")
    print("=" * 45)