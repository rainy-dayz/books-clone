from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,DateField
from wtforms.validators import DataRequired, Email, ValidationError
from datetime import datetime



class CartForm(FlaskForm):
    user_id=IntegerField('User ID')
    book_id=IntegerField('Book ID')
    quantity=IntegerField('quantity')
    created_at=DateField('Date', format='%Y-%m-%d', default=datetime.now().strftime("%Y-%m-%d"))
