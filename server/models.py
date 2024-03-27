from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

from config import db

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)

    reviews = db.relationship('Review', back_populates = 'customer')

    def __repr__(self):
        return f'<Customer {self.id}, {self.username}>'

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    cuisine_type = db.Column(db.String)

    reviews = db.relationship('Review', back_populates = 'restaurant')

    def __repr__(self):
        return f'<Restaurant {self.id}, {self.name}, {self.cuisine_type}'


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key = True)
    rating = db.Column(db.Integer)
    review = db.Column(db.String)
    image = db.Column(db.String, nullable = True)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    customer = db.relationship('Customer', back_populates = 'reviews')
    restaurant = db.relationship('Restaurant', back_populates = 'reviews')

    def __repr__(self):
        return f'<Review {self.id}, {self.rating}, {self.review}, {self.customer.username}, {self.restaurant.name}>'
    