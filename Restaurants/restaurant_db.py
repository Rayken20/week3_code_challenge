# restaurant_db.py

import sqlite3

# Establish connection to the database
conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

# Create restaurants table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurants (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER
    );
''')

# Create customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    );
''')

# Create reviews table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        restaurant_id INTEGER,
        customer_id INTEGER,
        star_rating INTEGER,
        FOREIGN KEY(restaurant_id) REFERENCES restaurants(id),
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    );
''')

# Commit changes and close connection
conn.commit()
conn.close()
