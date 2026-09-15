#========================== Logical Questions ===============================


# Question 1 :

# A shopping cart contains the prices of 8 products: 

# prices = [450, 1200, 799, 2500, 349, 999, 1750, 650]

# Using a for loop , Find the most expensive product , Find the cheapest product , Calculate the total cart value.


prices = [450, 1200, 799, 2500, 349, 999, 1750, 650]

total = 0
highest = prices[0]
lowest = prices[0]

for price in prices:
  total += price

  if price > highest:
    highest = price

  if price < lowest:
    lowest = price

print("Total : ", total)
print("Most expensive : ", highest)
print("Cheapest : ", lowest)


# Question 2

# A bank account has the following transactions:

# transactions = [5000, -1200, -800, 25000, -30000, 1500, -700, 45000]

# Positive numbers represent deposits and negative numbers represent withdrawals.

# Using a for loop:

# Calculate the final balance starting from ₹50,000.

# Count withdrawals greater than ₹10,000.

# Print every suspicious withdrawal.

transactions = [5000, -1200, -800, 25000, -30000, 1500, -700, 45000]

balance = 50000
suspicious = 0

for transaction in transactions:
  balance += transaction

  if transaction < -10000:
    print("Suspicious withdrawl : ", transaction)
    suspicious += 1

print("Final Balance : ", balance)
print("Suspicious transactions : ", suspicious)



# Question 2:
# A class has attendance percentages:

# attendance = [92, 67, 81, 74, 96, 58, 88, 72, 91, 63]

# Using a for loop:

# Count how many students have attendance below 75%.

# Print their attendance.

# Calculate the average attendance.

# Determine whether the class average is above 80%.

attendance = [92, 67, 81, 74, 96, 58, 88, 72, 91, 63]

total = 0
below_75 = 0

for percentage in attendance:
  total += percentage


  if percentage < 75:
    print("Student below 75 % : ", percentage)
    below_75 += 1

average = total / len(attendance)
print("Average attendence : ", average)
print("Students below 75 % : ", below_75)

if average > 80:
  print("Class attendence is good.")

else : 
  print("Class attendence needs improvement.")


# Question 3
# A taxi company charges:

# First 5 km → ₹100 flat

# Next 10 km → ₹15/km

# Above 15 km → ₹12/km

# Given the distances travelled by 6 customers:

# distances = [3, 8, 12, 17, 25, 30]

# Using a for loop, calculate the fare for every customer and the company's total earnings.

distances = [3, 8, 12, 17, 25, 30] 

total_earnings = 0

for distance in distances:

  if distance <= 5:
    fare = 100


  elif distance <= 15 :
    fare = 100 + (distance - 5) * 15

  else :
    fare = 100 + (10 * 15) + (distance - 15) * 20

  print("Distance :", distance , "KM")

  print("Fare : ₹", fare , )

  total_earnings += fare 

print("Total earnings : ₹", total_earnings)



# Question 4 
# A warehouse has 10 products with their current stock:

# stock = [120, 15, 80, 5, 200, 12, 75, 3, 150, 18]

# A product is considered low stock if its quantity is below 20.

# Using a for loop:

# Print all low-stock quantities.

# Count low-stock products.

# Calculate the total inventory.

# Find the highest stock quantity.

stock = [120, 15, 80, 5, 200, 12, 75, 3, 150, 18]

total = 0
low_stock = 0
highest_stock = stock[0]


for quantity in stock:

  total += quantity

  if quantity < 20 :
    print("Low stock : ", quantity)

  if quantity > highest_stock :
    highest_stock = quantity

print("Total inventory : ", total) 
print("Low-stock productis : ", low_stock)
print("Highest stock : ", highest_stock)




# Question 5
# A telecom company records monthly data usage in GB:

# usage = [2.5, 8.2, 15.6, 4.8, 20.5, 12.3, 1.7, 18.9]

# A customer is considered a heavy user if they use more than 15 GB.

# Using a for loop:

# Find the number of heavy users.

# Find the total data consumed.

# Find the average usage.

# Print the usage of heavy users.

usage = [2.5, 8.2, 15.6, 4.8, 20.5, 12.3, 1.7, 18.9]

total_users = 0
heavy_users = 0

for gb in usage:

    total_users += gb

    if gb > 15:
        print("Heavy user:", gb, "GB")
        heavy_users += 1

average = total_users / len(usage)

print("Total usage:", total_users, "GB")
print("Average usage:", average, "GB")
print("Heavy users:", heavy_users)

