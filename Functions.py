#  1. Creating Your First Function
def greet():
    print("Hello!Welcome to Python functions")

#Call the function
greet()

# Task 1: Create a function named `welcome_user` that prints "Welcome to ACA!
def welcome_user():
    print("Welcome to ACA")

welcome_user()

#  2. Function with Parameters
def greet_user(name):
    print(f"Hello,{name}!Great to see you.")

# Call the function with an argument
greet_user("Harpreet Singh")

#  3. Function with Multiple Parameters
def add_numbers(a,b):
    result=a+b
    print(f"The sum of {a} and {b} is {result}")

add_numbers(10,5)

# Task 3: Modify `add_numbers` to subtract numbers instead
def subtract_numbers(a, b):
    result = a - b
    print(f"The difference between {a} and {b} is {result}")

subtract_numbers(20, 7)

#  4. Function That Returns a Value
def multiply(a,b):
    return a*b
product=multiply(10,5)
print("Product is:",product)


#  Task 4: Create a function `divide(a, b)` that returns the result
def divide(a,b):
    if b==0:
        return"Error:Cannot divide by zero"
    return a/b
print("Division result:",divide(10,5))
print("Division result(zero):",divide(10,0))

#  5. Function with Default Parameters
def greet_city(name,city="Vancouver"):
    print(f"{name} lives in {city}")

greet_city("ankita")
greet_city("Rose","Toronto")

#  Task 5: Create a function `introduce(name, age=25)` that prints: "My name is ___ and I am ___ years old."
def introduce(name,age=25):
    print(f"My name is {name} and I am {age} years old")

introduce("Harpreet")
introduce("Ajit",7)

#  6. Using Functions in a Loop
def square(num):
    return num*num

numbers=[1,2,3,4,5]
squares=[]
for n in numbers:
    squares.append(square(n))

print("Square of numbers:",squares)

# Task 6: Write a function `is_even(num)` and use it to filter even numbers from a list
def is_even(num):
    return num % 2==0

even_numbers=[n for n in numbers if is_even(n)]
print("Even numbers:",even_numbers)