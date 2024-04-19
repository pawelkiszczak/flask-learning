# views.py @ puppies
from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.puppies.forms import AddForm, DelForm
from myproject.models import Puppy

puppies_blueprint = Blueprint('puppies', __name__,
                              template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        # Geet the puppy name from the form
        name = form.name.data
        # Get the object
        new_pup = Puppy(name)
        # Add it to the database
        db.session.add(new_pup)
        db.session.commit()
        # Redirect to list.html to check if it was added
        return redirect(url_for('puppies.list'))
    
    return render_template('add.html', form=form)

@puppies_blueprint.route('/list')
def list():
    # Retrieve all of the puppies
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@puppies_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():    
    form = DelForm()

    if form.validate_on_submit():
        # Geet the puppy data
        id = form.id.data
        pup = Puppy.query.get(id)
        # Delete puppy from database
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    
    return render_template('delete.html', form=form)