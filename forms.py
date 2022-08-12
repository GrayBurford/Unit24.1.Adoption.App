"""WTForm classes for Pet Adoption Agency App"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional, NumberRange, URL, Length

# https://wtforms.readthedocs.io/en/2.3.x/validators/#built-in-validators
class AddNewPetForm(FlaskForm):
    name = StringField("Pet's Name", 
        validators=[InputRequired(message="Pet name can't be blank!")])
    species = SelectField("Species", 
        choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')],
        validators=[InputRequired(message="Species can't be blank!"), ])
    photo_url = StringField("Photo URL",
        validators=[Optional(), URL()])
    age = IntegerField("Age",
        validators=[InputRequired(), NumberRange(min=0, max=30, message="That's not a valid number!")])
    notes = TextAreaField("Notes about this pet",
        validators=[Optional(), Length(min=0, max=500)])

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL",
        validators=[Optional(), URL()])
    notes = TextAreaField("Notes about this pet",
        validators=[Optional(), Length(min=0, max=500)])
    available = BooleanField()