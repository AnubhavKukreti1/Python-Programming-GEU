# We can check the type of any value using:
print(type(10)) # <class 'int'>
print(type("Hello")) # <class 'str'>
print(type(3.14)) # <class 'float'>

# Numeric data types

age = 18
marks = 95 
temperature = -5

print(type(age)) # <class 'float'>


# Operations 

a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7 
print(a * b)  # 30
print(a / b)  # 3.333333333335
print(a // b) # 3
print(a % b)  # 1
print(a ** b) # 1000


# Float 

pi = 3.14159
price = 99.99

print(type(pi)) # <class 'float'>


# Complex 

x = 2 + 5j 
y = 9 - 6j

print(type(x)) # <class 'complex'>

print(x + y) #(11-1j)
print(x * y) # (48+33j)

# Type Conversion 

a = int(5.8)
b = float(5)
c = str(100)

print(a) # 5
print(b) # 5.0
print(c) # 100

# Boolean 

is_student = True
is_adult = False

print(type(is_student)) # <class 'bool'>
 
print(10 > 5)  # True
print(10 == 5) # False
print(10 != 5) # True 

print(True and False) # False 
print(True or False)  #True
print(not True)       #False

# --------- String ---------

name = "Anubhav"
city = 'Dehradun'
a = "a"

print(ord(a))
print(name) #Anubhav
print(city) #Dehradun 

# String Indexing

name = "Python"

print(name[0])  #p
print(name[1])  #y
print(name[-1]) #n 

# String Slicing 

text = "Programming"

print(text[0:5])  # Progr
print(text[3:])   # gramming
print(text[:6])   # Progra
print(text[::-1]) # gnimmargorP

# Important String Methods

# Uppercase :
name.upper()

# lowercase
name.lower()

# Capitalize 
name.capitalize()

# Title
name.title()

# Replace
name.replace("a", "x")

# Count
name.count("a")

# Find
name.find("h")

# Split
# sentence.split()

# Join
"-".join(["a", "b", "c"])

# Strip
text.strip()

# String Formatitng 

#f-Strings :
name = "Anubhav"
age = 18 

print(f"My name is {name} and I am {age} years old.")
# My name is Anubhav and I am 18 years old.

# Escape Characters

print("Hello\nWorld") 
# Hello
# World 

print("Hello\tWorld") # Hello   World   
print("\"Python\"") # "Python" 