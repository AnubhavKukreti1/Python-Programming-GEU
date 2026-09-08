# Create a list containing your five favorite foods.
foods = ["Biryani", "Pasta", "Ice Cream", "Momos", "Sandwich"]

# Print the first and last item of the list.
print("First Item: ",foods[0])
print("Last Item: ",foods[-1])

# Replace the second item with another food.
foods[1] = "Noodles"
print("New Food List 1.: ",foods)

# Add "Pizza" to the end of the list.
foods.append("Pizza")
print("New Food List 2.: ",foods)

# Insert "Burger" at index 2.
foods.insert(2, "Burger")
print("New Food List 3.: ",foods)

# Remove "Pizza" from the list.
foods.remove("Pizza")
print("New Food List 4.: ",foods)

# Print the length of the list.
print(len(foods))

# Check whether "Burger" is in the list.
if "Burger" in foods:
  print("Burger is in the List")
else :
  print("Burger is not in the list.")

print("New Food Lists: ", foods)    

# Create a list of numbers from 1 to 10.
numbers = list(range(10,101,10))

# Print all numbers using a for loop.
print("\nAll Numbers")
for num in numbers:
  print(num)

# Print only the even numbers.
numbers1 = list(range(1,11))
print("Even Numbers")
for num1 in numbers1:
  if num1 % 2 == 0:
    print(num1)

# Find the largest number in the list.
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)

# Find the smallest number.
smallest = numbers1[0]
for num in numbers1:
  if num < smallest :
    smallest = num 
print("Smallest Number:", smallest)


# Calculate the sum of all numbers without using sum().
total = 0 
for num in numbers:
  total += num 
print("Sum: ", total)

# Reverse the list.
numbers.reverse()
print(numbers)
# Sort the list in descending order.
numbers.sort(reverse=True)
print("Descending Order: ",numbers)

# Ask the user to enter 5 numbers and store them in a list. Print the largest number.
user_list = []

for i in range(5):
  n = int(input(f"Enter your number {i+1} :"))
  user_list.append(n)

print("Your list is:- ",user_list)  

largest = user_list[0]
for num in user_list:
  if num > largest :
    largest = num 

print("Largest number of the list is:- ", largest)

# Count how many times 5 appears in this list:
numbers = [5, 2, 5, 8, 5, 1]

count = 0 
for num in numbers :
  if num == 5:
    count += 1 

print("5 Appears", count ,"times")    

# Remove all duplicate numbers from this list:
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)

# Create a program that asks the user to enter names until they type "stop". Store all the names in a list and print the final list.
names = []

while True:
    name = input("Enter a name (or 'stop' to finish): ")
    if name.lower() == "stop":
        break
    names.append(name)

print("Final list of names:", names)