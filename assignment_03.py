# page192

#6-1
my_friend = {
    "first_name": "ada",
    "last": "eze",
    "age": 20,
    "city": "enugu"
}

print(my_friend)

#6-1
favorite_numbers = {"steph": 7, "chidi": 3, "amara": 21, "tunde": 9, "ify": 12}

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")

#6-2
glossary = {
    "function": "a reusable block of code that performs a specific task",
    "dictionary": "a collection of key-value pairs",
    "list": "an ordered, changeable collection of items",
    "argument": "a value passed into a function when it's called",
    "loop": "a structure that repeats a block of code multiple times",
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}:\n\t{meaning}")

# page201

#6-4
glossary = {
    "function": "a reusable block of code that performs a specific task",
    "dictionary": "a collection of key-value pairs",
    "list": "an ordered, changeable collection of items",
    "argument": "a value passed into a function when it's called",
    "loop": "a structure that repeats a block of code multiple times",
    "string": "a sequence of characters, used for text",
    "boolean": "a value that is either True or False",
    "index": "the position of an item in a list, starting at 0",
    "tuple": "an ordered, unchangeable collection of items",
    "module": "a file containing Python code you can import and reuse",
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}:\n\t{meaning}")


#6-5
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}


for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")


print("\nRivers:")
for river in rivers.keys():
    print(river.title())


print("\nCountries:")
for country in rivers.values():
    print(country.title())

#6-5
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

people_to_poll = ["jen", "chukwuemeka", "sarah", "ngozi", "phil", "amaka"]

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()} for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll!")

# page210

#6-7
person_1 = {"first_name": "John", "last_name": "Okafor", "age": 25, "city": "Enugu"}

person_2 = {"first_name": "Mary", "last_name": "Adeyemi", "age": 30, "city": "Lagos"}

person_3 = {"first_name": "David", "last_name": "Obi", "age": 22, "city": "Abuja"}

people = [person_1, person_2, person_3]

for person in people:
    print("\nPerson:")

    for key, value in person.items():
        print(f"{key}: {value}")

#6-8
pet_1 = {"animal": "dog", "owner": "John"}

pet_2 = {"animal": "cat", "owner": "Mary"}

pet_3 = {"animal": "parrot", "owner": "David"}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print("\nPet:")

    for key, value in pet.items():
        print(f"{key}: {value}")

#6-9
favorite_places = {
    "Charles": ["Enugu", "London", "Dubai"],
    "Mary": ["Lagos", "Paris"],
    "Franklin": ["Abuja", "New York", "Cape Town"],
}

for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places:")

    for place in places:
        print(f"- {place}")

#6-10
favorite_numbers = {"Charles": [7, 10, 21], "Mary": [3, 8, 15], "Franklin": [5, 12, 30]}

for person, numbers in favorite_numbers.items():
    print(f"\n{person}'s favorite numbers:")

    for number in numbers:
        print(number)


#6-11
cities = {
    "Enugu": {
        "country": "Nigeria",
        "population": 722664,
        "fact": "Enugu is known as the Coal City.",
    },
    "London": {
        "country": "United Kingdom",
        "population": 9000000,
        "fact": "London is home to Big Ben.",
    },
    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Paris is home to the Eiffel Tower.",
    },
}

for city, information in cities.items():
    print(f"\nCity: {city}")

    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")

#6-12
cities = {
    "Enugu": {
        "country": "Nigeria",
        "population": 722664,
        "fact": "Enugu is known as the Coal City.",
        "language": "English",
        "currency": "Naira",
        "famous_food": "Abacha",
    },
    "London": {
        "country": "United Kingdom",
        "population": 9000000,
        "fact": "London is home to Big Ben.",
        "language": "English",
        "currency": "Pound Sterling",
        "famous_food": "Fish and chips",
    },
    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Paris is home to the Eiffel Tower.",
        "language": "French",
        "currency": "Euro",
        "famous_food": "Croissant",
    },
}

for city, information in cities.items():
    print("\n======================")
    print(f"CITY: {city}")
    print("======================")

    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
    print(f"Language: {information['language']}")
    print(f"Currency: {information['currency']}")
    print(f"Famous food: {information['famous_food']}")


#6-12
cities = {
    "Enugu": {
        "country": "Nigeria",
        "population": 722664,
        "fact": "Enugu is known as the Coal City.",
        "language": "English",
        "currency": "Naira",
        "famous_food": "Abacha",
    },
    "London": {
        "country": "United Kingdom",
        "population": 9000000,
        "fact": "London is home to Big Ben.",
        "language": "English",
        "currency": "Pound Sterling",
        "famous_food": "Fish and chips",
    },
    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Paris is home to the Eiffel Tower.",
        "language": "French",
        "currency": "Euro",
        "famous_food": "Croissant",
    },
}

for city, information in cities.items():
    print("\n======================")
    print(f"CITY: {city}")
    print("======================")

    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
    print(f"Language: {information['language']}")
    print(f"Currency: {information['currency']}")
    print(f"Famous food: {information['famous_food']}")

# page247

#8-3
def make_shirt(size,text):
    print(f"My T-shirt size is {size} and I want {text} to be printed on it, thank you. ")
make_shirt("xl", "El-roi")
make_shirt(text="El-roi", size="xl")

#8-4
def make_shirt(size="large", text="I love python"):
    print(f"My T-shirt size is {size} and I want {text} to be printed on it, thank you. ")

make_shirt()
make_shirt("medium")
make_shirt("small", "Hackathonafrica3.0")

#8-5
def describe_city(city, country="Nigeria"):
    print(f"{city} is in {country}")

describe_city("Lagos")
describe_city("Abuja")
describe_city("Tokyo","Japan")

# page255

#8-6
def city_country(city, country):
    return f"{city}, {country}"

first = city_country("Tokyo", "Japan")
print(first)

second = city_country("Lagos", "Nigeria")
print(second)

third = city_country("Santiago", "Chile")
print(third)

#8-6
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album
firstAlbum = make_album("Adele", "25")
print(firstAlbum)

secondAlbum = make_album("Burna Boy", "Twice as Tall")
print(secondAlbum)

thirdAlbum = make_album("Beyonce", "Renaissance", 16)
print(thirdAlbum)

#8-7
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

while True:
    print("\nEnter 'q' at any time to quit.")
    artist = input("Artist's name: ")
    if artist == "q":
        break

    title = input("Album title: ")
    if title == "q":
        break

    album = make_album(artist, title)
    print(album)

# page261

#8-9
def show_messages(messages):
    for message in messages:
        print(message)

text_messages = ["hey, you free later?", "don't forget the meeting", "happy birthday!"]
show_messages(text_messages)

#8-10

def show_messages(messages):
    for message in messages:
        print(message)

text_messages = ["hey, you free later?", "don't forget the meeting", "happy birthday!"]

#8-11
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

text_messages = ["hey, you free later?", "don't forget the meeting", "happy birthday!"]
sent_messages = []

send_messages(text_messages, sent_messages)

print("\nOriginal list:", text_messages)
print("Sent list:", sent_messages)

# page266

#8-12
def make_sandwich(*toppings):
    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich("cheese")
make_sandwich("cheese", "lettuce", "tomato")
make_sandwich("turkey", "mustard", "onions", "pickles")

#8-13

def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

my_profile = build_profile(
    "steph", "neche", location="Enugu", field="software development", hobby="writing"
)

print(my_profile)

#8-14
def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info

car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)

# page342

#10-6
first_number = input("Enter a number: ")
second_number = input("Enter another number: ")

try:
    total = int(first_number) + int(second_number)
except ValueError:
    print("Sorry, please enter numbers only.")
else:
    print(f"The sum is {total}")

#10-7
print("Enter 'q' to quit at any time.\n")

while True:
    first_number = input("Enter a number: ")
    if first_number == "q":
        break

    second_number = input("Enter another number: ")
    if second_number == "q":
        break

    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, please enter numbers only.\n")
    else:
        print(f"The sum is {total}\n")

#10-8
try:
    with open("cats.txt") as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry, the file cats.txt could not be found.")
else:
    print(contents)

try:
    with open("dogs.txt") as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry, the file dogs.txt could not be found.")
else:
    print(contents)

#10-9
try:
    with open("cats.txt") as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)

try:
    with open("dogs.txt") as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)

#10-10
filename = "alice.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} could not be found.")
else:
    word_count = contents.lower().count("the")
    print(f"The word 'the' appears approximately {word_count} times.")

    word_count_with_space = contents.lower().count("the ")
    print(f"'the ' (with trailing space) appears {word_count_with_space} times.")

# page398
