from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Optional, URL
class AddNewPetForm(FlaskForm):
    """Form for adding a new pet."""

    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL', validators=[URL(require_tld=True, message='Invalid URL'), Optional()])
    age = IntegerField('Age', validators=[NumberRange(min=0, max=30, message='Age must be between 0 and 30')])
    notes = TextAreaField('Notes')
    available = BooleanField('Available', default=True)
