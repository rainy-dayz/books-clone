from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,DateField,BooleanField
from wtforms.validators import DataRequired
from datetime import datetime


class BookForm(FlaskForm):
    types = BooleanField('types', validators=[DataRequired()])
