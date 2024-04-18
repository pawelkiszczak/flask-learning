from basic import app, db, Puppy

with app.app_context():
    ## CREATE ##
    my_puppy = Puppy("Rufus", 5)
    db.session.add(my_puppy)
    db.session.commit()

    ## READ ##
    all_puppies = Puppy.query.all() # returns a list of Puppy objects in the table
    print(f"All: {all_puppies}")

    # SELECT BY ID #
    puppy_one = db.session.get(Puppy, 1)
    print(f"Puppy one: {puppy_one}")

    # FILTERS #
    puppy_frank = db.session.query(Puppy).filter_by(name="Frank").all()
    #puppy_frank.all()
    print(f"Frank: {puppy_frank}")

    ## UPDATE ##
    first_puppy = db.session.get(Puppy, 1)
    first_puppy.age = 10
    print(f"First puppy: {first_puppy}")
    db.session.add(first_puppy)
    db.session.commit()

    ## DELETE ##
    second_puppy = db.session.get(Puppy, 2)
    db.session.delete(second_puppy)
    db.session.commit()

    all_puppies = Puppy.query.all()
    print(f"All: {all_puppies}")