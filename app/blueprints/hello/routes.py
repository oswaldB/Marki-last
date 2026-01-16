# Blueprint: Hello World
from flask import Blueprint, render_template

bp = Blueprint('hello', __name__)

@bp.route('/')
def hello_world():
    """
    Affiche une page simple avec le texte "Hello World".
    Inclut le logo Marki.
    """
    return render_template('hello_world.html')