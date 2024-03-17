# customer.py

import sqlite3
import restaurant_db
from Review import Review
from Restaurant import Restaurant

class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """Returns the full name of the customer, with the first name and the last name concatenated, Western style."""
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        """
        Returns the restaurant instance that has the highest star rating from this customer.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT restaurants.* FROM restaurants
            JOIN reviews ON restaurants.id = reviews.restaurant_id
            WHERE reviews.customer_id=?
            ORDER BY reviews.star_rating DESC
            LIMIT 1
        """, (self.id,))
        restaurant_data = cursor.fetchone()
        conn.close()
        if restaurant_data:
            return Restaurant(*restaurant_data)
        else:
            return None

    def add_review(self, restaurant, rating):
        """
        Creates a new review for the restaurant with the given `restaurant_id`.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reviews (restaurant_id, customer_id, star_rating)
            VALUES (?, ?, ?)
        """, (restaurant.id, self.id, rating))
        conn.commit()
        conn.close()

    def delete_reviews(self, restaurant):
        """
        Removes all reviews for the given restaurant.
        """
        conn = sqlite3.connect('restaurant.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM reviews
            WHERE restaurant_id=? AND customer_id=?
        """, (restaurant.id, self.id))
        conn.commit()
        conn.close()
