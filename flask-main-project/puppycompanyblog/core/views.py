# core/views.py

# IMPORTS
from flask import render_template, request, Blueprint

# BLUEPRINT SETUP
core = Blueprint('core', __name__)

# ROUTES
@core.route('/')
def index():
    return render_template('index.html')

@core.route('/info')
def info():
    return render_template('info.html')