"""Application for Pet Adoption Agency"""

from flask import Flask, render_template, redirect, request, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddNewPetForm, EditPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///adopt'

# Set this to false or SQLAlchemy will yell at you
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Print all SQL statements to the terminal (helpful for debugging)
app.config['SQLALCHEMY_ECHO']  = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "ABC123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/', methods=["GET"])
def display_home_page():
    """Render home page with list of all pets"""

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def handle_add_pet_form():
    """Render new pet form (GET) or handles new pet form submittion (POST)."""

    form = AddNewPetForm()

    # Run this if coming from form POST request
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added new pet, whose is a {age} year old {species} named {name}!")
        return redirect('/') 

    # else, render form template (GET request)       
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET'])
def display_pet_info(pet_id):
    """Render basic info on a specific pet."""

    pet = Pet.query.get_or_404(pet_id)

    pet.photo_url = pet.image_url()
    return render_template('display_pet_info.html', pet=pet)
    # info = {'name' : pet.name, 'age' : pet.age, 'species' : pet.species, 'notes' : pet.notes}
    # return jsonify(info)

@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def handle_edit_pet_form(pet_id):
    """Render edit pet form (GET) or handle edit pet form submission (POST)"""

    form = EditPetForm()
    pet = Pet.query.get_or_404(pet_id)
    pet.photo_url = pet.image_url()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()

        flash(f'Edited info for {pet.name}')
        return redirect('/')
    
    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)

    