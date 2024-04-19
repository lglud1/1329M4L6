class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("The Great Pizzaria", "Italian")
print("Number of customers served initially:", restaurant.number_served)

restaurant.number_served = 100
print("Number of customers served after change:", restaurant.number_served)

restaurant.set_number_served(200)
print("Number of customers served after using set_number_served():", restaurant.number_served)

restaurant.increment_number_served(50)
print("Number of customers served after using increment_number_served():", restaurant.number_served)

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print("User Information:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("John", "Doe", 27, "john@example.com")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print("Login attempts before reset:", user.login_attempts)

user.reset_login_attempts()

print("Login attempts after reset:", user.login_attempts)
