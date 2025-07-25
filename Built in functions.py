
fruits=["apple","banana","cherry","mango"]
# Task 1: Print the length of the word "Analytics"
word="Analytics"
print("Length of 'Analytics':",len(word))

#  2. sum() - Sum of all elements in a list
numbers = [10, 20, 30, 40]
total=sum(numbers)
print("Sum of numbers:",total)

# Task 2: Use sum() to find the total of [5, 15, 25, 35]
print("Sum of [5,15,25,35]:",sum([5,15,25,35]))

#  3. max() and min() - Find the largest and smallest values
print("Maximum number:",max(numbers))
print("Minimum number:",min(numbers))

#  Task 3: Use max() to find the highest fruit name alphabetically
print("Alphabetically highest fruit:", max(fruits))

#  4. sorted() - Returns a sorted copy (does NOT change original list)
sorted_fruits=sorted(fruits)
print("Sorted fruits:",sorted_fruits)
print("Original fruits list remains:",fruits)

#  Task 4: Sort the fruits in reverse alphabetical order
print("Reverse sorted fruits:", sorted(fruits, reverse=True))

#  5. type() - Find the data type of a variable
x=100
print("Type of x:",type(x))

y=[1,2,3]
print("Type of y:",type(y))

# ✅ Task 5: Print the type of "Hello" and 3.14
print("Type of 'Hello':", type("Hello"))
print("Type of 3.14:", type(3.14))

#  6. round() - Rounds a float to nearest integer or given decimal places
num=3.14159
print("Rounded (default):", round(num))
print("Rounded to 2 decimals:", round(num, 2))


# Task 6: Round 7.8567 to 1 decimal place
print("Rounded 7.8567 to 1 decimal:", round(7.8567, 1))

#  7. range() - Generates a sequence of numbers
print("Numbers from 0 to 4:", list(range(5)))
print("Numbers from 1 to 10 (step size 2):", list(range(1, 11, 2)))

#  Task 7: Print numbers from 10 to 1 using range
print("Countdown from 10:", list(range(10, 0, -1)))

#  8. abs() - Returns absolute value (no negative sign)
print("Absolute value of -50:", abs(-50))

# ✅ Task 8: Print absolute value of -12.5
print("Absolute of -12.5:", abs(-12.5))

#  9. input() - Takes input from the user (disabled in some IDEs)
name = input("Enter your name: ")
print("Hello,", name)

