from flask import Blueprint

hello_bp = Blueprint('hello', __name__, template_folder='templates')

from . import routes