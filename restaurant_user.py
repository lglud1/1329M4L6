class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

# Creating an instance of Restaurant
restaurant = Restaurant("The Great Pizzaria", "Italian")
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Creating three different instances of Restaurant
restaurant1 = Restaurant("Burger King", "Fast Food")
restaurant2 = Restaurant("Sushi Palace", "Japanese")
restaurant3 = Restaurant("Taco Bell", "Mexican")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    
    def describe_user(self):
        print("User Information:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        # Add other attributes here
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

# Creating an instance of User
user1 = User("John", "Doe", 27, "john@example.com")
user1.describe_user()
user1.greet_user()