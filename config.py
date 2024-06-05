from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/postgres/dicomve'
app.config['SECRET_KEY'] = 'your_secret_key'  # Necesario para Flask-Login
db = SQLAlchemy(app)
