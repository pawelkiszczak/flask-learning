from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask (__name__)

# Setting up a secret in naive way
# Better ways in further lessons
app.config['SECRET_KEY'] = "mysecretkey"

# Create a WTForm class, inherit from FlaskForm
class InfoForm(FlaskForm):
    breed = StringField("What breed are you?")
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def index():
    # Necessary, will see later
    breed = False

    # Create instance of a InfoForm created above
    form = InfoForm()

    # Check for submission of the form
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ""

    # Return a template with data
    return render_template('index.html', form=form, breed=breed)

if __name__ == "__main__":
    app.run(debug=True)