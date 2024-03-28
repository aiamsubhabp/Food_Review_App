from config import app, db, api
from flask import Flask, make_response, session, request, jsonify
from flask_migrate import Migrate
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from models import Customer, Restaurant, Review

class Customers(Resource):
  def get(self):
    customers = Customer.query.all()
    customers_dict = [customer.to_dict() for customer in customers]
    return customers_dict, 200
  
  def post(self):
    data = request.get_json()
    new_customer = Customer(
      username = data['username']
    )
    try:
      db.session.add(new_customer)
      db.session.commit()
      return (new_customer.to_dict(), 201)
    except:
      return ('Failed to create customer', 404)
    
api.add_resource(Customers, '/api/customers')

class Restaurants(Resource):
  def get(self):
    restaurants = Restaurant.query.all()
    resturants_dict = [restaurant.to_dict() for restaurant in restaurants]
    return resturants_dict, 200
  
  def post(self):
    data = request.get_json()
    new_restaurant = Restaurant(
      name = data['name'],
      cuisine_type = data['cuisine_type']
    )
    try:
      db.session.add(new_restaurant)
      db.session.commit()
      return (new_restaurant.to_dict(), 201)
    except:
      return ('Failed to create restaurant', 404)

api.add_resource(Restaurants, '/api/restaurants')

class Reviews(Resource):
  def get(self):
    reviews = Review.query.all()
    reviews_dict = [review.to_dict() for review in reviews]
    return reviews_dict, 200
  
  def post(self):
    data = request.get_json()
    new_review = Review(
      rating = data['rating'],
      review = data['review'],
      image = data['image'],
      customer_id = int(data['customer_id']),
      restaurant_id = int(data['restaurant_id'])
    )

    try:
      db.session.add(new_review)
      db.session.commit()
      return (new_review.to_dict(), 201)
    except:
      return ('Failed to create review', 404)
    
api.add_resource(Reviews, '/api/reviews')

class ReviewById(Resource):
  def get(self, id):
    review = Review.query.filter(Review.id == id).first()
    if not review:
      return ('Review not found, 404')
    
    review_dict = review.to_dict()

    return make_response(jsonify(review_dict), 200)
  
  def patch(self, id):
    review = Review.query.filter(Review.id == id).first()
    if not review:
      return ('Review not found', 404)
    
    try:
      data = request.get_json()
      for attr in data:
        setattr(review, attr, data[attr])
      db.session.add(review)
      db.session.commit()
      return make_response(review.to_dict(), 202)
    except:
      return ('Failed to update review', 400)
    
  def delete(self, id):
    review = Review.query.filter(Review.id == id).first()
    if not review:
      return ('Review not found', 404)
    db.session.delete(review)
    db.session.commit()
    return ('Review successfully deleted', 204)
  
api.add_resource(ReviewById, '/api/reviews/<int:id>')

if __name__ == "__main__":
  app.run(port=5555, debug=True)
