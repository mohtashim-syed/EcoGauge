from flask import Flask
from routes import init_routes
import secrets 

def create_app():
    app = Flask(__name__)
    app.secret_key = 'aaaa'    
    init_routes(app)
    return app
