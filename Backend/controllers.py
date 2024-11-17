import hmac
from flask import jsonify
from hashlib import sha256
import sqlite3
import secrets
import base64
 

def signin_handler(data):

    MISSING_CREDENTIALS_ERROR = jsonify({"error": "Missing Email or Password"}), 401
    INVALID_CREDENTIALS_ERROR = jsonify({"error": "Incorrect Email or Password"}), 401

    # Validate the presence of 'email' and 'password' keys
    if not {'email', 'password'}.issubset(data):
        return MISSING_CREDENTIALS_ERROR

    email = data['email'].lower()
    password = sha256(data['password'].encode('utf-8')).hexdigest()

    # Database connection and query
    connection = sqlite3.connect('toyota_analysis.db')
    cursor = connection.cursor()
    cursor.execute("SELECT password FROM Users WHERE email = ?", (email,))
    databasepassword = cursor.fetchone()
    
    
    # Check if the user exists and if the password matches
    # Security: Uses hmac.compare_digest for constant-time string comparison to prevent timing attacks
    if not databasepassword or not hmac.compare_digest(databasepassword[0], password):
        return INVALID_CREDENTIALS_ERROR
    

    # Generate an API key as a session
    
    while True:
        token = secrets.token_bytes(32)
        # Encode as URL-safe base64 string
        api_key = base64.urlsafe_b64encode(token).decode('utf-8')
        cursor.execute("SELECT * FROM Users WHERE apikey = ?", (api_key,))
        if not cursor.fetchone():
            break

    
    cursor.execute("UPDATE users SET apikey = ? WHERE email = ?", (api_key, email))
    connection.commit()
    connection.close()
    
    # Returns an API key on successfull authentication
    return jsonify({"apikey": api_key})



def forgotpassword_handler(data):

    MISSING_EMAIL_ERROR = jsonify({"error": "Missing or Incorrect Email"}), 400

    # Validate the presence of 'email' and 'password' keys
    if not {'email'}.issubset(data):
        return MISSING_EMAIL_ERROR

    email = data['email'].lower()

    # TODO: No SMTP for now, will be implemented in production. Password changes can be done in the admin portal.

    # Returns an API key on successfull authentication
    return jsonify({"status": "success"})


def get_all_data():
    # Query the database for the data of the car
    connection = sqlite3.connect('toyota_analysis.db')
    cursor = connection.cursor()
    cursor.execute("SELECT year, city08, highway08 FROM Data")
    result = cursor.fetchone()
    connection.close()

    #print("Query result:", result)
    #print(f"Type of result: {type(result)}")
    
    if not result:
        return jsonify({"error": "No data found"}), 404

    
    # Convert result to list of dictionaries
    data = [{"year": result[0], "city08": result[1], "highway08": result[2]}]

    # Return the data in JSON format
    return jsonify({"data": data})


### Admin Controllers