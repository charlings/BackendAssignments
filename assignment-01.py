# Question 1
instructor = "Alex"
students = 30
course = "Python"
print(f"The instructor is {instructor}, there are {students} students in the {course} class!")

# Question 2
students_morning, students_evening = 15, 25
print(f"Before Swap: Morning Batch = {students_morning}, Evening Batch = {students_evening}")
students_morning, students_evening = students_evening, students_morning
print(f"After Swap: Morning Batch = {students_morning}, Evening Batch = {students_evening}")

# Question 3
python, java, ai = 25, 18, 12
print(f"Python = {python}, Java = {java}, AI = {ai}")

# Question 4
age = 21
rating = 4.9
course_name = "Python Programming"
print(f"{age} is of type {type(age)}")
print(f"{rating} is of type {type(rating)}")
print(f"{course_name} is of type {type(course_name)}")

# Question 5
instructor = "Alex"
academy = "Lkhibra Academy"
slogan = "Learning Python is fun!"
print(f"The instructor at {academy} says: \"{slogan}\"")

# Question 6
num_str = "100"
num_int = int(num_str)
num = 42
num_str2 = str(num)
print(f"Integer value: {num_int}, Type: {type(num_int)}")
print(f"String value: {num_str2}, Type: {type(num_str2)}")

# Question 7
flt = 9.75
int_val = int(flt)
int_num = 50
flt_val = float(int_num)
print(f"Float to Int: {int_val}, Type: {type(int_val)}")
print(f"Int to Float: {flt_val}, Type: {type(flt_val)}")

# Question 8
print(f"True as an integer: {int(True)}")
print(f"False as an integer: {int(False)}")

# Question 9
words = ["Python", "is", "amazing"]
string_val = ", ".join(words)
list_val = string_val.split(", ")
print(f"List to String: {string_val}")
print(f"String to List: {list_val}")

# Question 10
info = {"name": "Lkhibra Academy", "age": 5, "language": "Python"}
print(f"Keys: {list(info.keys())}")
print(f"Values: {list(info.values())}")

# Question 11
a, b = 10, 5
print(f"Addition: {a+b}")
print(f"Subtraction: {a-b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")
print(f"Modulus: {a%b}")

# Question 12
print(f"10 > 5: {10 > 5}")
print(f"10 < 5: {10 < 5}")
print(f"10 == 10: {10 == 10}")
print(f"10 != 5: {10 != 5}")
print(f"10 >= 5: {10 >= 5}")
print(f"10 <= 5: {10 <= 5}")

# Question 13
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"Not True: {not True}")

# Question 14
x = 10
print(f"Initial Value: {x}")
x += 5; print(f"After += : {x}")
x -= 3; print(f"After -= : {x}")
x *= 2; print(f"After *= : {x}")
x /= 3; print(f"After /= : {x}")
x %= 2; print(f"After %= : {x}")

# Question 15
print(f"5 & 3 = {5 & 3}")
print(f"5 | 3 = {5 | 3}")
print(f"5 ^ 3 = {5 ^ 3}")
print(f"5 << 1 = {5 << 1}")
print(f"5 >> 1 = {5 >> 1}")

# Question 16
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# Question 17
a, b, c = map(int, input("Enter three numbers: ").split())
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print(f"The largest number is {largest}.")

# Question 18
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Question 19
score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score} -> Grade: {grade}")

# Question 20
email = "student@example.com"
domain = email.split("@")[1]
print(f"Domain: {domain}")

# Question 21
review = "The quality of this product is great. Quality matters. Excellent quality!"
count = review.lower().count("quality")
print(f"The word 'quality' appears {count} times.")

# Question 22
print("Item        Price")
print("-------------------")
print(f"Laptop      $1200.99")
print(f"Mouse       $25.50")

# Question 23
sentence = "Lkhibra Academy is great"
words = sentence.split()
reversed_sentence = " ".join(words[::-1])
print(reversed_sentence)

# Question 24
post = "Loving #Python and #Coding at #LkhibraAcademy"
hashtags = [word for word in post.split() if word.startswith("#")]
print(f"Hashtags: {hashtags}")

# Question 25
password = "Passw0rd!"
if len(password) >= 8 and any(ch.isdigit() for ch in password) and any(not ch.isalnum() for ch in password):
    print("Password is strong.")
else:
    print("Password is weak.")

# Question 26
messy = " Hello   World  !  "
cleaned = " ".join(messy.split())
print(cleaned)

# Question 27
text = "lkhibra academy python training"
print(text.title())

# Question 28
text = "I love Python programming"
print(text.replace("Python", "Java"))

# Question 29
filename = "report.pdf"
if filename.startswith("report") and filename.endswith(".pdf"):
    print("This is a valid report PDF file.")
else:
    print("Invalid file.")

  # Mini Project: Palindrome Checker 
text = input("Enter a word or phrase: ")
cleaned = text.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print(f"{text} is a palindrome!")
else:
    print(f"{text} is not a palindrome.")
