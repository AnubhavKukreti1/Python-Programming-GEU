
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
