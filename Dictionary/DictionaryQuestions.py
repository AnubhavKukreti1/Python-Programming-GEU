""" Q1. Create and print a dictionary
   Question: Create a dictionary containing name = "Rahul", age = 20, and city = "Dehradun". Then print it. 
"""

student = {
  "name" : "Rahul",
  "age" : 20,
  "city" : "Dehradun"
}

print(student)
# {'name': 'Rahul', 'age': 20, 'city': 'Dehradun'}

"""
Q2. Access a value
Question: Given:

student = {
    "name": "Aman",
    "age": 20,
    "marks": 85
}

Print only the student's name. 
"""

student1 = {
    "name": "Aman",
    "age": 20,
    "marks": 85
}

print(student1["name"])

"""
Q3. Change a value
Question: Change the marks from 85 to 95.
"""

student1["marks"] = 95

print(student1)

# {'name': 'Aman', 'age': 20, 'marks': 95} 

"""
Q4. Add a new key
Question: Add:

"course": "Python"

to the dictionary.
"""

student1["course"] = "Python"

print(student1)

# Q5. Remove a key
# Question: Remove the "age" key.

# Answer:

student.pop("age")

print(student)

# Output:

# {'name': 'Aman', 'marks': 95, 'course': 'Python'}

# You can also use:

del student["age"]

# Q6. Check whether a key exists
# Question: Check whether "name" exists in the dictionary.

# Answer:

if "name" in student:
    print("name exists")
else:
    print("name does not exist")

# Output:

# name exists

# A shorter way:

print("name" in student)

# Output:

True

# Intermediate
# Q7. Predict the output
# Question:

person = {
    "name": "Raj",
    "age": 25
}

person["age"] = 30
person["city"] = "Delhi"

print(person)

# Answer:

{'name': 'Raj', 'age': 30, 'city': 'Delhi'}

# Why?

# First, "age" is changed from 25 to 30.

# Then "city" is added with the value "Delhi".

# Q8. Predict the output
# Question:

numbers = {
    "a": 10,
    "b": 20,
    "c": 30
}

for key, value in numbers.items():
    print(key, value)

# Answer:

# a 10
# b 20
# c 30

# Here:

numbers.items()

# gives us both the key and value.

# Q9. Count character frequency
# Question: Write a program that counts how many times each character occurs in:


word = "hello"

# Expected result:

{
    "h": 1,
    "e": 1,
    "l": 2,
    "o": 1
}

# Answer:



count = {}

for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)

# Output:

{'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""
How it works
For every character, we check whether it already exists.

For example, when Python reaches the second l:
"""
count["l"] += 1

# So its count changes from 1 to 2.
"""
Q10. Store 5 students and marks
Question: Create a dictionary of 5 students and their marks. Then use a loop to print:
"""
Aman: 85
Rahul: 90
...

# Answer:

students = {
    "Aman": 85,
    "Rahul": 90,
    "Priya": 78,
    "Neha": 95,
    "Rohit": 88
}

for name, marks in students.items():
    print(name + ":", marks)

# Output:

# Aman: 85
# Rahul: 90
# Priya: 78
# Neha: 95
# Rohit: 88

# Q11. Find the student with the highest marks
# Question:

marks = {
    "Aman": 85,
    "Rahul": 92,
    "Priya": 78,
    "Neha": 95
}

# Find the student who has the highest marks.

# Answer:

highest_student = ""
highest_marks = 0

for student, mark in marks.items():
    if mark > highest_marks:
        highest_marks = mark
        highest_student = student

print(highest_student)
print(highest_marks)

# Output:

# Neha
# 95

# A useful built-in approach is:

highest_student = max(marks, key=marks.get)

print(highest_student)
print(marks[highest_student])

# Output:
"""
Neha
95

Q12. Count word frequency
Question: Count the frequency of each word:

sentence = "python is easy and python is powerful"

Expected result:
"""
{
    "python": 2,
    "is": 2,
    "easy": 1,
    "and": 1,
    "powerful": 1
}

# Answer:

sentence = "python is easy and python is powerful"

words = sentence.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)

# Output:

{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

# The important part here is:

sentence.split()

# It converts the sentence into a list of words:

["python", "is", "easy", "and", "python", "is", "powerful"]

# Q13. Find the average marks
# Question:

student = {
    "name": "Aman",
    "marks": [80, 90, 85]
}
"""
Find the student's average marks.
"""

# Answer:

student = {
    "name": "Aman",
    "marks": [80, 90, 85]
}

marks = student["marks"]

average = sum(marks) / len(marks)

print(average)

# Output:

# 85.0

# Here:

sum(marks)

# gives:

# 255

# and:

len(marks)

# gives:

# 3

# So:

# 255 / 3 = 85
"""
Q14. Create a dictionary of numbers and squares
Question: Create:
"""
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

# Answer:

squares = {}

for number in range(1, 6):
    squares[number] = number ** 2

print(squares)

# Output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# You can also do this using dictionary comprehension:

squares = {number: number ** 2 for number in range(1, 6)}

print(squares)
"""
Q15. dictionary["name"] vs dictionary.get("name")
Question: What is the difference between:
"""
dictionary["name"]

# and:

dictionary.get("name")

# Answer:

# Suppose:

student = {
    "name": "Aman",
    "age": 20
}

# Both work when "name" exists:

print(student["name"])
print(student.get("name"))

