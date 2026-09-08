
                         # 1. Classes, Attributes, and Methods

# Question 1 : Create a class Student with an attribute school = "ABC School".Print the school name using the class.

class School:
  school = "ABC School"

print(School.school)  # ABC School

# Question 2 :  Create a class Car with: Attribute: 
# brand = "Toyota" Method: 
# start() that prints "Car Started"
# Access both using the class. 

class Car:
  brand = "Toyota"

  def start():
    print("Car started")

print(Car.brand)  # Toyota
Car.start()       # Car started

# Question 3 : Create a class Laptop with:
# Attribute: company = "Dell"
# Method: specs() that prints "16GB RAM, 512GB SSD"
# Access both.

class Laptop:
  company = "Dell"

  def specs():
    print("16GB RAM, 512GB SSD")

print(Laptop.company) # Dell
Laptop.specs()        # 16GB RAM, 512GB SSD

# Question 4 : Create a class Book with:
# Attribute: title = "Python Basics"
# Method: read() that prints "Reading Python Basics".

class Books:
  tilte = "Python Basics"
  
  def read():
    print("Reading Python Basics")

print(Books.tilte) # Python Basics
Books.read()       # Reading Python Basics

                 # Objects


# Question 5 : Create a class Mobile with:
# Attribute brand = "Samsung"
# Create an object and print the brand.

class Mobile:
  brand = "Samsung"

m = Mobile() 

print(m.brand) # Samsung 

# Question 6 : Create a class Pen with:
# Attribute color = "Blue"
# Create two objects and print the color using both.

class Pen:
  color = "Blue"

trimax = Pen()
Montax = Pen() 

print(trimax.color) # Blue
print(Montax.color) # Blue

# Question 7 : Create a class Fan with:
# Attribute company = "Usha"
# Method rotate() that prints "Fan is rotating"
# Create an object and call the method.

class Fan:
  company = "Usha"

  def rotate(self):
    print("Fan is Rotating")

f1 = Fan() 
print(f1.company)  # Usha
f1.rotate()        # Fan is Rotating 

               # Constructor 

# Question 8 : Create a class Student that accepts name in the constructor.
# Print "My name is <name>".

class Student:
  def __init__(self, name):
    self.name = name 

  def display(self):
    print("My name is", self.name)

a = Student("Anubhav")   
a.display() # My name is Anubhav 


# Question 9 : Create a class Employee with:
# name
# salary
# Method details() to print both.

class Employee:
  def __init__(self, name,salary):
    self.name = name 
    self.salary = salary

  def details(self):
    print("Name :", self.name)
    print("Salary :", self.salary)

b = Employee("Amit", 50000)
b.details()    
       # Name : Amit
       # Salary : 50000

# Question 10 : Create a class Movie with:
# title
# hero
# Method show() to display both.

class Movie:
    def __init__(self, title, hero):
        self.title = title
        self.hero = hero

    def show(self):
        print("Title:", self.title)
        print("Hero:", self.hero)

m = Movie("RockStar", "Imtiaz Ali")
m.show() # Title: RockStar Hero: Imtiaz Ali

# Question 11 : Create a class Phone with:
# brand
# price
# Method details().

class Phone:
  def __init__(self, brand,price):
    self.brand = brand 
    self.price = price

  def details(self):
    print("Brand :", self.brand)
    print("Price :", self.price)

p = Phone("Iphone 15 pro max", 150000)
p.details()  # Brand : Iphone 15 pro max , Price : 150000 

# Question 12 : Create a class Dog.
# Constructor takes name.
# Method bark() prints "Bruno says Woof!".

class Dog:
  def __init__(self, name):
    self.name = name 

  def bark(self):
    print(self.name, "Says Woof") 

d = Dog("Bruno")
d.bark()      # Bruno Says Woof


# Question 13 : Create a class Teacher.
# Constructor takes name.
# Method teach() prints "Mr. Sharma is teaching Python".

class Teacher:
  def __init__(self, name):
    self.name = name 

  def teach(self):
    print("Hello i am ", self.name ,"and i am your teacher")

t = Teacher("Mr. Sharma")

t.teach() # Hello i am  Mr. Sharma and i am your teacher

# Question 14 : Create a class Player.
# Constructor takes name.
# Method play() prints "Virat is playing cricket".

class Player:
  def __init__(self, name):
    self.name = name 

  def play(self):
    print(self.name,"is playing cricket")  

p = Player("Virat")
p.play()  # Virat is playing cricket

# Question 15 : Create a class Bank.
# Class attribute: bank_name = "SBI"
# Class method bank_details() prints the bank name.

class Bank: 
  bank_name = "SBI"

  @classmethod
  def bank_details(cls):
    print("Bank Name :", cls.bank_name)

Bank.bank_details() # Bank Name : SBI

                 # Instance Attributes

# Question 16 : Create a class Bike.
# Constructor takes brand.
# Method show_brand() prints "Bike Brand: Honda".

class Bike:
  def __init__(self, brand):
    self.brand = brand

  def show_brand(self):
    print("Bike Brand :",self.brand)

b1 = Bike("Honda")
b1.show_brand() # Bike Brand : Honda
 
# Question 17 : Create a class Fruit.
# Constructor takes name and color.
# Method details() prints both.

class Fruit:
  def __init__(self, name,color):
    self.name = name 
    self.color = color 

  def details(self):    
    print("Name :", self.name)
    print("Color :", self.color)

f1 = Fruit("Apple","Red")
f1.details()    # Name : Apple , Color : Red

# Question 18 : Create a class Animal.
# Constructor takes animal_name.
# Method sound() prints "<animal_name> makes a sound".

class Animal:
  def __init__(self, animal_name):
    self.animal_name = animal_name 

  def sound(self):
    print(self.animal_name, "Makes a sound.")

a1 = Animal("Dog")
a1.sound()  # Dog Makes a sound.


# Question 19 : Create a class City.
# Constructor takes city_name and state.
# Method display() prints both.

class City:
  def __init__(self, city_name,state):
    self.city_name = city_name
    self.state = state

  def display(self):
    print("City :",self.city_name) 
    print("State :",self.state)

c1 = City("Dehradun", "Uttrakhand")
c1.display()    # City : Dehradun , State : Uttrakhand

# Question 20 : Create a class Laptop.
# Constructor takes company and price.
# Method info() prints:
# Company : Dell
# Price : 60000

class Laptop:
  def __init__(self,company,price):
    self.company = company 
    self.price = price 

  def info(self):
    print("Company :", self.company)
    print("Price :",self.price)

l = Laptop("Dell", 60000)
l.info()        # Company : Dell , Price : 60000


                 # Updating Object Attributes

# Question 21 : Create a class Student.
# Constructor takes name.
# Create an object with name = "Rahul".
# Change the name to "Rohan".
# Print the updated name.

class Student:
  def __init__(self,name):
    self.name = name 
  
s1 = Student("Rahul")
s1.name = "Rohan"
print(s1.name)  # Rohan




# Question 22 : Create a class Car.
# Constructor takes brand.
# Create an object with brand = "Toyota".
# Change the brand to "BMW".
# Print the updated brand.

class Car:
  def __init__(self,brand):
    self.brand = brand
car = Car("Toyota")
car.brand = "BMW"
print(car.brand)     # BMW




# Question 23 : Create a class Mobile.
# Constructor takes brand and price.
# Create an object.
# Change only the price.
# Print both brand and updated price.

class Mobile:
  def __init__(self,brand,price):
    self.brand = brand
    self.price = price
  def info(self):
    print("Brand :",self.brand)
    print("Price :",self.price)  

mobile = Mobile("Iphone",150000)
mobile.price = 50000
mobile.info()  # Brand : Iphone, Price : 50000


                 # Multiple Objects

# Question 24 : Create a class Employee.
# Constructor takes name.
# Create two objects:
# "Amit"
# "Neha"
# Print both names.

class Employee:
  def __init__(self,name):
    self.name = name 

E1 = Employee("Amit")
E2 = Employee("Neha")

print(E1.name) # Amit
print(E2.name) # Neha 



# Question 25 : Create a class Book.
# Constructor takes title.
# Create three book objects.
# Print all book titles.

class Book:
  def __init__(self,title):
    self.title = title 
b1 = Book("Python")
b2 = Book("Java")
b3 = Book("C++")

print(b1.title) # Python
print(b2.title) # Java
print(b3.title) # C++ 

                 # Default Constructor Values

# Question 26 : Create a class Student.
# Constructor takes name with default value "Unknown".
# Create one object without passing a name.
# Print the name.

class Students:
  def __init__(self, name="Unknown"):
    self.name = name 

s1 = Students()
print(s1.name)    



# Question 27 : Create a class Dog.
# Constructor takes name with default value "Tommy".
# Method bark() prints "<name> says Woof!".

class Dog:
  def __init__(self,name="Tommy"):
    self.name = name 

  def bark(self):
    print(self.name,"says Woof !")

d1 = Dog()
d1.bark()  # Tommy says Woof !


                 # Using self

# Question 28 : Create a class Rectangle.
# Constructor takes length and width.
# Method area() prints the area.

class Rectangle: 
  def __init__(self, length,width):
    self.length = length
    self.width = width

  def area(self):
    print("Area :", self.length * self.width)

r = Rectangle(10,15)
r.area()  # Area : 150 


# Question 29 : Create a class Square.
# Constructor takes side.
# Method perimeter() prints the perimeter.
class Square:
  def __init__(self, side):
    self.side = side

  def perimeter(self):
    print("Perimeter:", 4 * self.side)

a = Square(5)
a.perimeter()    # Perimeter: 20     

# Question 30 : Create a class Circle.
# Constructor takes radius.
# Method diameter() prints the diameter.

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def diameter(self):
    print("Diameter:", 2 * self.radius)  

c = Circle(6)
c.diameter()   # Diameter: 12

                 # Class Attributes

# Question 31 : Create a class School.
# Class attribute: school_name = "ABC Public School"
# Constructor takes student_name.
# Method details() prints:
# Student : Rahul
# School : ABC Public School
class School:
  school_name = "ABC Public School"


  def __init__(self, student_name):
    self.student_name = student_name

  def details(self):
    print("Student:", self.student_name) 
    print("School:", self.school_name) 

s = School("Rahul")
s.details()  # School: ABC Public School

# Question 32 : Create a class Company.
# Class attribute: country = "India"
# Constructor takes company_name.
# Method info() prints both.

class Company:
  country = "India"

  def __init__(self,company_name):
    self.company_name = company_name

  def info(self):
    print("Company:",self.company_name)
    print("Country:",Company.country)

c = Company("TCS")
c.info()        # Company: TCS , Country: India 


            # Polymorphism 

# Queston 33 : Write a program to demonstrate method overloading.
class Calculator:
  def add(self,a,b,c=0):
    return a+b+c 

obj = Calculator()

print("Sum of 2 numbers",obj.add(10,20))
print("Sum of 3 numbers",obj.add(10,20,30))


# Queston 34 : Create a class Animal with a method sound(). Derive classes Dog, Cat, and Cow that override the sound() method.
class Animal:
  def sound(self):
    print("Animal makes a sound")

class Dog(Animal):
  def sound(self):
    print("Dog Barks")

class Cat(Animal):
  def sound(self):
    print("Cat,meows")

class Cow(Animal):
  def sound(self):
    print("Cow, moos")

animals = [Dog(), Cat(), Cow()]

for animals in animals:
  animals.sound() 

# Queston 35 : Write a program showing runtime polymorphism using a parent class reference.
class Animal:
  def sound(self):
    print("Animal makes a sound")

class Dog(Animal):
  def sound(self):
    print("Dog barks")

obj = Dog()
obj.sound() 

# Queston 36 : Write a program that calculates the area of different shapes using method overloading.

class Area:
  def calculate(self,a,b=None):
    if b is None:
      return 3.14 * a * a 
    else:
      return a * b 

obj = Area()
print("Area of Circle =", obj.calculate(5))
print("Area of Rectangle =", obj.calculate(4,5))


# Queston 37 : Create a banking application where different account types override the calculateInterest() method.
class Account:
  def calculate_interest(self):
    print("General Interest")
class Savings(Account):
  def calculate_interest(self):
    print("Saving Interest: 6 %")
class Current(Account):
  def calculate_interest(self):
    print("Current Interest : 5 %")    

accounts = [Savings(),Current()]

for account in accounts:
  account.calculate_interest()

# Queston 38 : Implement a payment system with classes CreditCard, UPI, and NetBanking using polymorphism.
class Payment:
  def pay(self):
    print("Payment Processing")

class NetBanking(Payment):
  def pay(self):
    print("Paid using Net Banking")    

class UPI(Payment):
  def pay(self):
    print("Paid using UPI")

class CreditCard(Payment):
  def pay(self):
    print("Paid using Credit Card")

payments = [NetBanking(),UPI(),CreditCard()]

for payment in payments :
  payment.pay()


# Queston 39 : Create an employee salary system where different employee types calculate salary differently.

class Employee:
  def salary(self):
    print("Basic Salary")
class Manager(Employee):
  def salary(self):
    print("Manager Salary = ₹80,000")
class Developer(Employee):
  def salary(self):
    print("Developer Salary = ₹60,000")

employees = [Manager(),Developer()]
for employee in employees:
  employee.salary()


# Queston 40 : Write a menu-driven program using runtime polymorphism.

class Animal:
  def sound(self):
    print("Animal Makes a Sound")

class Dog(Animal):
  def sound(self):
    print("Dog Barks")

class Cat(Animal):
  def sound(self):
    print("Cat,meows")

class Cow(Animal):
  def sound(self):
    print("Cow, moos")

print("1. Dog")    
print("2. Cat")    
print("3. Cow")    

choice = int(input("Enter your choice number :"))

if choice == 1:
  animal = Dog()
elif choice == 2:
  animal = Cat()
elif choice == 3:
  animal == Cow()
else: 
  print("Invalid Choice")
  exit()

animal.sound() 