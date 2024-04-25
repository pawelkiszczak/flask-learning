# app.py
from myproject import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user, current_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm
from wtforms import ValidationError
import logging

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome_user')
@login_required # this decorator makes sure that user can see the view after being logged in
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've logged out")
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully!")

            # If a user was trying to access a page that requires to be logged in
            # we can redirect him there after a successful login operation

            # 'next' holds the page that user had requested
            next = request.args.get('next')

            # if it's None or empty, we simply redirect him to greeting after login
            if next == None or not next[0] =='/':
                next = url_for('welcome_user')

            # if next was not None nor empty, we can redirect him to desired view
            return redirect(next)
        
    return render_template('login.html', form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data)
            
            print(user.email, user.username, user.password_hash)

            try:
                if form.check_email(form.email) and form.check_username(form.username):
                    db.session.add(user)
                    db.session.commit()
                    flash('Thanks for the registration', "success")
                    return redirect(url_for('login'))
                
            except ValidationError:
                return redirect(url_for('home'))
    
    return render_template('register.html', form=form)

@app.route('/test', methods=["GET", "POST"])
def test():
    
    ### POST
    if request.method == "POST":
        pass    

    ### GET
    # get current user's username
    username = current_user.username
    user_data = User.query.filter_by(username=username)

    return render_template('test.html', user_data=user_data)    

if __name__ == "__main__":
    app.run(debug=True)

