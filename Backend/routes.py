from flask import Blueprint, request, jsonify
from functools import wraps
import sqlite3
from controllers import *
 
# Create a blueprint for routing
main_routes = Blueprint('main_routes', __name__)

# Authentication Decorator
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check for the API key in the headers
        api_key = request.headers.get('Authorization')
        if not api_key:
            return jsonify({"error": "Missing API Key"}), 401

        # Database connection and query
        connection = sqlite3.connect('toyota_analysis.db')
        cursor = connection.cursor()
        cursor.execute("SELECT email, apikey FROM users WHERE apikey = ?", (api_key,))
        user = cursor.fetchone()
        connection.close()

        # Constant-time comparison of API keys
        if not user or not hmac.compare_digest(user[1], api_key):
            return jsonify({"error": "Invalid API Key"}), 403

        # Attach user information to the request object
        request.user = user[0]
        return f(*args, **kwargs)
    
    return decorated_function

# Admin Check Decorator
def require_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('Authorization')
        if not api_key:
            return jsonify({"error": "Missing API Key"}), 401
        
        # Query the database for user details
        connection = sqlite3.connect('toyota_analysis.db')
        cursor = connection.cursor()
        cursor.execute("SELECT isAdmin FROM users WHERE apikey = ?", (api_key,))
        user = cursor.fetchone()
        connection.close()

        # Verifying the  Admin Status
        if not user[0]: # is_admin flag is 0 or false
            return jsonify({"error": "Admin privileges are required to access"}), 403
        
        # If admin then call the original function 'f'
        return f(*args, **kwargs)
    
    return decorated_function




#@require_api_key
# Define routes
@main_routes.route("/")
def home():
    return "healthy"

@main_routes.route("/admin", methods=["GET"])
@require_admin
def admin_only_route():
    return jsonify({"message": "Welcome, admin!"})


@main_routes.route("/sign-in", methods=["POST"])
def signin():
    try:
        # Access the JSON data sent in the POST request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        # Process the JSON data using your handler
        response = signin_handler(data)
        return response

    except Exception as e:
        #return jsonify({"error": "Internal Server Error"}), 500
        return jsonify({"error": str(e)}), 500

@main_routes.route("/data", methods=["GET"])
@require_api_key
def get_data():
    return get_all_data()

# Initialize routes to the app
def init_routes(app):
    app.register_blueprint(main_routes)
