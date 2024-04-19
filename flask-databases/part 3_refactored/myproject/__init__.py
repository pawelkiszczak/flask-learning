# __init__.py
import os

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Application config
app = Flask(__name__,
            static_folder='/static')

basedir = os.path.abspath(os.path.dirname(__file__))
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'mykey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database config
db = SQLAlchemy(app)
Migrate(app, db)

# Blueprints config
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(puppies_blueprint, url_prefix='/puppies')
app.register_blueprint(owners_blueprint, url_prefix='/owners')
