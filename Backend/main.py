from flask import Flask
from routes import init_routes
import secrets 
if __name__ == "__main__":
    app = Flask(__name__)
    app.secret_key = 'aaaa'    
    init_routes(app)
    app.run(debug=True, port=8000)
