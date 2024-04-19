# BASIC.py

# CREATE ENTRIES INTO THE TABLES

from models import app, db, Puppy, Toy, Owner

with app.app_context():
    # Creating 2 puppies
    rufus = Puppy('Rufus')
    fido = Puppy('Fido')

    # Add puppies to database
    db.session.add_all([rufus, fido])
    db.session.commit()

    # Check!
    print(Puppy.query.all())

    rufus = Puppy.query.filter_by(name="Rufus").first()
    print(rufus)

    # Create an Owner object
    jose = Owner('Jose', rufus.id)

    # Give Rufus some toys
    toy1 = Toy('Chew Toy', rufus.id)
    toy2 = Toy('Ball', rufus.id)

    db.session.add_all([jose, toy1, toy2])
    db.session.commit()

    # Grab Rufus again
    rufus = Puppy.query.filter_by(name='Rufus').first()
    print(rufus)
    rufus.report_toys()