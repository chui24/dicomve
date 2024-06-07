from flask import Flask, render_template, request,  redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import db
from models.models import UserConnection, User
from datetime import datetime



# defining the app main for this project
port = 5000
app = Flask(__name__)

#Static folder route

app.static_folder = 'static'  

#Web app secret key (Need to change)

app.secret_key = '123456789' 

login_manager = LoginManager()

#Configuracion para el modo debug al momento de iniciar el servidor
if __name__ == 'main':
    app.run(host='0.0.0.0', debug = True, port=port)



# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



#---General routes---
@login_manager.user_loader
def load_user(id):
    return User(id) 


# This is the main view rute 
@app.route('/')
def home():
    return render_template('index.html')

# Login view
@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login_view.html')

# Register view
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))
        data = {
            'username': username,
            'email': email,
            'password': password
        }

        connection = UserConnection(db)
        connection.write_user(data)


        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register_view.html')


# user view template after get login
@app.route('/user')
def user():
    return render_template('user_view.html')

# about page for more information of DiconMVE
@app.route('/about')
def about():
    return render_template('about_view.html')
