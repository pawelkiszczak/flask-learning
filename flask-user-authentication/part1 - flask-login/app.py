# app.py
from myproject import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from myproject.models import User, Motto
from myproject.forms import LoginForm, RegistrationForm
from wtforms import ValidationError
from myproject.utils.oaiClient import MottoGenerator

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
                flash('User already exsists')
                return redirect(url_for('home'))
    
    return render_template('register.html', form=form)

@app.route('/get_motto', methods=["GET", "POST"])
@login_required
def get_motto():
    
    ### POST
    if request.method == "POST":
        mg = MottoGenerator()
        generated_motto = mg.generate(current_user.username)
        #motto = "testowe motto"

        motto = Motto(
            motto_text=generated_motto,
            user_id=current_user.id)
        db.session.add(motto)
        db.session.commit()

        return render_template('get_motto.html', generated_motto=generated_motto)   

    ### GET
    return render_template('get_motto.html') 

@app.route('/motto_list')
@login_required
def motto_list():
    motto_list = Motto.query.filter_by(user_id=current_user.id).all()
    return render_template('motto_list.html', motto_list=motto_list)  

@app.route('/motto_list/<int:motto_id>', methods=["POST"])
@login_required
def delete_motto(motto_id):
    # Deleting from db
    motto_to_delete = Motto.query.filter_by(motto_id=motto_id).first()
    db.session.delete(motto_to_delete)
    db.session.commit()
    return redirect(url_for('motto_list'))

if __name__ == "__main__":
    app.run(debug=True)

