"""restaurant_module.py - module containing the Restaurant class (9-10)"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type} in stock.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business today. Make your orders.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, amount):
        self.number_served += amount
