from flask import Flask, render_template, request

# defining the app main for this project
app = Flask(__name__)
port = 5000

#Configuracion para el modo debug al momento de iniciar el servidor
if __name__ == 'main':
    app.run(host='0.0.0.0', debug = True, port=port)

# This is the main view rute 
@app.route('/')
def home():
    return render_template('index.html')

# Login view
@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login_view.html')

# Register view
@app.route('/register')
def register():
    return render_template('register_view.html') 

# user view template after get login
@app.route('/user')
def user():
    return render_template('user_view.html')

# about page for more information of DiconMVE
@app.route('/about')
def about():
    return render_template('about_view.html')
