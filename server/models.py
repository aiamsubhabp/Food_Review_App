from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

from config import db

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    serialize_rules = ('-reviews.customer',)

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)

    reviews = db.relationship('Review', back_populates = 'customer')

    def __repr__(self):
        return f'<Customer {self.id}, {self.username}>'

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-reviews.restaurant',)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    cuisine_type = db.Column(db.String)

    reviews = db.relationship('Review', back_populates = 'restaurant')

    def __repr__(self):
        return f'<Restaurant {self.id}, {self.name}, {self.cuisine_type}'


class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    serialize_rules = ('-customer.reviews', '-restaurant.reviews')

    id = db.Column(db.Integer, primary_key = True)
    rating = db.Column(db.Integer)
    review = db.Column(db.String)
    image = db.Column(db.String, default = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2048px-No_image_available.svg.png')

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))

    customer = db.relationship('Customer', back_populates = 'reviews')
    restaurant = db.relationship('Restaurant', back_populates = 'reviews')

    def __repr__(self):
        return f'<Review {self.id}, {self.rating}, {self.review}, {self.customer.username}, {self.restaurant.name}>'
    