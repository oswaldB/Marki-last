from flask import render_template
from . import hello_bp

@hello_bp.route('/hello')
def hello():
    return render_template('hello.html')