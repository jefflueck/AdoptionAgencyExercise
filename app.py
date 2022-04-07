from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddNewPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# the toolbar is only enabled in debug mode:
app.debug = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'The secret key'
toolbar = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def list_all_pets():
    """Show all pets."""

    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """Show form for adding a pet."""
    form = AddNewPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_pet.html', form=form)

@app.route('/pet/<int:pet_id>', methods=['GET', 'POST'])
def see_details(pet_id):
    """Show details of a pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = AddNewPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_details.html', pet=pet, form=form)


