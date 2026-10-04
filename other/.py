# n = int(input("Enter a number: "))
# sum = 0

# for i in range(1, n + 1):
#     sum += i  
  
# print("Sum of first", n, "natural numbers is:", sum)


# # write a program to calculate the square of each numbers upto n  
# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     square = i ** 2
#     print("Square of", i, "is:", square)  

# Write a program to find the total number of even numbers present upto n input of n will be provided by the user 

n = int(input("Enter a number: "))  
count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1

print("Total number of even numbers upto", n, "is:", count)


# Write a program to find the total number of even numbers present upto n input of n will be provided by the user using while loop 

n = int(input("Enter a number: "))

count = 0
i = 1

while i <= n:
    if i % 2 == 0:
        count += 1
    i += 1

print("Total number of even numbers up to", n, "is:", count)

# Write a python program to find the factorial of an integer entered by the user using while loop

n = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1  

print("Factorial of", n, "is:", factorial)