""" Even or Odd
Write a program that takes an integer from the user and prints whether it is even or odd. """

a = int(input("Enter a integer : "))

if a % 2 == 0 :
  print("Even")
else :
  print("Odd")


""" Positive, Negative, or Zero
Take a number as input and determine whether it is positive, negative, or zero. """

a = int(input("Enter a number : "))

if a < 0 :
  print("Negative")
else :
  print("Positive")

""" Largest of Three Numbers
Take three numbers as input and print the largest one. """

print("Enter three numbers")

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
c = int(input("Enter your third number : "))

largest = a 

if c < a > b :
  largest = a 
elif a < b > c :
  largest = b 
else :
  largest = c 

print("Largest number is : ", largest)


""" Sum of Numbers
Write a program to calculate the sum of numbers from 1 to n. """


print("Sum of all numbers")

num = int(input("Enter the last number: "))

total = 0

for i in range(1, num + 1):
    total += i

print(total)


""" Multiplication Table
Take a number from the user and print its multiplication table from 1 to 10. """

print("Multiplication of number")

num = int(input("Enter a number : "))

for i in range(1,11):
  print(num * i) 




""" Count Digits
Given an integer, count how many digits it contains.
Example: 12345 → 5 """

num = int(input("Enter a number : "))

count = 0

while num > 0:
  num = num // 10
  count += 1 

print(count)

""" Reverse a Number
Reverse a number without converting it to a string.
Example: 1234 → 4321 """

print("Reverse a Number")

num = int(input("Enter a number : "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(reverse)


""" Palindrome Number
Check whether a number is a palindrome.
Example: 121 → Palindrome """

print("Palindrome Number")

num = int(input("Enter a number : "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")