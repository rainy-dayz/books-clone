from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Order(db.Model):
    __tablename__ = 'orders'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    created_at=db.Column(db.Date)


    # Relationships go here
    user = db.relationship("User", back_populates="orders")
    orderitem=db.relationship("OrderItem", back_populates="order")
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'created_at':self.created_at
        }
