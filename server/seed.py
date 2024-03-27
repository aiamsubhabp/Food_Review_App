from config import app, db
from models import Customer, Review, Restaurant

if __name__ == "__main__":
  with app.app_context():
    print('Deleting all records...')
    Review.query.delete()
    Customer.query.delete()
    Restaurant.query.delete()

    print('Seeding in process...')

    c1 = Customer(username = 'Mario')
    c2 = Customer(username = 'Luigi')
    c3 = Customer(username = 'Bowser')

    db.session.add_all([c1, c2, c3])
    db.session.commit()

    r1 = Restaurant(name = 'Koopa Kitchen', cuisine_type = 'Bold and flavorful dishes with a hint of spiciness, inspired by Koopa Troopa culture.')
    r2 = Restaurant(name = 'Bowser BBQ', cuisine_type = 'Hearty barbecue dishes with a fiery kick, featuring grilled meats and savory sides.')
    r3 = Restaurant(name = 'Shy Guy Sushi', cuisine_type = 'Creative and artfully presented sushi rolls, sashimi, and Japanese-inspired small plates.')

    db.session.add_all([r1, r2, r3])
    db.session.commit()
    
    c1_r1 = Review(rating = 8, review = "Mamma mia! Koopa Kitchen serves up some spicy dishes that pack a punch! I loved the bold flavors and the hearty portions. Definitely worth a visit if you're looking for a flavorful meal.", customer = c1, restaurant = r1)
    c1_r2 = Review(rating = 7, review = "Bowser's BBQ Pit certainly brings the heat with its fiery barbecue dishes! While the flavors were bold, I found some of the meats to be a bit too charred for my taste. Still, a solid choice for barbecue lovers.", customer = c1, restaurant = r2)

    c2_r2 = Review(rating = 6, review = "Mama mia, Bowser's BBQ Pit was a bit too intense for me! The flavors were overpowering, and the atmosphere was a bit too hot for comfort. Not my first choice, but great if you're a fan of intense barbecue flavors.", customer = c2, restaurant = r2)
    c2_r3 = Review(rating = 8, review = "Shy Guy Sushi Bar offers a delightful sushi experience with its creative rolls and fresh ingredients. While the quality was good, I found some of the rolls to be a bit lacking in flavor. Still, a solid choice for sushi enthusiasts.", customer = c2, restaurant = r3)

    c3_r2 = Review(rating = 10, review = "Now that's what I'm talking about! Bowser's BBQ Pit is the ultimate barbecue destination, with smoky flavors and perfectly charred meats. It's fit for a king, or should I say, a Koopa King!", customer = c3, restaurant = r2)

    db.session.add_all([c1_r1, c1_r2, c2_r2, c2_r3, c3_r2])
    db.session.commit()

    print('Seeding complete!')


    
