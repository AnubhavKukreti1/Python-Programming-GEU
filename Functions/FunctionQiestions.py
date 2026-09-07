# 🟢 Level 1: Beginner (1–25)
# Write a function to print "Hello, World!"
def hello():
  print("Hello World")
hello()

# Write a function that prints your name.
def name():
  print("Anubhav")
name()

# Create a function that returns your age.
def age():
  print("Your age is 18")
age()

# Write a function that adds two numbers.
def add(a,b):
  print(a + b)
add(23,24)  

# Write a function that subtracts two numbers.
def subtract(a,b):
  print(a - b)
subtract(45,20)  
# Multiply two numbers using a function.
def multiply(a,b):
  print(a * b)
multiply(5,4)  

# Divide two numbers.
def divide(a, b):
    return a / b

print(divide(10, 2))

# Find the square of a number.
def square(num):
    return num * num

print(square(6))  

# Find the cube of a number.
def cube(num):
    return num * num * num

print(cube(3))

# Find the area of a rectangle.
def rectangle_area(length, width):
    return length * width

print(rectangle_area(5, 4))  

# Find the perimeter of a rectangle.
def rectangle_perimeter(length, width):
    return 2 * (length + width)

print(rectangle_perimeter(5, 4))

# Find the area of a circle.
def Area_Of_Circle(radius):
  pi = 3.14
  return pi * radius * radius

print(Area_Of_Circle(5))

# Find the circumference of a circle.
def circumference(radius):
  pi = 3.14 
  return 2 * pi * radius

print(circumference(5))  

# Convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(25)) 

# Convert Fahrenheit to Celsius.
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print(fahrenheit_to_celsius(77))

# Find the maximum of two numbers.
def maximum(a, b):
  if a > b:
    return a 
  else :
    return b 
print(maximum(20,30))    
# Find the minimum of two numbers.
def minimum(a,b):
  if a < b:
    return a 
  else :
    return b 

print(minimum(30,40))
# Check whether a number is positive.
def positive(num):
  if num > 0:
    return True
  else :
    return False
print(positive(9))    
# Check whether a number is negative.
def negative(num):
  if num < 0:
    return True
  else :
    return False
print(negative(-9))  
# Check whether a number is even.
def is_even(num):
  return num %2 == 0
print(is_even(9))
# Check whether a number is odd.
def is_odd(num):
  return num %2 != 0
print(is_odd(7))
# Find the average of three numbers.
def average(a,b,c):
  return ((a + b + c) / 3)
print(average(12,34,56))  

# Return the larger of three numbers.
def largest_number(a,b,c):
  if a >= b and a >= c :
    return a 
  elif b >= a and b >= c :
    return b 
  else :
    return c 
print(largest_number(1,2,3))    
# Find the absolute value of a number.
def absolute(num):
    if num < 0:
        return -num
    else:
        return num

print(absolute(-15))
# Swap two numbers using a function.

def swap(a, b):
    a, b = b, a
    return a, b

x, y = swap(10, 20)

print(x)
print(y)


# 🟡 Level 2: Basic Logic (26–50)
# Check if a number is prime.
# Find factorial using a function.
# Find GCD of two numbers.
# Find LCM of two numbers.
# Check if a number is a palindrome.
# Reverse a number.
# Count digits in a number.
# Sum digits of a number.
# Find Armstrong number.
# Find perfect number.
# Check leap year.
# Fibonacci number.
# Generate first N Fibonacci numbers.
# Print multiplication table.
# Find power without using **.
# Find square root using a function.
# Check divisible by both 3 and 5.
# Check if a year is century.
# Find largest digit.
# Find smallest digit.
# Count even digits.
# Count odd digits.
# Sum of even digits.
# Sum of odd digits.
# Product of digits.
# 🟠 Level 3: String Functions (51–75)
# Count vowels.
# Count consonants.
# Reverse a string.
# Check palindrome string.
# Convert to uppercase.
# Convert to lowercase.
# Count words.
# Find longest word.
# Find shortest word.
# Replace spaces with "-".
# Remove spaces.
# Count character frequency.
# Remove duplicate characters.
# Find first non-repeating character.
# Find first repeating character.
# Check anagram.
# Capitalize every word.
# Count uppercase letters.
# Count lowercase letters.
# Count digits in string.
# Count special characters.
# Reverse words.
# Find ASCII value.
# Convert ASCII to character.
# Remove vowels.
# 🔵 Level 4: List Functions (76–100)
# Find largest element.
# Find smallest element.
# Find second largest.
# Find second smallest.
# Find average.
# Find sum.
# Find product.
# Remove duplicates.
# Sort ascending.
# Sort descending.
# Reverse list.
# Count even numbers.
# Count odd numbers.
# Find common elements.
# Merge two lists.
# Rotate list left.
# Rotate list right.
# Find missing number.
# Find duplicate numbers.
# Remove negative numbers.
# Remove zeros.
# Count frequency.
# Flatten nested list.
# Find intersection.
# Find union.
# 🟣 Level 5: Dictionary Functions (101–115)
# Count keys.
# Count values.
# Swap keys and values.
# Merge dictionaries.
# Find highest value.
# Find lowest value.
# Remove duplicate values.
# Sort by key.
# Sort by value.
# Count word frequency.
# Group students by grade.
# Find common keys.
# Sum all values.
# Update dictionary.
# Delete key safely.
# 🔴 Level 6: Function Concepts (116–140)
# Function with no arguments.
# Function with one argument.
# Function with multiple arguments.
# Function returning multiple values.
# Default arguments.
# Keyword arguments.
# Positional arguments.
# Variable arguments (*args).
# Keyword variable arguments (**kwargs).
# Combine *args and **kwargs.
# Nested functions.
# Recursive factorial.
# Recursive Fibonacci.
# Recursive palindrome.
# Recursive binary search.
# Lambda addition.
# Lambda sorting.
# Lambda filtering.
# Lambda mapping.
# Lambda reducing.
# Pass function as argument.
# Return a function.
# Closure.
# Decorator.
# Generator function.
# ⚫ Level 7: Intermediate (141–165)
# Implement map manually.
# Implement filter manually.
# Implement reduce manually.
# Count function calls.
# Timer decorator.
# Logging decorator.
# Memoization decorator.
# Retry decorator.
# Validate input decorator.
# Cache results.
# Recursive directory traversal.
# Flatten nested dictionary.
# Merge nested dictionaries.
# Deep copy function.
# Function composition.
# Partial functions.
# Create custom zip().
# Create custom enumerate().
# Create custom range().
# Create custom max().
# Create custom min().
# Create custom sorted().
# Custom all().
# Custom any().
# Recursive sum of nested list.
# 🟤 Level 8: Advanced (166–190)
# Implement a calculator using functions.
# Calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

# Main program
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result:", add(num1, num2))
elif choice == "2":
    print("Result:", subtract(num1, num2))
elif choice == "3":
    print("Result:", multiply(num1, num2))
elif choice == "4":
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice!")

# Build a banking system.
# Student management system.
# Library management.
# Inventory management.
# Contact book.
# Employee payroll.
# ATM simulation.
# Quiz game.
# Tic Tac Toe functions.
# Sudoku validator.
# Password strength checker.
# File encryption.
# File decryption.
# Word counter.
# Log analyser.
# CSV reader.
# JSON parser.
# Text search engine.
# URL validator.
# Email validator.
# Credit card validator.
# Password generator.
# OTP generator.
# UUID generator.
# 🟠 Level 9: AI Engineer-Oriented (191–220)
# Normalize a list of numbers.
# Standardize data.
# Calculate mean.
# Calculate median.
# Calculate mode.
# Calculate variance.
# Calculate standard deviation.
# Min-Max scaling.
# One-hot encoding.
# Label encoding.
# Split dataset.
# Shuffle dataset.
# Batch generator.
# Accuracy function.
# Precision function.
# Recall function.
# F1-score function.
# Confusion matrix.
# Euclidean distance.
# Cosine similarity.
# Dot product.
# Matrix multiplication.
# Sigmoid function.
# ReLU function.
# Softmax function.
# Cross entropy.
# Mean Squared Error.
# Gradient calculation.
# Simple linear regression prediction.
# K-Nearest Neighbour prediction.
# 🎯 Challenge (221–250)

# These combine multiple function concepts and are great preparation for AI engineering and technical interviews:

# Build a scientific calculator.
# Build a text analyser.
# Build a spell checker.
# Build a mini search engine.
# Build a recommendation system (basic).
# Build a chatbot using only functions.
# Build a to-do application.
# Build a file organiser.
# Build a student grading system.
# Build a weather data analyser.
# Build a stock price analyser.
# Build a password manager.
# Build a URL shortener.
# Build a QR code generator wrapper.
# Build a log parser.
# Build a Markdown-to-HTML converter.
# Build a custom JSON serializer.
# Build a custom CSV parser.
# Build a mini interpreter for arithmetic expressions.
# Build a command-line notes application.
# Build a function profiler.
# Build a simple scheduler.
# Build a plagiarism checker (basic).
# Build an image metadata reader.
# Build a text summariser (rule-based).
# Build a sentiment analyser (keyword-based).
# Build a simple web crawler.
# Build a file duplicate finder.
# Build a dataset cleaner.
# Build a complete machine learning pipeline using functions.