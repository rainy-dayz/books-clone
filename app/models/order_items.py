from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class OrderItem(db.Model):
    __tablename__ = 'orderItems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("orders.id")), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("books.id")), nullable=False)
    quantity= db.Column(db.Integer)


    # Relationships go here
    order = db.relationship("Order", back_populates="orderitem")
    book1= db.relationship('Book',back_populates="orders1")

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'book_id': self.book_id,
            'quantity': self.quantity
        }
