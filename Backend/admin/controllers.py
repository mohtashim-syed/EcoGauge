import hmac
from flask import session, jsonify, request
from hashlib import sha256
import sqlite3
import secrets 
import pandas as pd
import json
from openai import OpenAI
from flask import Flask
from routes import init_routes
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
	api_key = os.getenv("PROJECT_KEY")    
)


import time
import os

def signin_handler(email, password):
    MISSING_CREDENTIALS_ERROR = "Missing Email or Password", 401
    INVALID_CREDENTIALS_ERROR = "Incorrect Email or Password", 401
    UNAUTHORIZED_ERROR = "Unauthorized", 401


    # Validate the presence of 'email' and 'password'
    if not email or not password:
        return MISSING_CREDENTIALS_ERROR

    email = email.lower()
    hashed_password = sha256(password.encode('utf-8')).hexdigest()

    try:
        # Database connection and query
        with sqlite3.connect('toyota_analysis.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id, password, isAdmin FROM Users WHERE email = ?", (email,))
            user = cursor.fetchone()



        if user[2] == False:
            return UNAUTHORIZED_ERROR
        if not user:
            print(f"No user found with email: {email}")
            return INVALID_CREDENTIALS_ERROR

        if not hmac.compare_digest(user[1], hashed_password):
            print(f"Password mismatch for user: {email}")
            return INVALID_CREDENTIALS_ERROR

        # Set up session
        session['user_id'] = user[0]  # Store user ID in session
        session['email'] = email
        return "Signed in successfully", 200
    except sqlite3.Error as db_error:
        print(f"Database error: {db_error}")
        return f"Database Error: {str(db_error)}", 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Server Error: {str(e)}", 500


def reset_user_password():
    try:
        # Get form data
        user_email = request.form.get('reset_password_user')
        new_password = request.form.get('new_password')

        if not user_email or not new_password:
            return jsonify({"error": "Email and new password are required"}), 400

        # Hash the new password using SHA-256
        hashed_password = sha256(new_password.encode('utf-8')).hexdigest()

        # Update the password in the database
        with sqlite3.connect('toyota_analysis.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE Users SET password = ? WHERE email = ?",
                (hashed_password, user_email)
            )
            connection.commit()

            if cursor.rowcount == 0:
                return jsonify({"error": "User not found"}), 404

        return jsonify({"message": "Password successfully reset"}), 200

    except sqlite3.Error as db_error:
        return jsonify({"error": f"Database error: {str(db_error)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


# Controller for creating a new user
def create_user():
    try:
        # Get form data
        email = request.form.get('new_user_email')
        role = request.form.get('new_user_role')

        if not email or not role:
            return jsonify({"error": "Email and role are required"}), 400

        # Default values for a new user
        default_password = secrets.token_hex(16)
        hashed_password = sha256(default_password.encode('utf-8')).hexdigest()
        is_admin = True if role.lower() == 'admin' else False

        # Insert the new user into the database
        with sqlite3.connect('toyota_analysis.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Users (fullname, email, password, isAdmin, apikey)
                VALUES (?, ?, ?, ?, ?)
                """,
                ("New User", email.lower(), hashed_password, is_admin, secrets.token_hex(16))
            )
            connection.commit()

        return jsonify({
            "message": "User successfully created",
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "The email address is already registered."}), 409
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

def delete_user():
    try:
        # Get the email from the form
        email = request.form.get('delete_user_email')

        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Check if the user exists
        with sqlite3.connect('toyota_analysis.db') as connection:
            connection.row_factory = sqlite3.Row  # Enable dictionary-like access
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE email = ?", (email.lower(),))
            user = cursor.fetchone()

            if not user:
                return jsonify({"error": "User not found"}), 404

            # Delete the user from the database
            cursor.execute("DELETE FROM Users WHERE email = ?", (email.lower(),))
            connection.commit()

        return jsonify({"message": "User successfully deleted"}), 200

    except sqlite3.Error as db_error:
        return jsonify({"error": f"Database error: {str(db_error)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

# Controller for finetuning a model of a dataset
def create_user():
    try:
        # Get form data
        fullname = request.form.get('new_user_fullname')
        email = request.form.get('new_user_email')
        role = request.form.get('new_user_role')

        if not fullname or not email or not role:
            return jsonify({"error": "Full name, email, and role are required"}), 400

        # Default values for a new user
        default_password = secrets.token_hex(16)
        hashed_password = sha256(default_password.encode('utf-8')).hexdigest()
        is_admin = True if role.lower() == 'admin' else False

        # Insert the new user into the database
        with sqlite3.connect('toyota_analysis.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Users (fullname, email, password, isAdmin, apikey)
                VALUES (?, ?, ?, ?, ?)
                """,
                (fullname, email.lower(), hashed_password, is_admin, secrets.token_hex(16))
            )
            connection.commit()

        return jsonify({
            "message": f"User {fullname} successfully created",
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "The email address is already registered."}), 409
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

    ## AI Finetuning controller

    # Controller for handling file upload and fine-tuning
def upload():
    try:
        # Check if a file is part of the request
        if 'dataset' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['dataset']
        if file.filename == '':
            return jsonify({"error": "No file selected for uploading"}), 400

        # Get model and description from form data
        model = request.form.get('model')
        description = request.form.get('description')

        # Validate model type
        allowed_models = [
            "gpt-4o-mini-2024-07-18",
            "gpt-4o-2024-08-06",
            "gpt-3.5-turbo-0613"
        ]
        if model not in allowed_models:
            return jsonify({"error": "Invalid model type selected."}), 400

        # Save the uploaded file
        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)
        uploaded_file_path = os.path.join(upload_folder, file.filename)
        file.save(uploaded_file_path)

        # Filter the dataset for vehicles between 2021-2025
        filtered_csv_path = os.path.join(upload_folder, "vehicles_2021_2025.csv")
        filter_csv(uploaded_file_path, filtered_csv_path)

        # Convert filtered CSV to JSONL
        jsonl_file_path = os.path.join(upload_folder, "toyota_vehicle_details.jsonl")
        convert_csv_to_jsonl(filtered_csv_path, jsonl_file_path)

        # Upload JSONL to OpenAI for fine-tuning
        file_id = upload_training_file(jsonl_file_path)
        if not file_id:
            return jsonify({"error": "Failed to upload JSONL file for fine-tuning"}), 500

        # Create a fine-tuning job
        fine_tune_job_id = create_fine_tune_job(file_id, model)
        if not fine_tune_job_id:
            return jsonify({"error": "Failed to create fine-tuning job"}), 500

        # Monitor fine-tuning job
        return jsonify({
            "message": "Fine-tuning completed successfully",
            "model": model
        }), 200

    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


# Helper: Filter dataset
def filter_csv(input_csv, output_csv):
    data = pd.read_csv(input_csv)
    filtered_data = data[(data['year'] >= 2021) & (data['year'] <= 2025)]
    filtered_data.to_csv(output_csv, index=False)

# Helper: Convert CSV to JSONL
def convert_csv_to_jsonl(input_csv, output_jsonl):
    data = pd.read_csv(input_csv)
    with open(output_jsonl, "w") as jsonl_file:
        for _, row in data.iterrows():
            json_obj = {
                "messages": [
                    {"role": "user", "content": generate_prompt(row)},
                    {"role": "assistant", "content": generate_completion(row)}
                ]
            }
            jsonl_file.write(json.dumps(json_obj) + "\n")

def generate_prompt(row):
    return (
        f"What are the details of the {int(row['year'])} {row['make']} {row['model']}? "
        "Include fuel economy, engine specs, and class."
    )

def generate_completion(row):
    return (
        f"The {int(row['year'])} {row['make']} {row['model']} features a {row['cylinders']}-cylinder engine "
        f"with a displacement of {row['displ']} liters. It offers a combined fuel economy of {row['comb08']} MPG, "
        f"a city fuel economy of {row['city08']} MPG, and a highway fuel economy of {row['highway08']} MPG. "
        f"This vehicle uses {row['fuelType']} fuel and has a {row['drive']} drivetrain. "
        f"It belongs to the {row['VClass']} vehicle class."
    )

# Helper: Upload JSONL file to OpenAI
def upload_training_file(file_path):
    with open(file_path, "rb") as file:
        response = client.files.create(file=file, purpose="fine-tune")
    return response.id

# Helper: Create fine-tuning job
def create_fine_tune_job(file_id, model="gpt-4o-mini-2024-07-18"):
    response = client.fine_tuning.jobs.create(training_file=file_id, model=model)
    return response.id
