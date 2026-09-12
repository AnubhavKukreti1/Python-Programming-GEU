# # Question 1: Print numbers from 1 to 10

# for i in range(1,11):
#   print(i)

# # Print numbers from 10 to 1

# for i in range(10,0,-1):
#   print(i)

# # Print all even numbers from 1 to 50

# for i in range(2,51,2):
#   print(i)

# # Print all odd numbers from 1 to 50

# for i in range(1,51,2):
#   print(i)

# # Multiplication table of a given number

# num = int(input("Enter your number : "))
# for i in range(1,11):
#   print(f"{num} x {i} = {num*i}")


# # Sum of numbers from 1 to 100 

# for i in range(1,101):
#   print(i)

# Factorial of a number 

# num = int(input("Enter a number :"))

# fact = 1 

# for i in range(1, num + 1):
#   fact *= i 

# print("Factorial =", fact)

# Count digits in an integer 

# num = int(input("Enter number :"))

# count = 0 

# while num > 0:
#   num //=10
#   count += 1 

# print("Digits =",count)  

# Reverse a number 

# num = int(input("Enter number :"))

# reverse = 0 

# while num > 0: 
#   digit = num % 10 
#   reverse = reverse * 10 + digit
#   num //= 10 
# print(reverse)   


# Print each character of a string using a for loop.

text = input("Enter a string: ")

for char in text:
    print(char)

