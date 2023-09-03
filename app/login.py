import requests
from flask import Blueprint, Response, request, jsonify
from flask import Blueprint, render_template
from utils.scrape_products import scrape_products

from flask import Flask, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


login_bp = Blueprint('login', __name__)
app = Flask(__name__)
login_manager = LoginManager(app)

login_manager.login_view = 'login'  # Specify the view function name for the login page
login_manager.login_message_category = 'info'  # Customize the login message category (optional)


@login_manager.user_loader
def load_user(user_id):
    # Load the user from your data source (e.g., database) based on the user_id
    # Return the User object or None if the user does not exist
    return User(user_id)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']

        # Perform login logic here
        # Verify username and password against your data source (e.g., database)

        if username == 'valid_username' and password == 'valid_password':
            user = User(username)
            login_user(user)  # Log in the user

            return redirect(url_for('login_success'))  # Redirect to the login success page

        else:
            # Invalid credentials, display an error message
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/login_success')
@login_required  # Restrict access to logged-in users only
def login_success():
    return render_template('loginsuccess.html')

