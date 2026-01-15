from flask import Blueprint, render_template

bp = Blueprint('hello', __name__)

@bp.route('/')
def hello_world():
    return render_template('hello_world.html')