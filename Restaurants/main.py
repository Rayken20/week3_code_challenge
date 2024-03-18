from Customer import Customer
from Restaurant import Restaurant
from Review import Review

def main():
    try:
        # Create some sample data to test
        customer1 = Customer(1, "Rachael", "NJoki")
        customer2 = Customer(2, "Peter", "Macharia")

        restaurant1 = Restaurant(1, "Pepinos 1", 50)
        restaurant2 = Restaurant(2, "Wa Kalucy 2", 60)

        review1 = Review(1, 1, 1, 5)
        review2 = Review(2, 2, 1, 4)
        review3 = Review(3, 1, 2, 3)

        # Testing methods for Customer
        print("Testing methods for Customer:")
        print("Full Name of Customer 1:", customer1.full_name())
        print("Full Name of Customer 2:", customer2.full_name())
        print("Favorite Restaurant of Customer 1:", customer1.favorite_restaurant().name)
        print("Favorite Restaurant of Customer 2:", customer2.favorite_restaurant().name)

        # Adding a new review for a restaurant by a customer
        customer1.add_review(restaurant1, 4)

        # Displaying all reviews for a restaurant
        print("All Reviews for Restaurant 1:")
        for review in restaurant1.all_reviews():
            print(review)

        # Deleting all reviews for a restaurant by a customer
        customer1.delete_reviews(restaurant1)

        # Displaying all reviews for a restaurant again to confirm deletion
        print("All Reviews for Restaurant 1 (after deletion):")
        for review in restaurant1.all_reviews():
            print(review)

        # Testing methods for Review
        print("\nTesting methods for Review:")
        print("Full Review:", review1.full_review())

        # Testing methods for Restaurant
        print("\nTesting methods for Restaurant:")
        print("Fanciest Restaurant:", Restaurant.fanciest().name)
    
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
