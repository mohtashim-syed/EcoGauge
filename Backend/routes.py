from flask import Blueprint, request, jsonify
from functools import wraps
import sqlite3
from controllers import *
from admin.routes import admin_app  # Import admin routes

# Create a blueprint for API routes
api_routes = Blueprint('api_routes', __name__, url_prefix="/")

# Authentication Decorator
def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('Authorization')
        if not api_key:
            return jsonify({"error": "Missing API Key"}), 401

        connection = sqlite3.connect('toyota_analysis.db')
        cursor = connection.cursor()
        cursor.execute("SELECT email, apikey FROM users WHERE apikey = ?", (api_key,))
        user = cursor.fetchone()
        connection.close()

        if not user:
            return jsonify({"error": "Invalid API Key"}), 403

        request.user = user[0]
        return f(*args, **kwargs)

    return decorated_function

# Define routes for API routes
@api_routes.route("/")
def home():
    return "healthy"

@api_routes.route("/forgot-password", methods=["POST"])
def resetpassword():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        response = forgotpassword_handler(data)
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_routes.route("/sign-in", methods=["POST"])
def signin():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        response = signin_handler(data)
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api_routes.route("/data", methods=["GET"])
@require_api_key
def get_data():
    return get_all_data()

# Initialize routes in the app
def init_routes(app):
    # Register blueprints with proper prefixes
    app.register_blueprint(api_routes, url_prefix="/api")  # Handles /api/*
    app.register_blueprint(admin_app, url_prefix="/admin")  # Handles /admin/*
