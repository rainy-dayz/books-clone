from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

# Reviews
class Review(db.Model):
    __tablename__ = "reviews"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(2000), nullable=False)
    rating = db.Column(db.Numeric(precision=3, scale=2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    book_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("books.id")))

    # Relationships goes here
    user = db.relationship("User", back_populates='reviews')
    book = db.relationship("Book", back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'rating': self.rating,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'user': {
                'id': self.user.id,
                'firstName': self.user.first_name,
                'lastName': self.user.last_name,
            }
        }
