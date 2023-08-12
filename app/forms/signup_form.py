from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User
import re


def is_valid(form, field):
    el = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email = field.data
    if not re.match(el, email):
        raise ValidationError('Invalid email address.')

def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')

def long_enough(form, field):
    username=field.data
    if len(username) <2 or len(username) > 32:
        raise ValidationError("Must be 2-32 characters long")

def long_enough_firstName(form, field):
    firstName=field.data
    if len(firstName) <2 :
        raise ValidationError("Must be at least 2 characters long")

def long_enough_lastName(form, field):
    lastName=field.data
    if len(lastName) <2 :
        raise ValidationError("Must be at least 2 characters long")

def username_exists(form, field):
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')
def password_enough(form,field):
    password=field.data
    if len(password)<8:
        raise ValidationError("Must be at least 8 characters long")


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists,long_enough])
    email = StringField('email', validators=[DataRequired(), user_exists, is_valid])
    firstName = StringField('firstName', validators=[DataRequired(),long_enough_firstName])
    lastName = StringField('lastName', validators=[DataRequired(),long_enough_lastName])
    password = StringField('password', validators=[DataRequired(),password_enough])
