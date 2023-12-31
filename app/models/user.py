from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    reviews = db.relationship('Review', back_populates="user",cascade="all, delete-orphan")
    orders = db.relationship('Cart', back_populates="user", cascade="all, delete-orphan")
    wishlist = db.relationship('WishList', back_populates="user", cascade="all, delete-orphan")
    likes=db.relationship('Like',back_populates="users" )
    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'firstName':self.firstName,
            'lastName':self.lastName,
            'email': self.email,
            'hashed_password': self.hashed_password,
            'reviews': [review.to_dict() for review in self.reviews],
            'orders': [order.to_dict() for order in self.orders],
            'likes': [like.to_dict() for like in self.likes],
        }
