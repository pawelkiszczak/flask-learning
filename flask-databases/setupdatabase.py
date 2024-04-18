from basic import app, db, Puppy

# Creates all the tables
# REMEMBER TO USE WITH APP.APP_CONTEXT() AS IT IS MANDATORY
with app.app_context():
    db.create_all()

    sam = Puppy(name="Sammy", age=3)
    frank = Puppy(name="Frank", age=5)

    # Those should return none
    print(sam.id)
    print(frank.id)

    # Add ALL items to database
    db.session.add_all([sam, frank])

    # Commit the changes to the database
    db.session.commit()

    # Check again for ID
    print(sam.id)
    print(frank.id)

