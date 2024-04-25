# app.py
import os
import json

# setup for local testing as OAuth is not meant to be working locally
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'

# Get client data
client_config_path = "/Users/pkiszczak/Desktop/courses/flask/flask-learning/flask-user-authentication/oauth-google.json"
with open(client_config_path, 'r') as f:
    CLIENT_DATA = json.load(f)

######
from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

# main focus in this section
blueprint = make_google_blueprint(client_id=CLIENT_DATA['web']['client_id'],
                                  client_secret=CLIENT_DATA['web']['client_secret'],
                                  offline=True,
                                  scope=['profile', 'email'])

app.register_blueprint(blueprint, 
                       url_prefix='/login')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    # RETURN ERROR INTERNAL SERVER IF NOT LOGGEND IN
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html', email=email)

@app.route('/login/google')
def login():
    # Check is user is already authorized with Google
    if not google.authorized:
        return render_template(url_for('google.login'))
    
    # Get the response from Google
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text

    # Retrieve email
    email = resp.json()['email']

    return render_template('welcome.html', email=email)

if __name__ == "__main__":
    #app.run(ssl_context=('cert.pem', 'key.pem'))
    app.run()