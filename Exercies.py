from tkinter.messagebox import YESNO

name="Harpreet Singh"
age=36
height=1.83 # in meters
is_student=True

print("Name:",name)
print("Age:",age)
print("Height:",height)
print("Is student",is_student)

#Task 1:Creat variables for your city(string),number of kids (integer) and has_pet (boolean)
city="Abbotsford"
num_kids=1
has_pet=False

print("\nYour City:",city)
print("Number of kids:",num_kids)
print("Has pet:",has_pet)

#Task 2: Reassigning Variables
age=37 #Happy birthday
print("\nNew Age after birthday:",age)
city="Vancouver"
print("New city:",city)

#using Variables in Expressions
year_born=2025-age
print("\nYear born:",year_born)

#Task 3: Calculate the age your kids will be in 5 years and print
kids_age_in_5_years=num_kids+5 #Assuming num_kids is the total number, change logic as needed
print("kids' age in 5 year (assuming starting age=num_kids):",kids_age_in_5_years)

#Data Types check
print("\nType of name:",type(name))
print("Type of age:",type(age))
print("Type of height:",type(height))
print("Type of is_student:",type(is_student))
print("Type of city:",type(city))
print("Type of num_kids:",type(num_kids))
print("Type of has_pet:",type(has_pet))

#String Concatenation Using Variables
greeting="Hello, my name is" + name + "and I live in" + city + "."
print("\n"+greeting)

#Task 5: Create a sentence introducing yourself using your variables and print it
my_intro = f"My name is {name}, I am {age} year old, and I live in {city}."
print(my_intro)