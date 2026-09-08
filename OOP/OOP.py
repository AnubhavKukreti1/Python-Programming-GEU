class hello:
  a = 12        #attribute 

  def hello():  #method
    print("Hello Guys")

# How to access Attributes and Methods 
# You can access attributes and methods after accessing the class

print(hello.a)  #accessing Attributes 
hello.hello()   #accessing Methods 


# Objects 

class Bags:
  name = "Skybags"

  def details():
    print("This is a company which creates bags")

Rebook = Bags() 

print(Rebook.name)


class Animals: 
  a = 12 

  def __init__(self,name): #objects/instance attributes 
    self.name = name 

  def hello(self): # instance/object method captures the location of object 
    print(f"I am {self.name}")

  @classmethod # class method captures the location of a class 
  def detail(cls):
    print(f"How are you ")
  
  @staticmethod #this is a static method and it will not target any location
  def speak():
    print(f"Hello how are you i am a static method")

obj = Animals("Lion")    

obj.hello()
obj.detail()
Animals.speak()
print(Animals.hello)

# Inheritance 

class Animal: # Child class
  a = 12
  def __init__(self,name):
    self.name = name 

  def speak(self):
    print("Animal sound")  

  def details(self):
    print(f"Hello {self.name} how are you")  

class Humans(Animal): # Parent class 
  pass

class Dog(Animal):
  def speak(self):
    print("Bhau Bhau")

dg = Dog("Bruno")
dg.speak()
obj = Animal("Lion")
obj2 = Humans("Abhinav")
obj2.details()
print(obj2.a)

# Your child class objects has all the powers to access the attributes and methods of parent class.

# Multilevel inheritance


class BagFactory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def details(self):
        print("Your bag details are:")
        print("Material :", self.material)
        print("Zips :", self.zips)
        print("Pockets :", self.pockets)


class Reebok(BagFactory):
    def __init__(self, material, zips, pockets, color):
        super().__init__(material, zips, pockets)
        self.color = color

    def details(self):
        super().details()
        print("Color :", self.color)


class Campus(BagFactory):
    def __init__(self, material, zips, pockets, color, size):
        super().__init__(material, zips, pockets)
        self.color = color
        self.size = size

    def details(self):
        super().details()
        print("Color :", self.color)
        print("Size :", self.size)


bag1 = BagFactory("Leather", 3, 4)

bag2 = Reebok("Polyester", 4, 2, "Blue")

bag3 = Campus("Leather", 5, 3, "Black", "Large")


bag2.details()

print()

bag3.details()

# multiple inheritance 

class Animal: 
  def __init__(self, name):
    self.name = name 

class Humans:
  def __init__(self,id):
    self.id = id 

class Robots(Humans, Animal):
  def __init__(self, id,name):
    Humans.__init__(self,id)
    Animal.__init__(self,name)

robo = Robots(12, "abhinav")    

print(robo.id)
print(robo.name)

          #  Polymorphism 

          #  Poly = many , Morphism = forms 


def hello():
  print("How are you")

def hello():
  print("What are you doing")

hello() 


class Animals:
  def speak(self):
    print("Animal will not speak")

class Humans:
  def speak(self):
    print("we are humans we can speak")

obj = Animals()
obj2 = Humans()

obj.speak()  # Animal will not speak
obj2.speak() #we are humans we can speak


# Method overriding (we need inheritance)

class Animals:
    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"Your name is {self.name}")


class Humans(Animals):
    def __init__(self, name):
        super().__init__(name)

    def info(self):
        self.a = 23
        print(f"Your info is {self.name} and this is all we have")


obj = Humans("Harsh")

obj.details()
obj.info()
print(obj.a)


# When we are doing inheritance and parent and child clases have same method name so the child class method will override the parent class method 

class Hello:
  def speak(self,a):
    print(f"Hello how are you")


  def speak(self,a,b):
    print("How are you ?")

   #            Encapsulation              
#Encapsulation => Bundling data (variables) and methods (functions) together inside a class, while controlling direct access to the data.


class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin

    def check_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        return "Incorrect PIN"

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Incorrect PIN"

        if amount > self.__balance:
            return "Insufficient Balance"

        self.__balance -= amount
        return f"₹{amount} Withdrawn Successfully"


acc = BankAccount("Rahul", 8000000, 1234)

print(acc.check_balance(1234))
print(acc.withdraw(90000, 1234))
print(acc.check_balance(1234))


 #        Abstraction 
# Abstraction => Showing only the essential features of an object while hiding the complex implementation details.

from abc import ABC, abstractclassmethod

class enforce(ABC):
  @abstractclassmethod
  def enginestart():
    pass 

class bike(enforce):
  def enginestart():
    pass  

class car(enforce):
  def enginestart():
    pass 

class truck:
  pass 

obj1 = bike()
obj2 = car()
obj3 = truck()

# Types of Methods

# Instance Method 

class Student:
  def show(self):
    print("Instance method")

# Class Method 
# uses @classmethod 

class Student:
  school = "ABC"

  @classmethod
  def show_school(cls):
    print(cls.show_school)

Student.show_school()

# Static Method 
# uses @staticmethod 

class Math:
  @staticmethod
  def add(a,b):
    return a+b 

print(Math.add(10,100))
    