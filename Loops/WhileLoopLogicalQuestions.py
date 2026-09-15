"""
QUESTION 1 — ATM TRANSACTION SYSTEM

Create an ATM simulation using a while loop.

Starting balance = ₹50,000

The user should repeatedly see this menu:

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit

Requirements:
- The program should continue running until the user chooses Exit.
- Deposits must be greater than ₹0.
- Withdrawals must not exceed the available balance.
- The user cannot withdraw more than ₹20,000 in a single transaction.
- Keep track of the total number of deposits and withdrawals.
- Keep track of the total amount deposited and withdrawn.
- Display a transaction summary when the user exits.
- If the user enters an invalid menu option, ask again.
- Use a while loop as the main control structure.
"""


"""
QUESTION 2 — ONLINE SHOPPING CART

Create a shopping cart program using a while loop.

The user should repeatedly enter products until they type "checkout".

For every product, ask for:
- Product name
- Price
- Quantity

Requirements:
- Calculate the cost of each product.
- Maintain the running total.
- If the cart total exceeds ₹5,000, give a 10% discount.
- If the cart total exceeds ₹10,000, give a 15% discount instead.
- Add 18% GST after applying the discount.
- Display the final bill at checkout.
- The user should not be allowed to enter a negative price or quantity.
- If the user enters an invalid product price or quantity, ask again.
- Count the total number of different products purchased.
"""


"""
QUESTION 3 — LOGIN SYSTEM WITH ACCOUNT LOCK

Create a login system using a while loop.

Correct username:
    admin

Correct password:
    Python@123

Requirements:
- The user gets a maximum of 3 login attempts.
- After every incorrect attempt, display the number of attempts remaining.
- If the user successfully logs in, display a welcome message.
- After successful login, show a menu:

    1. View Profile
    2. Change Password
    3. Logout

- The user should remain inside the system until they select Logout.
- If the user fails all 3 attempts, lock the account.
- Once locked, the program should not allow another login attempt.
- The new password must be at least 8 characters long.
"""


"""
QUESTION 4 — BANK LOAN REPAYMENT SIMULATOR

Create a loan repayment simulator using a while loop.

Ask the user for:
- Loan amount
- Annual interest rate
- Monthly payment

For every month:
1. Calculate the monthly interest.
2. Add the interest to the remaining loan.
3. Subtract the monthly payment.
4. Display the remaining balance.

Requirements:
- Continue until the loan is completely paid.
- Count the total number of months required.
- Calculate the total interest paid.
- Calculate the total amount paid.
- If the monthly payment is less than or equal to the first month's interest,
  display an error because the loan will never be repaid.
- Display a final loan summary after repayment.
"""


"""
QUESTION 5 — ATM DAILY WITHDRAWAL LIMIT

Create an ATM withdrawal system using a while loop.

Starting account balance:
₹75,000

Daily withdrawal limit:
₹25,000

The user can perform multiple withdrawals in one day.

Requirements:
- Ask the user for a withdrawal amount.
- Reject negative or zero amounts.
- Reject withdrawals greater than the available balance.
- Reject withdrawals that exceed the remaining daily limit.
- Continue asking for withdrawals until:
    1. The user chooses to stop,
    2. The daily withdrawal limit is reached,
    3. The account balance becomes zero.
- Track:
    - Number of withdrawals
    - Total withdrawn
    - Remaining balance
    - Remaining daily limit
- At the end, display a complete transaction summary.
"""


"""
QUESTION 6 — RESTAURANT BILLING SYSTEM

Create a restaurant billing system using a while loop.

Menu:

1. Burger       ₹150
2. Pizza        ₹250
3. Pasta        ₹180
4. Sandwich     ₹120
5. Coffee       ₹80
6. Exit

Requirements:
- Allow the customer to order multiple items.
- Ask for the quantity of each item.
- Calculate the running bill.
- If the subtotal exceeds ₹1,000, provide a 10% discount.
- Add 5% GST after the discount.
- If the customer orders more than 5 items in total, give an additional ₹100 discount.
- Display the complete bill when the customer chooses Exit.
- Handle invalid menu choices.
- Handle invalid quantities.
- Display:
    - Subtotal
    - Discount
    - GST
    - Final amount
    - Total number of items
"""


"""
QUESTION 7 — ELECTRICITY BILL CALCULATOR

Create an electricity billing program using a while loop.

Ask the user for the electricity units consumed.

Use the following pricing:

First 100 units:
    ₹5 per unit

Next 200 units:
    ₹7 per unit

Next 300 units:
    ₹10 per unit

Above 600 units:
    ₹15 per unit

Requirements:
- Calculate the electricity bill.
- Ask the user whether they want to calculate another customer's bill.
- Continue until the user chooses "no".
- Keep track of:
    - Number of customers
    - Total units consumed
    - Total revenue
    - Highest bill
    - Lowest bill
- Display a final company summary when the program ends.
"""


"""
QUESTION 8 — MOBILE DATA PLAN MONITOR

Create a mobile data monitoring system using a while loop.

A customer has a monthly data limit of 50 GB.

Every time the customer uses data, ask how many GB were consumed.

Requirements:
- Continue accepting usage until the user enters 0.
- Keep track of total data consumed.
- Display remaining data after every usage.
- If usage reaches 80% of the limit, display:
      "Warning: You are approaching your data limit."
- If usage exceeds the limit, calculate the extra data used.
- Extra data costs ₹20 per GB.
- At the end, display:
    - Total data used
    - Remaining data
    - Extra data used
    - Extra charges
- Reject negative data usage.
"""


"""
QUESTION 9 — DELIVERY MANAGEMENT SYSTEM

Create a delivery tracking system using a while loop.

The company has a list of delivery statuses:

    "pending"
    "delivered"
    "cancelled"

The program should repeatedly ask the delivery person to enter the
status of a delivery.

Requirements:
- Continue until the user enters "stop".
- Count:
    - Total deliveries
    - Delivered orders
    - Pending orders
    - Cancelled orders
- Calculate the delivery success percentage.
- If the delivery success rate is below 70%, display:
      "Performance needs improvement."
- If it is 90% or above, display:
      "Excellent performance."
- Reject invalid statuses.
- At the end, display a complete performance report.
"""


"""
QUESTION 10 — EMPLOYEE SALARY PROCESSING SYSTEM

Create an employee salary processing system using a while loop.

For each employee, ask for:
- Employee name
- Basic salary
- Years of experience

Salary rules:

Experience below 2 years:
    No bonus

Experience 2–5 years:
    10% bonus

Experience 6–10 years:
    20% bonus

Experience above 10 years:
    30% bonus

Tax rules:

Salary below ₹30,000:
    No tax

Salary ₹30,000–₹60,000:
    10% tax

Salary ₹60,001–₹1,00,000:
    20% tax

Salary above ₹1,00,000:
    30% tax

Requirements:
- Continue entering employees until the user enters "stop".
- Calculate bonus for each employee.
- Calculate gross salary.
- Calculate tax.
- Calculate final salary.
- Display each employee's salary details.
- Keep track of:
    - Total employees
    - Total salary paid
    - Total tax collected
    - Highest-paid employee
    - Lowest-paid employee
    - Average final salary
- Display a final company payroll report.
"""
