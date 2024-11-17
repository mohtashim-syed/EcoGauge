from flask import Flask
from routes import init_routes

if __name__ == "__main__":
    app = Flask(__name__)
    init_routes(app)
    app.run(debug=True)
