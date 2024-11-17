import pandas as pd
import sqlite3
import hashlib

# Load and filter dataset
file_path = "vehicles.csv"  # Replace with your dataset file name if different

try:
    # Read the CSV file
    vehicles_data = pd.read_csv(file_path)

    # Filter for Toyota vehicles between 2021-2025
    toyota_data = vehicles_data[
        (vehicles_data['make'] == 'Toyota') &
        (vehicles_data['year'] >= 2021) &
        (vehicles_data['year'] <= 2025)
    ]

    # Select relevant fields
    selected_fields = ['make', 'model', 'year', 'city08', 'highway08', 'comb08', 'fuelType', 'cylinders', 'displ', 'drive', 'VClass']
    toyota_analysis_data = toyota_data[selected_fields]

    # Connect to SQLite database (or create it)
    conn = sqlite3.connect("toyota_analysis.db")
    cursor = conn.cursor()

    # Create Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    # Insert user data into Users table
    user_data = (1, "test@toyota.com", "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08")
    cursor.execute("INSERT OR IGNORE INTO Users (id, username, password) VALUES (?, ?, ?)", user_data)

    # Create Data table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Data (
            make TEXT,
            model TEXT,
            year INTEGER,
            city08 INTEGER,
            highway08 INTEGER,
            comb08 INTEGER,
            fuelType TEXT,
            cylinders REAL,
            displ REAL,
            drive TEXT,
            VClass TEXT
        )
    """)

    # Insert vehicle data into Data table
    toyota_analysis_data.to_sql("Data", conn, if_exists="append", index=False)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("Data successfully parsed and stored in 'toyota_analysis.db'.")
    print("Users and Data tables created and populated.")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure it's in the same directory as this script.")
except Exception as e:
    print(f"An error occurred: {e}")
