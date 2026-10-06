
# Write a func to print graphic era without using return type 

def GEU():
  print("Graphic Era")

GEU()

# write a function to find the sum of two numbers while making a function add use return tyoes

a = int(input("Enter a number :"))
b= int(input("Enter another number :"))

def add():
  return a + b 

print(add())


# write a funtion to print the cube of a number using parameter in a function and without return type

def cube(num):
  print(num * num * num)

print(cube(3))

# Write a python program to calculate the factorial of a number while using parameters and return type 

def factorial(n):
  fact = 1

  for i in range(1, n + 1):
    fact = fact * i

  return fact


num = int(input("Enter a number: "))
result = factorial(num)

print("Factorial =", result)


""" Problem 1
You are building an e-commerce website. Each cart item looks like:

cart = [
    {"name": "Shoes", "price": 2500, "quantity": 2},
    {"name": "T-Shirt", "price": 1200, "quantity": 3},
    {"name": "Cap", "price": 500, "quantity": 1}
]

Write a function that:

Calculates the subtotal.

Gives a 15% discount if the subtotal is ₹10,000 or more.

Gives a 10% discount if the subtotal is ₹5,000 – ₹9,999.

Otherwise gives no discount.

Adds ₹100 shipping if the final amount is below ₹5,000.

Shipping is free if the final amount is ₹5,000 or more.

Returns the final amount.
"""
cart = [
    {"name": "Shoes", "price": 2500, "quantity": 2},
    {"name": "T-Shirt", "price": 1200, "quantity": 3},
    {"name": "Cap", "price": 500, "quantity": 1}
]

def calculate_bill(cart):
  subtotal = 0

  for item in cart:
    subtotal += item["price"] * item["quantity"]
  
  if subtotal >= 10000:
    discount = 0.15
  elif subtotal >= 5000:
    discount = 0.10 
  else :
    discount = 0 
  
  discount_amount = subtotal * discount

  final_amount = subtotal - discount_amount

  if final_amount < 5000 :
    shipping = 100

  else : 
    shipping = 0 
  
  final_amount += shipping

  return final_amount

print(calculate_bill(cart))



""" Problem 2
A company wants to calculate employee salaries after increments.

employees = [
    {"name": "A", "salary": 50000, "experience": 6},
    {"name": "B", "salary": 40000, "experience": 2},
    {"name": "C", "salary": 70000, "experience": 10}
]

Write a function that returns a new list containing each employee's
new salary.

Salary increment rules:

Experience 8 years or more → 20% increment

Experience 5–7 years → 12% increment

Experience 3–4 years → 7% increment

Experience below 3 years → 0% increment.

Do not modify the original employee list.
"""

employees = [
    {"name": "A", "salary": 50000, "experience": 6},
    {"name": "B", "salary": 40000, "experience": 2},
    {"name": "C", "salary": 70000, "experience": 10}
]

def calculate_salaries(employees):
  result = []

  for employee in employees:
    salary = employee["salary"]
    experience = employee["experience"]

    if experience >= 8 :
      increment = 0.20
    elif experience >= 5 :
      increment = 0.12
    elif experience >= 3 :
      increment = 0.07 
    else :
      increment = 0 

    new_salary = salary * (1 + increment)

    result.append({
      "name" : employee["name"],
      "new_salary": new_salary
    })

  return result

print(calculate_salaries(employees))




""" Problem 3
You receive a list of bank transactions:

transactions = [
    ("deposit", 10000),
    ("withdraw", 3000),
    ("withdraw", 9000),
    ("deposit", 5000),
    ("transfer", 2000),
    ("withdraw", -500)
]

Write a function that calculates the final balance.

Rules:

A deposit increases the balance.

A withdrawal should only happen if there is enough balance.

Negative amounts are invalid transactions.

Invalid transaction types should be ignored and stored as failed
transactions.

Return both:

1. The final balance
2. The list of failed transactions

The function should also accept an optional initial_balance parameter.
"""

transactions = [
    ("deposit", 10000),
    ("withdraw", 3000),
    ("withdraw", 9000),
    ("deposit", 5000),
    ("transfer", 2000),
    ("withdraw", -500)
]

def calculate_balance(transactions, initial_balance=0):
  balance = initial_balance
  failed_transactions = []

  for transaction in transactions:
    transaction_type, amount = transaction

    if amount < 0:
      failed_transactions.append(transaction)
      continue

    if transaction_type == "deposit":
      balance += amount
    elif transaction_type == "withdraw":
      if balance >= amount:
        balance -= amount
      else:
        failed_transactions.append(transaction)
    else:
      failed_transactions.append(transaction)

  return balance, failed_transactions

print(calculate_balance(transactions, initial_balance=5000))

""" Problem 4
You are managing product inventory.

products = [
    {"name": "Laptop", "stock": 5},
    {"name": "Mouse", "stock": 20},
    {"name": "Keyboard", "stock": 0},
    {"name": "Monitor", "stock": 3}
]

Write a function that analyzes the inventory.

The function should return three lists:

1. Products that are available.
2. Products that are out of stock.
3. Products that are low in stock.

A product is considered:

Available → stock greater than 5

Low stock → stock between 1 and 5

Out of stock → stock equal to 0

Return the product names rather than the complete dictionaries.
"""

products = [
    {"name": "Laptop", "stock": 5},
    {"name": "Mouse", "stock": 20},
    {"name": "Keyboard", "stock": 0},
    {"name": "Monitor", "stock": 3}
]

def analyze_inventory(products):
  available = []
  low_stock = []
  out_of_stock = []

  for product in products:
    name = product["name"]
    stock = product["stock"]

    if stock > 5:
      available.append(name)
    elif stock >= 1:
      low_stock.append(name)
    else:
      out_of_stock.append(name)

  return available, low_stock, out_of_stock

print(analyze_inventory(products))


""" Problem 5
You are creating a student result system.

students = [
    {"name": "Rahul", "marks": [80, 90, 70]},
    {"name": "Aman", "marks": [40, 35, 50]},
    {"name": "Priya", "marks": [95, 92, 88]}
]

Write a function that returns a new list containing the result of
each student.

For every student:

Calculate the total marks.

Calculate the percentage.

If any subject has marks below 40, the student is "Fail".

Otherwise calculate the grade:

90 or above → A+

80–89 → A

70–79 → B

60–69 → C

Below 60 → D

Each result should contain:

name

total

percentage

grade
"""
students = [
    {"name": "Rahul", "marks": [80, 90, 70]},
    {"name": "Aman", "marks": [40, 35, 50]},
    {"name": "Priya", "marks": [95, 92, 88]}
]

def generate_results(students):
  results = []

  for student in students:
    name = student["name"]
    marks = student["marks"]

    total = sum(marks)

    percentage = total / len(marks)

    if any(mark < 40 for mark in marks):
      grade = "Fail"
    else:
      if percentage >= 90:
        grade = "A+"
      elif percentage >= 80:
        grade = "A"
      elif percentage >= 70:
        grade = "B"
      elif percentage >= 60:
        grade = "C"
      else:
        grade = "D"

    results.append({
        "name": name,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })

  return results

print(generate_results(students))


""" Problem 6
You are creating an expense tracker.

expenses = [
    ("food", 500),
    ("travel", 1200),
    ("food", 300),
    ("shopping", 2000),
    ("travel", 800),
    ("food", 700)
]

Write a function that calculates the total amount spent in each
category.

The function should return a dictionary like:

{
    "food": 1500,
    "travel": 2000,
    "shopping": 2000
}

Then create another function that finds the category with the highest
total spending.

If two categories have the same highest amount, return the first one.
"""

expenses = [
    ("food", 500),
    ("travel", 1200),
    ("food", 300),
    ("shopping", 2000),
    ("travel", 800),
    ("food", 700)
]


def calculate_expenses(expenses):
    result = {}

    for category, amount in expenses:

        if category in result:
            result[category] += amount
        else:
            result[category] = amount

    return result


def highest_expense(expenses):
    totals = calculate_expenses(expenses)

    highest_category = None
    highest_amount = 0

    for category, amount in totals.items():

        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

    return highest_category


print(calculate_expenses(expenses))
print(highest_expense(expenses))




""" Problem 7
You are creating a simple ATM system.

Create a function:

create_atm(initial_balance, correct_pin)

The function should return another function that can perform ATM
operations.

The returned function should support:

"balance" → returns current balance

"deposit" → adds money to the balance

"withdraw" → removes money if sufficient balance exists

"change_pin" → changes the PIN

The ATM should remember the balance and PIN between function calls.

The user gets only 3 attempts to enter the correct PIN.

After 3 incorrect PIN attempts, the account should be locked.

Once the account is locked, no further transactions are allowed.

Use a nested function and nonlocal where appropriate.
"""


def create_atm(initial_balance, correct_pin):

    balance = initial_balance
    pin = correct_pin
    failed_attempts = 0
    locked = False

    def atm(operation, amount=0, entered_pin=None, new_pin=None):
        nonlocal balance, pin
        nonlocal failed_attempts, locked

        if locked:
            return "Account locked"

        if entered_pin != pin:
            failed_attempts += 1

            if failed_attempts >= 3:
                locked = True
                return "Account locked"

            return "Incorrect PIN"

        failed_attempts = 0

        if operation == "balance":
            return balance

        elif operation == "deposit":
            if amount <= 0:
                return "Invalid amount"

            balance += amount
            return balance

        elif operation == "withdraw":
            if amount <= 0:
                return "Invalid amount"

            if amount > balance:
                return "Insufficient balance"

            balance -= amount
            return balance

        elif operation == "change_pin":
            pin = new_pin
            return "PIN changed successfully"

        else:
            return "Invalid operation"

    return atm


atm = create_atm(10000, 1234)

print(atm("balance", entered_pin=1234))
print(atm("deposit", 5000, entered_pin=1234))
print(atm("withdraw", 2000, entered_pin=1234))
print(atm("balance", entered_pin=1234))






""" Problem 8
You are building a library management system.

books = [
    {"title": "Python", "available": True},
    {"title": "Java", "available": True},
    {"title": "C++", "available": False}
]

Write a function:

borrow_book(books, title)

Rules:

If the book does not exist, return "Book not found".

If the book exists but is not available, return "Book already borrowed".

If the book is available, change its availability to False and return
"Book borrowed successfully".

Also write:

return_book(books, title)

If the book does not exist, return "Book not found".

If the book is already available, return "Book was not borrowed".

Otherwise change its availability to True and return
"Book returned successfully".
"""


""" Problem 9
You are building a movie ticket booking system.

movies = [
    {"name": "Movie A", "price": 250, "seats": 10},
    {"name": "Movie B", "price": 300, "seats": 5},
    {"name": "Movie C", "price": 200, "seats": 0}
]

Write a function:

book_ticket(movies, movie_name, number_of_seats)

Rules:

The movie must exist.

If the movie does not exist, return "Movie not found".

If there are not enough seats, return "Not enough seats".

Otherwise reduce the available seats.

Calculate the total ticket price.

If the customer books more than 5 seats, give a 10% discount.

Return the movie name, number of seats, discount and final price.
"""


""" Problem 10
You are creating a coupon system for an online store.

Write a function:

apply_coupon(amount, coupon)

Available coupons:

"SAVE10" → 10% discount

"SAVE20" → 20% discount

"FLAT500" → ₹500 discount

Rules:

SAVE10 works for all amounts.

SAVE20 only works if the amount is ₹5,000 or more.

FLAT500 only works if the amount is ₹3,000 or more.

An invalid coupon should give no discount.

The final amount can never be negative.

Return the final amount after applying the coupon.
"""


""" Problem 11
You are creating a login system.

Create a function:

create_login_system(correct_username, correct_password)

The function should return another function called login.

The login function should remember previous login attempts.

Rules:

Correct username and password → "Login successful"

Incorrect username or password → increase failed attempts.

After 3 failed attempts → "Account locked"

Once the account is locked, even the correct password should return
"Account locked".

If the login is successful before the account is locked, reset the
failed attempt counter to 0.

Use a nested function and nonlocal variables.
"""


""" Problem 12
You are creating a quiz application.

questions = [
    {"question": "2 + 2?", "answer": "4"},
    {"question": "Capital of India?", "answer": "Delhi"},
    {"question": "5 * 5?", "answer": "25"}
]

Write a function:

create_quiz(questions)

The function should return another function called answer_question.

The quiz should remember:

The current question number.

The user's score.

The number of questions answered.

When the user provides the correct answer, increase the score.

When the answer is incorrect, do not increase the score.

After all questions have been answered, return the final score.

The quiz should not allow additional answers after it has finished.

Use a nested function and nonlocal variables.
"""


""" Problem 13
You are building an online food delivery system.

orders = [
    {"customer": "A", "amount": 1200, "distance": 3},
    {"customer": "B", "amount": 500, "distance": 8},
    {"customer": "C", "amount": 3000, "distance": 15}
]

Write a function that calculates the delivery charge for every order.

Rules:

If order amount is ₹2,000 or more → Free delivery.

Otherwise:

Distance up to 5 km → ₹50 delivery

Distance from 6 to 10 km → ₹100 delivery

Distance above 10 km → ₹200 delivery

Return a new list containing:

customer name

original amount

delivery charge

final amount
"""


""" Problem 14
You are creating a number analysis program.

Write the following functions:

count_digits(n)

digit_sum(n)

reverse_number(n)

is_palindrome(n)

is_prime(n)

is_armstrong(n)

is_perfect(n)

Then create another function:

analyze_number(n)

The analyze_number function should call the other functions and return
a dictionary containing all the results.

For example, for:

n = 153

The result should contain:

digits

digit_sum

reverse

palindrome

prime

armstrong

perfect

Do not repeat the same logic unnecessarily.
"""


""" Problem 15
You are building a complete e-commerce order processing system.

orders = [
    {
        "customer": "Rahul",
        "items": [
            {"name": "Laptop", "price": 60000, "quantity": 1},
            {"name": "Mouse", "price": 1500, "quantity": 2}
        ],
        "coupon": "SAVE10"
    },
    {
        "customer": "Aman",
        "items": [
            {"name": "Keyboard", "price": 3000, "quantity": 2}
        ],
        "coupon": None
    }
]

Write a function:

process_orders(orders)

For every order:

Calculate the subtotal using price × quantity.

Apply the following discounts:

Subtotal ₹50,000 or more → 10% discount

Subtotal ₹20,000–₹49,999 → 5% discount

Below ₹20,000 → no discount

Then apply the coupon.

Available coupons:

SAVE10 → additional 10% discount

SAVE20 → additional 20% discount

If the final amount after discounts is below ₹5,000,
add ₹100 delivery charges.

Otherwise delivery is free.

Return a new list containing:

customer

subtotal

discount

delivery_charge

final_amount

Also calculate and return the total revenue from all orders.

Do not modify the original orders list.
"""
