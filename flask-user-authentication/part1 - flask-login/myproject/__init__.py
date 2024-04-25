# __init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Instentiate login manager and the app itself
login_manager = LoginManager()
app = Flask(__name__)

# Basic configuration of app and database
app.config['SECRET_KEY'] = 'mykey'
basedir = os.path.abspath(os.path.dirname(__name__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Link the app with database
db = SQLAlchemy(app)
Migrate(app, db)

# Link the app with LoginManager
login_manager.init_app(app)
# Where LoginManager should redirect (to which view)
login_manager.login_view = 'login'