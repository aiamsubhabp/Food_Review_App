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
  
api.add_resource(Customers, '/api/customers')

class Restaurants(Resource):
  def get(self):
    restaurants = Restaurant.query.all()
    resturants_dict = [restaurant.to_dict() for restaurant in restaurants]
    return resturants_dict, 200

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

if __name__ == "__main__":
  app.run(port=5555, debug=True)
