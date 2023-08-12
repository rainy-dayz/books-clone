from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Book(db.Model):
    __tablename__ = 'books'

    if environment == "production":
       __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(200),nullable=False)
    author= db.Column(db.String(200),nullable=False)
    price = db.Column(db.Numeric(precision=5, scale=2),nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    genre_id=db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("genres.id")))
    book_image=db.Column(db.String(255), nullable=False)
    types=db.Column(db.Boolean, nullable=False)
    releaseDate=db.Column(db.Date)

    genre = db.relationship('Genre', back_populates='book')
    orders1= db.relationship('Cart',back_populates="book1",cascade="all, delete-orphan")
    reviews = db.relationship('Review', back_populates='book', cascade="all, delete-orphan")
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'author':self.author,
            'price': self.price,
            'description': self.description,
            'genre_id':self.genre_id,
            'book_image':self.book_image,
            'types':self.types,
            'releaseDate':self.releaseDate,
            'reviews': [review.to_dict() for review in self.reviews],
            'avgRating': self.avgRating
        }

    @property
    def avgRating(self):
        if not self.reviews:
            return None
        total = sum(review.rating for review in self.reviews)
        return total / len(self.reviews) if len(self.reviews) > 0 else None
