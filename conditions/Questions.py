"""
1. ✈️ Flight Baggage Charges — Domestic / International
Question:
Write a program to calculate the extra baggage charges for a passenger travelling by flight.

The program should accept:

Flight type (Domestic or International)
Baggage weight in kg
For Domestic flights:

If baggage weight is 15 kg or less, there is no extra charge.
If baggage weight is more than 15 kg but up to 25 kg, charge ₹500.
If baggage weight is more than 25 kg, charge ₹500 + ₹100 for every kg above 25 kg.
For International flights:

If baggage weight is 20 kg or less, there is no extra charge.
If baggage weight is more than 20 kg but up to 30 kg, charge ₹1,000.
If baggage weight is more than 30 kg, charge ₹1,000 + ₹200 for every kg above 30 kg.
Display the flight type, baggage weight and total extra baggage charges.
"""
flight = input("Enter flight type (Domestic/International): ")
weight = float(input("Enter baggage weight in kg: "))

if flight == "Domestic":
    if weight <= 15:
        charge = 0
    elif weight <= 25:
        charge = 500
    else:
        charge = 500 + (weight - 25) * 100

elif flight == "International":
    if weight <= 20:
        charge = 0
    elif weight <= 30:
        charge = 1000
    else:
        charge = 1000 + (weight - 30) * 200

else:
    charge = -1

if charge == -1:
    print("Invalid flight type")
else:
    print("Extra baggage charges:", charge)
  

"""
2. 💧 Water Consumption Tariff
Question:
Write a program to calculate the monthly water bill based on the amount of water consumed.

The program should accept the number of litres of water consumed.

Tariff structure:

If consumption is 100 litres or less, tariff is ₹0.
If consumption is between 101 and 200 litres, charge ₹2 per litre for the amount above 100 litres.
If consumption is between 201 and 500 litres, charge ₹200 + ₹3 per litre for the amount above 200 litres.
If consumption is more than 500 litres, charge ₹1,100 + ₹5 per litre for the amount above 500 litres.
If consumption exceeds 1,000 litres, an additional fixed charge of ₹500 is applied.
Display the total water bill.
"""

water = float(input("Enter water consumption in litres : "))

if water <= 100:
  bill = 0
elif water <= 200:
  bill = (water - 100) * 2 

elif water <= 500:
  bill = 100 * 2 + (water - 200) * 3
else :
  bill = 100 * 2 + 300 * 3 + (water - 500) * 5

  if water > 1000:
    bill = bill + 500

print("Total Water bill : ", bill)



"""
3. ⚡ Electricity Bill
Question:
Write a program to calculate an electricity bill according to the units consumed.

Up to 100 units → ₹0 per unit
101–200 units → ₹2 per unit
201–500 units → ₹3 per unit
Above 500 units → ₹5 per unit
Additionally:

If total consumption is more than 500 units, add a fixed surcharge of ₹200.
If consumption is more than 1,000 units, add another ₹500 surcharge.
Display the final electricity bill.
"""

units = float(input("Enter the Units consumed : "))

if units <= 100:
  charge = 0
elif units <= 200:
  charge = (units - 100) * 2
elif units <= 500:
  charge = 100 * 2 + (units - 200) * 3
else:
  charge = (100 * 2 + 300 * 3 + (units - 500) * 5) + 200

  if units > 1000:
    charge = charge + 500

print("Total Bill : ", charge)

"""
4. 🏨 Hotel Room Charges
Question:
A hotel charges customers according to the type of room and number of nights stayed.

Room types:

Standard → ₹2,000 per night
Deluxe → ₹3,500 per night
Suite → ₹5,000 per night
Discounts:

Stay of 1–2 nights → No discount
Stay of 3–5 nights → 10% discount
Stay of more than 5 nights → 20% discount
Additional conditions:

If the customer orders room service, add ₹500 per night.
If the total bill after discount exceeds ₹20,000, add a luxury tax of 5%.
Calculate and display the final bill.
"""

room = input("Enter the room type (Standard/Deluxe/Suite): ")
stay = int(input("Enter the duration of stay: "))

if room == "Standard":
    cost = 2000

elif room == "Deluxe":
    cost = 3500

elif room == "Suite":
    cost = 5000

else:
    print("Invalid room type")
    cost = 0

if cost != 0:

    total = cost * stay

    # Discount
    if stay <= 2:
        discount = 0

    elif stay <= 5:
        discount = total * 0.10

    else:
        discount = total * 0.20

    bill = total - discount

    # Room service
    service = input("Do you want room service? (Yes/No): ")

    if service == "Yes":
        bill = bill + (500 * stay)

    # Luxury tax
    if bill > 20000:
        tax = bill * 0.05
        bill = bill + tax

    print("Final bill:", bill)



"""
5. 🛒 Shopping Discount + Extra Charges
Question:
Write a program to calculate the final shopping bill.

Discount rules:

Bill less than ₹1,000 → No discount
₹1,000–₹4,999 → 5% discount
₹5,000–₹9,999 → 10% discount
₹10,000 or above → 20% discount
Additional conditions:

If the customer is a premium member, give an additional 5% discount.
If the final bill after discount is below ₹500, add a ₹50 handling charge.
If the final bill is above ₹10,000, add ₹200 delivery charges.
Display the final payable amount.
"""

bill = float(input("Enter the total shopping bill: "))
premium_member = input("Are you a premium member? (y/n): ")

if bill < 1000:
    discount = 0

elif bill < 5000:
    discount = bill * 0.05

elif bill < 10000:
    discount = bill * 0.10

else:
    discount = bill * 0.20


if premium_member == "y":
    discount = discount + (bill * 0.05)


final_bill = bill - discount


if final_bill < 500:
    total_bill = final_bill + 50

elif final_bill > 10000:
    total_bill = final_bill + 200

else:
    total_bill = final_bill


print("Total Amount:", total_bill)




"""
6. 🚕 Taxi Fare
Question:
Write a program to calculate taxi fare based on distance travelled.

Fare structure:

First 5 km → ₹100 fixed
Next 10 km → ₹15/km
Above 15 km → ₹20/km
Additional charges:

If the journey is between 10 PM and 6 AM, add 20% night charge.
If the passenger is travelling on a Sunday, add an additional ₹50.
If the total distance is more than 50 km, give a 10% discount on the basic fare.
Display the final taxi fare.
"""

distance = int(input("Enter the distance travelled: "))

time = input("Enter the time of travelling (night/day): ")
day = input("Enter the day: ")


if distance <= 5:
    cost = 100

elif distance <= 15:
    cost = 100 + (distance - 5) * 15

else:
    cost = 100 + (10 * 15) + (distance - 15) * 20


if distance > 50:
    cost = cost - (cost * 0.10)


if time == "night":
    cost = cost + (cost * 0.20)


if day == "Sunday":
    cost = cost + 50

print("Final Taxi Fare:", cost)





"""
7. 📱 Mobile Data Charges
Question:
Write a program to calculate the monthly internet bill based on data usage.

Up to 2 GB → ₹199
More than 2 GB and up to 5 GB → ₹299
More than 5 GB and up to 10 GB → ₹499
More than 10 GB → ₹499 + ₹50 for every additional GB
Additional conditions:

If the customer is a premium user, give 10% discount.
If usage exceeds 20 GB, add an additional ₹100 heavy-usage charge.
Display the final bill.
"""

data = int(input("Enter the data usage in GB: "))
premium = input("Are you a premium user? (y/n): ")

if data <= 2:
    bill = 199

elif data <= 5:
    bill = 299

elif data <= 10:
    bill = 499

else:
    bill = 499 + (data - 10) * 50

# Premium discount
if premium == "y":
    bill = bill - (bill * 0.10)

# Heavy usage charge
if data > 20:
    bill = bill + 100

print("Final Internet Bill:", bill)



"""
8. 🎓 Student Scholarship — Good Conditional Practice
Question:
Write a program to determine whether a student is eligible for a scholarship.

Input:

Percentage
Attendance
Family income
Rules:

A student gets a 100% scholarship if:

Percentage ≥ 90
Attendance ≥ 90%
Family income ≤ ₹3,00,000
A student gets a 50% scholarship if:

Percentage ≥ 80
Attendance ≥ 75%
Family income ≤ ₹5,00,000
Otherwise, the student is not eligible.

Additionally, if percentage ≥ 95 and attendance ≥ 95%, display "Special Merit Scholarship".
"""

percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter family income: "))

# Special Merit Scholarship
if percentage >= 95 and attendance >= 95:
    print("Special Merit Scholarship")

# Scholarship eligibility
if percentage >= 90 and attendance >= 90 and income <= 300000:
    print("100% Scholarship")
elif percentage >= 80 and attendance >= 75 and income <= 500000:
    print("50% Scholarship")
else:
    print("Not Eligible for Scholarship")




"""
9. 🏦 Bank Loan Eligibility — 🔥
Question:
Write a program to determine whether a person is eligible for a bank loan.

Input:

Age
Monthly salary
Credit score
Existing loan amount
Conditions:

Age must be between 21 and 60.
Salary must be at least ₹30,000.
Credit score must be at least 700.
If all three conditions are satisfied:

If existing loan is less than ₹2,00,000 → Loan Approved
If existing loan is between ₹2,00,000 and ₹5,00,000 → Loan Approved with conditions
If existing loan is above ₹5,00,000 → Loan Rejected
Otherwise → Not Eligible.
"""

age = int(input("Enter your age : "))
monthly_salary = float(input("Enter your monthly salary : "))
credit_score = float(input("Enter your credit score : "))
Existing_loan_amount = float(input("Enter the existing loan amount : "))

if 21 <= age <= 60 and salary >= 30000 and credit_score >= 700:
  if Existing_loan_amount <= 200000:
    print("Loan Approved")
  elif Existing_loan_amount <= 500000:
    print("Loan approved with conditions.")
  else:
    print("Loan Rejected.")

else:
    print("Non Eligible") 



"""
10. 🏥 Hospital Bill — 🔥🔥
Question:
Write a program to calculate the final hospital bill.

Input:

Patient type (General / Private)
Number of days
Treatment cost
Room charges:

General → ₹1,000/day
Private → ₹3,000/day
Discount:

Treatment cost below ₹50,000 → No discount
₹50,000–₹1,00,000 → 5%
Above ₹1,00,000 → 10%
Additional charges:

If stay exceeds 10 days → ₹5,000 additional charge.
If patient is a senior citizen (age ≥ 60) → 10% discount on the final bill.
If the final bill exceeds ₹2,00,000 → add 5% medical service tax.
Calculate the final amount payable.
"""


patient_type = input("Enter patient type (General/Private): ")
days = int(input("Enter number of days: "))
treatment_cost = float(input("Enter treatment cost: "))
age = int(input("Enter patient age: "))

# Calculate room charges
if patient_type.lower() == "general":
    room_charge = 1000 * days
elif patient_type.lower() == "private":
    room_charge = 3000 * days
else:
    print("Invalid patient type")
    exit()

# Calculate treatment discount
if treatment_cost < 50000:
    discount = 0
elif treatment_cost <= 100000:
    discount = treatment_cost * 0.05
else:
    discount = treatment_cost * 0.10

# Amount after treatment discount
bill = treatment_cost - discount + room_charge

# Additional charge for stay exceeding 10 days
if days > 10:
    bill += 5000

# Senior citizen discount
if age >= 60:
    bill = bill * 0.90

# Medical service tax
if bill > 200000:
    bill = bill * 1.05

print("Final Amount Payable: ₹", bill)

