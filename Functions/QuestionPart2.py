""" Problem
You are building an e-commerce website. Each cart item looks like:

cart = [
    {"name": "Laptop", "price": 60000, "quantity": 1},
    {"name": "Mouse", "price": 1500, "quantity": 2},
    {"name": "Keyboard", "price": 3000, "quantity": 1}
]

Write a function that:

Calculates the total price.

Gives a 10% discount if the total is ₹50,000 or more.

Gives a 5% discount if the total is ₹20,000 – ₹49,999.

Otherwise gives no discount.

Returns the final amount. """


def calculate_total(cart):
  subtotal = sum(
    item["price"] * item["quantity"]
    for item in cart
  )                                     # subtotal => 66,000

  if subtotal >= 50000:
    discount = 0.10 

  elif subtotal >= 20000:
    discount = 0.05

  else:
    discount = 0

  final_price = subtotal * (1 - discount)

  return final_price

cart = [
    {"name": "Laptop", "price": 60000, "quantity": 1},
    {"name": "Mouse", "price": 1500, "quantity": 2},
    {"name": "Keyboard", "price": 3000, "quantity": 1}
]

print(calculate_total(cart))



""" Problem
A company wants to calculate employee bonuses.

employees = [
    {"name": "A", "salary": 50000, "rating": 5},
    {"name": "B", "salary": 60000, "rating": 3},
    {"name": "C", "salary": 40000, "rating": 4},
]

Bonus rules:

Rating 5 → 20% of salary

Rating 4 → 10%

Rating 3 → 5%

Rating below 3 → 0%

Write a function that returns a new list containing each employee's bonus. """


employees = [
    {"name": "A", "salary": 50000, "rating": 5},
    {"name": "B", "salary": 60000, "rating": 3},
    {"name": "C", "salary": 40000, "rating": 4},
]


def calculate_bonuses(employees):
    result = []

    for employee in employees:
        salary = employee["salary"]
        rating = employee["rating"]

        if rating == 5:
            bonus = salary * 0.20
        elif rating == 4:
            bonus = salary * 0.10
        elif rating == 3:
            bonus = salary * 0.05
        else:
            bonus = 0

        result.append({
            "name": employee["name"],
            "bonus": bonus
        })

    return result


print(calculate_bonuses(employees))



""" Problem
You receive transactions:

transactions = [
    ("deposit", 5000),
    ("withdraw", 2000),
    ("withdraw", 4000),
    ("deposit", 3000)
]

Write a function that calculates the final balance.

Rules:

Withdrawal should not be allowed if there isn't enough balance.

Invalid transaction types should be ignored.

The function should return both the balance and failed transactions. """



def process_transactions(transactions, initial_balance=0) :
  balance = initial_balance
  failed = [] 

  for transaction , amount in transactions :

    if amount < 0 :
      failed.append((transaction , amount))
      continue

    if transaction == "deposit" :
      balance += amount 

    elif transaction == "withdraw" :
      if amount <= balance :
        balance -= amount
      else :
        failed.append((transaction , amount))

    else :

      failed.append((transaction , amount))

  return balance , failed 

transactions = [
    ("deposit", 5000),
    ("withdraw", 2000),
    ("withdraw", 4000),
    ("deposit", 3000)
]


print(process_transactions(transactions))

"""
Problem
Create a function that tracks failed login attempts.

Rules:

Correct password → "Login successful"

Incorrect password → increase failed attempts.

After 3 failures → "Account locked"

The tricky part: the function needs to remember previous attempts between calls. """


def create_login_system(correct_password):
    attempts = 0
    locked = False

    def login(password):
        nonlocal attempts, locked

        if locked:
            return "Account locked"

        if password == correct_password:
            attempts = 0
            return "Login successful"

        attempts += 1

        if attempts >= 3:
            locked = True
            return "Account locked"

        return f"Wrong password. Attempts left: {3 - attempts}"

    return login


login = create_login_system("python123")

print(login("abc"))
print(login("xyz"))
print(login("hello"))
print(login("python123"))