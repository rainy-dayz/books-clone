from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,DateField
from wtforms.validators import DataRequired
from datetime import datetime


class ReviewForm(FlaskForm):
    comment = StringField('comment', validators=[DataRequired()])
    rating = IntegerField('rating', validators=[DataRequired()])
    user_id = IntegerField('user_id')
    book_id = IntegerField('book_id')
    created_at=DateField('Date')
