# MODELS.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

# Setup app
app = Flask(__name__)

# App config
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect db to SQLAlchemy
db = SQLAlchemy(app)

# Connect app and database for Migration
Migrate(app, db)

class Puppy(db.Model):
    __tablename__ = "puppies"

    id = db.Column(db.Integer, 
                   primary_key=True)
    name = db.Column(db.Text)

    # ONE TO MANY - puppy to many toys
    toys = db.relationship('Toy', # connecting to other Model -> Toy 
                           backref='Puppy', # add backreference to remember that Toy is connected to Puppy
                           lazy='dynamic') # how the related items to be loaded
    
    # ONE TO ONE -> one Puppy to one Owner
    owner = db.relationship('Owner',
                            backref="Puppy",
                            uselist=False) # exepecting one result to be returned
        
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet!"
        
    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.item_name)
    

class Toy(db.Model):
    __tablename__ = "toys"

    id = db.Column(db.Integer, 
                   primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, 
                         db.ForeignKey('puppies.id'))
    
    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id
    

class Owner(db.Model):
    __tablename__ = "owners"
    
    id = db.Column(db.Integer, 
                   primary_key=True)
    name = db.Column(db.Text)

    puppy_id = db.Column(db.Integer, 
                         db.ForeignKey('puppies.id'))
    
    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id