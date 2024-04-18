from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, 
                     RadioField, SelectField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

### BASIC SETUP
app = Flask(__name__)
app.config['SECRET_KEY'] = "mykey"

### FORMS
class InfoForm(FlaskForm):
    breed = StringField(label="What breed are you?", # label of the field
                        validators=[DataRequired()]) # make app require this data while submitting
    neutered = BooleanField(label="Have you been neutered?")
    mood = RadioField(label="Please choose your mood:",
                      choices=[("mood_one", "Happy"), # tuple pairs, value and label, are being passed
                               ("mood_two", "Excited")])
    food_choice = SelectField(label=u"Pick your favourite food:", # to make it always in unicode
                              choices=[("chi", "Chicken"), # again, value (backend) and label (frontend)
                                       ("bf", "Beef"),
                                       ("fish", "Fish")])
    feedback = TextAreaField()
    submit = SubmitField("Submit")

### ROUTING
@app.route("/", methods=["GET", "POST"])
def index():
    form = InfoForm()
    if form.validate_on_submit():

        # Collect data from the form
        session["breed"] = form.breed.data
        session["neutered"] = form.neutered.data
        session["mood"] = form.mood.data
        session["food_choice"] = form.food_choice.data
        session["feedback"] = form.feedback.data

        # Data forwarded on submission
        return redirect(url_for("thankyou"))

    # That's what is seen at first visiting the given site    
    return render_template("index.html", form=form)

@app.route("/thankyou", methods=["GET", "POST"])
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)

