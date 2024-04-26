# puppycompanyblog/__init__.py
# IMPORTS
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# BLUEPRINT IMPORTS
from puppycompanyblog.core.views import core
from puppycompanyblog.users.views import users
from puppycompanyblog.error_pages.handlers import error_pages


# SETUP APP
app = Flask(__name__)

# DATABASE SETUP
basedir = os.path.abspath(os.path.dirname(__name__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir + 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# LOGIN CONFIG
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# SETUP BLUEPRINTS
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)