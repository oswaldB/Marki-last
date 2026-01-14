from flask import Blueprint, redirect, url_for, jsonify, render_template
from flask_login import login_required

app_bp = Blueprint('app', __name__)

@app_bp.route('/')
def index():
    return redirect(url_for('app.dashboard'))

@app_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app_bp.route('/hello')
def hello():
    return render_template('hello.html')

@app_bp.route('/api/user/info')
@login_required
def user_info():
    from app.models import User
    from flask_login import current_user

    user_data = {
        'username': current_user.username,
        'email': current_user.email,
        'isAdmin': current_user.is_admin
    }
    return jsonify({'user': user_data})