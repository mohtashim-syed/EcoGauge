import jwt
import datetime
import secrets
from flask import Blueprint, render_template, request, jsonify, redirect, make_response
from functools import wraps
from admin.controllers import *

# JWT Configuration
SECRET_KEY = "secret"
TOKEN_EXPIRATION_MINUTES = 10

# Create a blueprint for admin routes
admin_app = Blueprint('admin_routes', __name__, url_prefix="/admin")

# Helper: Generate JWT
def generate_jwt(email):
    """Generate a JWT for the given email with an expiration time."""
    payload = {
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=TOKEN_EXPIRATION_MINUTES)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_jwt(token):
    """Decode and validate the provided JWT token."""
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

# Middleware: Protect Routes
def require_login(func):
    """Middleware to ensure the user is logged in using JWT."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get("auth_token")
        if not token:
            return redirect('/')  # Redirect to login if token is missing
        decoded_token = decode_jwt(token)
        if not decoded_token:
            return redirect('/')  # Redirect to login if token is invalid
        return func(decoded_token=decoded_token, *args, **kwargs)
    return wrapper

@admin_app.route('/')
def home():
    """Render the login page or redirect to dashboard if logged in."""
    token = request.cookies.get("auth_token")
    if token:
        decoded_token = decode_jwt(token)
        if decoded_token:
            return redirect('/dashboard')  # Redirect to dashboard if logged in
    return render_template('login.html')

@admin_app.route('/login', methods=['POST'])
def login():
    """Handle user login and generate a JWT upon successful authentication."""
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return "Missing Email or Password", 400

        # Authenticate user using the controller handler
        message, status_code = signin_handler(email, password)

        if status_code == 200:
            # Generate JWT
            token = generate_jwt(email)

            # Create response with token as a secure, HTTP-only cookie
            response = make_response(redirect('/dashboard'))
            response.set_cookie(
                "auth_token",
                token,
                httponly=True,
                secure=True,  # Use secure cookies only in production
                samesite='Lax',
                path="/"
            )
            return response

        return message, status_code
    except Exception as e:
        return f"Server Error: {str(e)}", 500

@admin_app.route('/dashboard')
@require_login
def dashboard(decoded_token):
    """Render the dashboard for the logged-in user."""
    try:
        user_email = decoded_token["email"]

        # Fetch all users
        with sqlite3.connect('toyota_analysis.db') as connection:
            connection.row_factory = sqlite3.Row  # Enable dictionary-like access
            cursor = connection.cursor()
            cursor.execute("SELECT fullname, email, isAdmin FROM Users")
            users = [dict(row) for row in cursor.fetchall()]

        # Fetch all trained models
        models = [
            {"name": "GPT-4 Custom", "type": "GPT-4", "file": "toyota_vehicle_details.jsonl"},
            {"name": "GPT-3.5 Turbo Model", "type": "GPT-3.5", "file": "toyota_vehicle_details.jsonl"}
        ]

        # Render the dashboard template with users and models
        return render_template('dashboard.html', email=user_email, users=users, models=models)

    except sqlite3.Error as db_error:
        print(f"Database error: {db_error}")
        return "Database error", 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Server error", 500


@admin_app.route('/logout', methods=['GET', 'POST'])
def logout():
    """Handle user logout by clearing the JWT cookie."""
    try:
        # Clear the token cookie
        response = make_response(redirect('/'))
        response.set_cookie("auth_token", '', expires=0, httponly=True, secure=True, path="/")
        return response
    except Exception as e:
        print(f"Error during logout: {e}")  # Log any errors for debugging
        return "Server Error: Unable to log out", 500

@admin_app.route('/reset-password', methods=['POST'])
@require_login
def handle_reset_password(decoded_token):
    """Reset the user's password."""
    return reset_user_password()

@admin_app.route('/create-user', methods=['POST'])
@require_login
def handle_create_user(decoded_token):
    """Create a new user."""
    return create_user()

@admin_app.route('/upload', methods=['POST'])
@require_login
def handle_upload(decoded_token):
    """Handle the file upload and trigger fine-tuning."""
    return upload()

@admin_app.route('/delete-user', methods=['POST'])
@require_login
def handle_delete_user(decoded_token):
    """Delete a user."""
    return delete_user()