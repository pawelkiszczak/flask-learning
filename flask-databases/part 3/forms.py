# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of Puppy:")
    submit = SubmitField("Add Puppy")

class DelForm(FlaskForm):
    id = IntegerField("Id number of Puppy to remove:")
    submit = SubmitField("Remove Puppy")

class AddOwner(FlaskForm):
    name = StringField("Name of the Owner:")
    puppy_id = IntegerField("ID of Puppy:")
    submit = SubmitField("Add owner")
