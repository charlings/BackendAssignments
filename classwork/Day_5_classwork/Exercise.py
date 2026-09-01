import random

print("=" * 60)
print("9-1 / 9-2 / 9-4: Restaurant class")
print("=" * 60)


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # 9-4: default value

    def describe_restaurant(self):
        print(f"{self.restaurant_name} has {self.cuisine_type} in stock.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business today. Make your orders.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, amount):
        self.number_served += amount


# 9-1: single instance, print attributes, call both methods
restaurant = Restaurant("Ntachiosa", "Abacha")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-4: number_served
print(f"\nCustomers served so far: {restaurant.number_served}")
restaurant.number_served = 25
print(f"Customers served so far: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"After set_number_served(50): {restaurant.number_served}")

restaurant.increment_number_served(15)
print(f"After increment_number_served(15): {restaurant.number_served}")

# 9-2: three different instances
print("\n--- 9-2: Three Restaurants ---")
restaurant2 = Restaurant("Mama Put", "Jollof Rice")
restaurant3 = Restaurant("Chops & Grills", "Suya")
for r in (restaurant, restaurant2, restaurant3):
    r.describe_restaurant()


print("\n" + "=" * 60)
print("9-3 / 9-5: User class")
print("=" * 60)


class User:
    def __init__(self, first_name, last_name, state_of_origin="Enugu",
                 program_name="Hackathon 3.0"):
        self.first_name = first_name
        self.last_name = last_name
        self.marital_status = "single"
        self.state_of_origin = state_of_origin
        self.program_name = program_name
        self.login_attempts = 0  # 9-5

    def describe_user(self):
        print(f"\n{self.last_name} {self.first_name} is {self.marital_status}, "
              f"and is from {self.state_of_origin} and is actively participating "
              f"in the {self.program_name} software development program.")

    def greet_user(self):
        print(f"\nGood day {self.last_name} {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# 9-3: several instances, call both methods
user1 = User("David", "Onunkakwu")
user2 = User("Loveth", "Onukwube", state_of_origin="Anambra")
user3 = User("Chidera", "Nwosu", state_of_origin="Imo")

for u in (user1, user2, user3):
    u.describe_user()
    u.greet_user()

# 9-5: login attempts
print("\n--- 9-5: Login Attempts ---")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts for {user1.first_name}: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")


print("\n" + "=" * 60)
print("9-6: Ice Cream Stand (inherits Restaurant)")
print("=" * 60)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Butterscotch"]

    def display_flavors(self):
        print(f"Our beautiful flavors are {self.flavors}")


pure_ice = IceCreamStand("Ntachiosa", "Abacha")
pure_ice.display_flavors()


print("\n" + "=" * 60)
print("9-7 / 9-8: Admin and Privileges (inherits User)")
print("=" * 60)


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.admin_privileges = Privileges()  # 9-8: Privileges as an attribute

    def show_privileges(self):
        # convenience passthrough so Admin can also call it directly
        self.admin_privileges.show_privileges()


new_admin = Admin("David", "Onunkakwu")
print(new_admin.first_name)
new_admin.admin_privileges.show_privileges()
new_admin.show_privileges()


print("\n" + "=" * 60)
print("9-9: Battery Upgrade (Electric Car)")
print("=" * 60)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range_value = 150
        elif self.battery_size == 65:
            range_value = 225
        else:
            range_value = None

        if range_value:
            print(f"This car can go about {range_value} miles on a full charge.")
        else:
            print("Unknown battery size; cannot calculate range.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar("tesla", "model s", 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


print("\n" + "=" * 60)
print("9-13: Dice")
print("=" * 60)


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


d6 = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    d6.roll_die()

d10 = Die(10)
print("\nRolling a 10-sided die 10 times:")
for _ in range(10):
    d10.roll_die()

d20 = Die(20)
print("\nRolling a 20-sided die 10 times:")
for _ in range(10):
    d20.roll_die()


print("\n" + "=" * 60)
print("9-14: Lottery")
print("=" * 60)

lottery_pool = list(range(1, 11)) + ['A', 'B', 'C', 'D', 'E']
winning_numbers = random.sample(lottery_pool, 4)
print(f"Winning combination: {winning_numbers}")
print(f"If your ticket matches these 4 numbers/letters: {winning_numbers}, you win!")


print("\n" + "=" * 60)
print("9-15: Lottery Analysis")
print("=" * 60)

my_ticket = [3, 7, 'B', 9]
tries = 0
while True:
    tries += 1
    draw = random.sample(lottery_pool, 4)
    if set(draw) == set(my_ticket):
        break

print(f"My ticket: {my_ticket}")
print(f"It took {tries} tries to win with this ticket.")
