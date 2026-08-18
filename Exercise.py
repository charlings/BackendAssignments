guests = ["Austine", "Stephanie", "Lilian"]
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")

# 3-5. Changing Guest List
print("\n--- Update: One guest can't make it ---")
unable_to_attend = guests[1]  # Austine can't make it
print(f"Unfortunately, {unable_to_attend} can't make it.")
guests[1] = "Kosi"
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")

# 3-6. More Guests
print("\n--- Good news: Found a bigger table! ---")
guests.insert(0, "Bonaventure")   # Beginning
guests.insert(2, "Davoski")        # Middle
guests.append("Loveth")          # End
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")

# 3-7. Shrinking List
print("\n--- Bad news: Only two seats available ---")
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, Just rest, no jolof for you again.")

# Final two guests
for guest in guests:
    print(f"{guest}, you are still invited!")

# Empty the list
del guests[:]
print("\nFinal guest list:", guests)  # Should be []


# Pg 113

# 3-8. Seeing the World
places = ["Enugu", "Awgu", "Nsukka", "Mgbowo", "Ikeja"]
print("Original list:", places)

print("Alphabetical order:", sorted(places))
print("Still original:", places)

print("Reverse alphabetical order:", sorted(places, reverse=True))
print("Still original:", places)

places.reverse()
print("Reversed order:", places)

places.reverse()
print("Back to original:", places)

places.sort()
print("Sorted alphabetically:", places)

places.sort(reverse=True)
print("Sorted reverse-alphabetically:", places)


# 3-9. Dinner Guests
guests = ["Austine", "Stephanie", "James"]
print(f"\nI am inviting {len(guests)} people to dinner.")


# 3-10. Every Function
items = ["River Niger", "River Benue", "Nigeria", "Lagos", "English"]

print("\nOriginal items:", items)

# Accessing elements
print("First item:", items[0])
print("Last item:", items[-1])

# Modifying elements
items[1] = "River Benue"
print("Modified list:", items)

# Adding elements
items.append("French")
print("After append:", items)

items.insert(2, "River Cross")
print("After insert:", items)

# Removing elements
removed = items.pop()
print(f"Popped item: {removed}")
print("After pop:", items)

del items[0]
print("After del:", items)

items.remove("River Cross")
print("After remove:", items)

# Sorting and reversing
print("Sorted:", sorted(items))
items.sort()
print("List sorted permanently:", items)

items.reverse()
print("List reversed:", items)

# Length
print("Length of list:", len(items))


# Pg 134

# 4-3. Counting to Twenty
print("\n--- 4-3 Counting to Twenty ---")
for number in range(1, 21):
    print(number)

# 4-4. One Million
print("\n--- 4-4 One Million ---")

numbers = list(range(1, 1000001))
print("List created with 1 to 1,000,000.")

# 4-5. Summing a Million
print("\n--- 4-5 Summing a Million ---")
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))

# 4-6. Odd Numbers
print("\n--- 4-6 Odd Numbers ---")
odds = list(range(1, 21, 2))
for odd in odds:
    print(odd)

# 4-7. Threes
print("\n--- 4-7 Threes ---")
threes = list(range(3, 31, 3))
for three in threes:
    print(three)

# 4-8. Cubes
print("\n--- 4-8 Cubes ---")
cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)
for cube in cubes:
    print(cube)

# 4-9. Cube Comprehension
print("\n--- 4-9 Cube Comprehension ---")
cubes_comp = [num ** 3 for num in range(1, 11)]
print(cubes_comp)

# Pg 141

# 4-10. Slices
print("\n--- 4-10 Slices ---")
foods = ["rice", "beans", "yam", "bread", "meat", "fish", "egg"]
print("Original list:", foods)

print("The first three items in the list are:", foods[:3])
print("Three items from the middle of the list are:", foods[2:5])
print("The last three items in the list are:", foods[-3:])

# 4-11. My Pizzas, Your Pizzas
print("\n--- 4-11 My Pizzas, Your Pizzas ---")
pizzas = ["pepperoni", "margherita", "bbq chicken"]
friend_pizzas = pizzas[:]  # Copy the list

# Add new pizzas
pizzas.append("veggie")
friend_pizzas.append("hawaiian")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12. More Loops
print("\n--- 4-12 More Loops ---")
foods = ["rice", "beans", "yam", "bread", "meat", "fish", "egg"]

print("Foods list:")
for food in foods:
    print(food)

desserts = ["cake", "ice cream", "pie", "pudding"]
print("\nDesserts list:")
for dessert in desserts:
    print(dessert)

# Pg 145

# Original buffet menu (tuple of 5 foods)
buffet = ("rice", "beans", "yam", "bread", "meat")

print("Original buffet menu:")
for food in buffet:
    print(food)

# Restaurant changes its menu (replace two items)
buffet = ("rice", "beans", "pasta", "salad", "chicken")

print("\nRevised buffet menu:")
for food in buffet:
    print(food)

# Pg 161

# 5-1. Conditional Tests
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

fruit = "apple"
print("\nIs fruit == 'apple'? I predict True.")
print(fruit == "apple")

print("\nIs fruit == 'banana'? I predict False.")
print(fruit == "banana")

age = 18
print("\nIs age >= 18? I predict True.")
print(age >= 18)

print("\nIs age < 18? I predict False.")
print(age < 18)

city = "Lagos"
print("\nIs city == 'Lagos'? I predict True.")
print(city == "Lagos")

print("\nIs city == 'Abuja'? I predict False.")
print(city == "Abuja")

number = 10
print("\nIs number == 10? I predict True.")
print(number == 10)

print("\nIs number != 10? I predict False.")
print(number != 10)


# 5-2. More Conditional Tests

# Equality and inequality with strings
name = "Charles"
print("\nIs name == 'Charles'? ->", name == "Charles")  # True
print("Is name != 'Charles'? ->", name != "Charles")    # False

# Using lower()
animal = "DOG"
print("\nIs animal.lower() == 'dog'? ->", animal.lower() == "dog")  # True
print("Is animal.lower() == 'cat'? ->", animal.lower() == "cat")    # False

# Numerical tests
num = 25
print("\nIs num == 25? ->", num == 25)        # True
print("Is num != 25? ->", num != 25)          # False
print("Is num > 20? ->", num > 20)            # True
print("Is num < 20? ->", num < 20)            # False
print("Is num >= 25? ->", num >= 25)          # True
print("Is num <= 24? ->", num <= 24)          # False

# Using and/or
print("\nIs num > 20 and num < 30? ->", num > 20 and num < 30)  # True
print("Is num > 30 or num == 25? ->", num > 30 or num == 25)    # True
print("Is num > 30 and num == 25? ->", num > 30 and num == 25)  # False

# Membership tests
colors = ["red", "blue", "green"]
print("\nIs 'red' in colors? ->", "red" in colors)        # True
print("Is 'yellow' in colors? ->", "yellow" in colors)    # False
print("Is 'yellow' not in colors? ->", "yellow" not in colors)  # True

# Pg 171

# 5-3. Alien Colors #1
print("\n--- 5-3 Alien Colors #1 ---")
alien_color = "green"
if alien_color == "green":
    print("Player just earned 5 points!")  # Passes

alien_color = "red"
if alien_color == "green":
    print("Player just earned 5 points!")  # Fails, no output


# 5-4. Alien Colors #2
print("\n--- 5-4 Alien Colors #2 ---")
alien_color = "green"
if alien_color == "green":
    print("Player just earned 5 points!")
else:
    print("Player just earned 10 points!")

alien_color = "yellow"
if alien_color == "green":
    print("Player just earned 5 points!")
else:
    print("Player just earned 10 points!")

# 5-5. Alien Colors #3
print("\n--- 5-5 Alien Colors #3 ---")
alien_color = "green"
if alien_color == "green":
    print("Player earned 5 points.")
elif alien_color == "yellow":
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

alien_color = "yellow"
if alien_color == "green":
    print("Player earned 5 points.")
elif alien_color == "yellow":
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

alien_color = "red"
if alien_color == "green":
    print("Player earned 5 points.")
elif alien_color == "yellow":
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

# 5-6. Stages of Life
print("\n--- 5-6 Stages of Life ---")
age = 34
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

# 5-7. Favorite Fruit
print("\n--- 5-7 Favorite Fruit ---")
favorite_fruits = ["banana", "mango", "apple"]

if "banana" in favorite_fruits:
    print("You really like bananas!")
if "mango" in favorite_fruits:
    print("You really like mangoes!")
if "apple" in favorite_fruits:
    print("You really like apples!")
if "orange" in favorite_fruits:
    print("You really like oranges!")
if "pineapple" in favorite_fruits:
    print("You really like pineapples!")

# Pg 177

# ================================
# Chapter 5 Exercises (5-8 to 5-11)
# ================================

# 5-8. Hello Admin
print("\n--- 5-8 Hello Admin ---")
usernames = ["admin", "Jaden", "Sophia", "Charles", "Maya"]
for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

# 5-9. No Users
print("\n--- 5-9 No Users ---")
usernames = []  # Empty list
if not usernames:
    print("We need to find some users!")

# 5-10. Checking Usernames
print("\n--- 5-10 Checking Usernames ---")
current_users = ["john", "mary", "alex", "sophia", "charles"]
new_users = ["John", "michael", "Sophia", "david", "rose"]

# Make lowercase copy of current users
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new one.")
    else:
        print(f"The username '{new_user}' is available.")

# 5-11. Ordinal Numbers
print("\n--- 5-11 Ordinal Numbers ---")
numbers = list(range(1, 10))
for num in numbers:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")

# 228

# 7-4. Pizza Toppings
print("\n--- 7-4 Pizza Toppings ---")
topping = ""
while topping != "quit":
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    if topping != "quit":
        print(f"I'll add {topping} to your pizza!")

# 7-5. Movie Tickets
print("\n--- 7-5 Movie Tickets ---")
age = ""
while age != "quit":
    age = input("Enter your age (or 'quit' to stop): ")
    if age != "quit":
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

# 7-6. Three Exits
print("\n--- 7-6 Three Exits ---")

# Version 1: Conditional test in while statement
print("Version 1: Conditional test in while")
topping = input("Enter a topping (type 'quit' to stop): ")
while topping != "quit":
    print(f"Adding {topping} to your pizza!")
    topping = input("Enter a topping (type 'quit' to stop): ")

# Version 2: Active variable to control loop
print("\nVersion 2: Active variable control")
active = True
while active:
    topping = input("Enter a topping (type 'quit' to stop): ")
    if topping == "quit":
        active = False
    else:
        print(f"Adding {topping} to your pizza!")

# Version 3: Using break
print("\nVersion 3: Using break")
while True:
    topping = input("Enter a topping (type 'quit' to stop): ")
    if topping == "quit":
        break
    print(f"Adding {topping} to your pizza!")

# 7-7. Infinity
print("\n--- 7-7 Infinity ---")


# 233

# 7-8. Deli
print("\n--- 7-8 Deli ---")
sandwich_orders = ["tuna", "chicken", "pastrami", "egg", "beef"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  # take first order
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)


# 7-9. No Pastrami
print("\n--- 7-9 No Pastrami ---")
sandwich_orders = ["tuna", "pastrami", "chicken", "pastrami", "egg", "pastrami"]
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

# Remove all pastrami orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Process remaining orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches (no pastrami):")
for sandwich in finished_sandwiches:
    print(sandwich)


# 7-10. Dream Vacation
print("\n--- 7-10 Dream Vacation ---")
responses = {}

polling_active = True
while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

    responses[name] = vacation

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        polling_active = False

print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")
