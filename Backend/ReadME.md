
# WGSI: Toyota Analysis Platform

WGSI is a Flask-based backend application for managing Toyota vehicle analysis data, integrating advanced tools like OpenAI for insights. It supports secure user authentication and data management with a SQLite database.

## Features
- **Authentication**: Secure login system with JWT.
- **Data Analysis**: Utilizes Pandas for insights.
- **Database**: Manages analysis data using SQLite.
- **API Integration**: Supports OpenAI integration for AI-driven features.

---

## Project Structure
```
wgsi/
├── wgsi.py                # Application entry point
├── app.py                 # Flask app factory
├── controllers.py         # Handles core logic and APIs
├── main.py                # App initializer
├── routes.py              # Route definitions
├── toyota_analysis.db     # SQLite database
├── admin/                 # Admin-specific logic
│   ├── controllers.py     # Admin controllers
│   └── routes.py          # Admin routes
├── static/                # Static assets (CSS, fonts, images)
├── templates/             # HTML templates
└── .env                   # Environment variables (to be created)
```

---

## Installation and Setup

### Prerequisites
- Python 3.9+
- `pip` for package management
- SQLite (optional, if not bundled with Python)

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/wgsi.git
cd wgsi
```

### Step 2: Install Dependencies
Create a virtual environment and install the required Python packages.
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables
Create a `.env` file in the root directory with the following:
```
OPENAI_API_KEY=your_openai_api_key
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///toyota_analysis.db
```

---

## Usage

### Step 1: Initialize the Database
Run the following to set up the database:
```bash
flask db init
flask db migrate
flask db upgrade
```

### Step 2: Run the Application
Start the Flask development server:
```bash
flask run
```
By default, the app will be available at `http://127.0.0.1:5000`.

---

## Deployment
For production deployment:
1. Use a production-ready server (e.g., Gunicorn).
2. Set up environment variables securely.
3. Use a reverse proxy (e.g., Nginx).

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## Contact
For questions or support, please contact `your-email@example.com`.
