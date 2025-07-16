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


#
#Create a List
fruits=["apple","banana","cherry","mango"]
print("initial list:",fruits)

#Task 1:Add orange to the list and print the updated list
fruits.append("orange")
print("After adding 'orange':",fruits)

#Accessing List Elements
print("First fruit:",fruits[0]) #index starts at 0
print("Last fruit:",fruits[-1]) #negative index starts from end

#Task 2:Print the second and third fruits using slicing
print("Second and third fruits:",fruits[1:3])

#Modifying Elements
fruits[1]="blueberry" #changing banana to blueberry
print("After modification:",fruits)

#Task 3:Change "cherry" to "pineapple"
index_cherry=fruits.index("cherry")
fruits[index_cherry]="pineapple"
print("After changing 'cherry' to 'pineapple':",fruits)

#Task 4: Add "lemon" at the begining of the list
fruits.insert(0,"lemon")
print("After adding 'lemon' at beginning:",fruits)

#Removing Items
fruits.remove("apple") #Remove first occurence of apple
popped_fruit=fruits.pop #Remove last item
print("After removing 'apple' and poping the last item:",fruits)
print("Popped fruit:",popped_fruit)

#Task 5: Remove "mango" and print the list
fruits.remove("mango")
print("After removing 'mango':",fruits)

#Sorting and Reversing
fruits.sort()
print("Sorted list:",fruits)

fruits.reverse()
print("Reversed list:",fruits)

#Task 6:Sort in reverse alphabetical order without changing origin
sorted_reversed=sorted(fruits,reverse=True)
print("Reverse-sorted (new list):",sorted_reversed)
print("Original list remains:",fruits)

#Iterating Over a List
print("Fruits one by one:")
for fruit in fruits:
    print("Fruit:",fruit)

#Task 7: Print each fruit in uppercase
print("Fruits in uppercase:")
for fruit in fruits:
    print(fruit.upper())

#List Comprehension
fruit_lengths=[len(fruit) for fruit in fruits]
print("Lengths of each fruit name:",fruit_lengths)

#Task 8: New list with fruits containing the letter 'e'
fruits_with_e=[fruit for fruit in fruits if 'e' in fruit]
print("Fruits with 'e':",fruits_with_e)

#  Creating a List of Lists (2D List)
# Let's say we have student scores for 3 students in 3 subjects
scores=[
    [85,92,78],
    [76,88,90],
    [90,91,95]
]
print("Initial scores:",scores)

#Accessing Elements
print("Score of Student 1 in Subject 2:",scores[0][1])

#Iterating through a List of Lists
print("All scores row by row:")
for student_scores in scores:
    print(student_scores)

# Task 2: Print each individual score in a tabular format
print("Individual scores:")
for i,student_scores in enumerate(scores):
    for j, score in enumerate(student_scores):
        print(f"Student{i+1},Subject{j+1}:{score}")

#Adding a New Student's Scores
scores.append([88,79,85])
print("After adding Student 4:",scores)

# Task 3: Add another student with scores [70, 80, 90]
scores.append([70,80,90])
print("After adding Student 5:",scores)

#Updating a Value
#Let's update Student 2's score in Subject 1 to 95
scores[1][0]=95
print("After updating Student 2's Subject 1 scores:", scores)

#Task 4: Change Student 5's Subject 2 score to 82
scores[4][1]=82
print("After updating Student 5's Subject 2 score:",scores)

# Calculating Averages
print("Average scores per student:")
for i,student_scores in enumerate(scores):
    avg=sum(student_scores)/len(student_scores)
    print(f"student{i+1} average:{round(avg,2)}")

# Task 5: Print subject-wise average (column-wise average)
print("Average score per subject:")
num_subjects=len(scores)
num_students=len(scores)

#  1. len() - Get the length of a list, string, or other iterable
fruits=["apple","banana","cherry"]
print("Length of the list",len(fruits))



