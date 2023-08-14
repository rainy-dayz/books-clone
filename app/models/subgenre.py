from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class SubGenre(db.Model):
    __tablename__ = "subgenres"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))


    book1 = db.relationship('Book', back_populates='subgenre')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'books': [libro.to_dict() for libro in self.book]
        }
