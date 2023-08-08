from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Genre(db.Model):
    __tablename__ = "genres"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)


    book = db.relationship('Book', back_populates='genre')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'books': [libro.to_dict() for libro in self.book]
        }
