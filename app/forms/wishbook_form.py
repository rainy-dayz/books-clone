from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,DateField
from wtforms.validators import DataRequired, Email, ValidationError
from datetime import datetime



class WishBookForm(FlaskForm):
    user_id=IntegerField('User ID')
    book_id=IntegerField('Book ID')

