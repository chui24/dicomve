from flask import Flask, render_template

# defining the app main for this project
app = Flask(__name__)


# This is de main view rute 
@app.route('/')
def home():
    return render_template('home_view.html')

# Login view
@app.route('/login')
def login():
    return render_template('login_view.html')

# Register view
@app.route('/register')
def register():
    return render_template('register_view.html') 
