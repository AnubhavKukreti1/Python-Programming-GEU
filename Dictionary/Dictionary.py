# Dictionary  = A dictionary stores data in key-value pairs.  

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

# "name" => key 
# "Rahul" => value
# "age" => key
# 20 => value
# "course" => key
# "Python" => value

# creating a dictionary 

person = {
    "name": "Aman",
    "age": 21,
    "city": "Dehradun"
}

print(person)   #  {'name': 'Aman', 'age': 21, 'city': 'Dehradun'}
 

# Accessing Values 

person = {
    "name": "Aman",
    "age": 21
}

print(person["name"])
print(person["age"])

# Aman
# 21


# Adding Items to a Dictionary

person = {
    "name": "Aman",
    "age": 21
}

person["city"] = "Dehradun"

print(person)

# {'name': 'Aman', 'age': 21, 'city': 'Dehradun'}


# Changing Values in a Dictionary

person = {
    "name": "Aman",
    "age": 21
}

person["age"] = 22

print(person)
# {'name': 'Aman', 'age': 22}

# Removing Items from a Dictionary

person = {
    "name": "Aman",
    "age": 21,
    "city": "Dehradun"
}

person.pop("age")

print(person)
# {'name': 'Aman', 'city': 'Dehradun'}

# Checking if a Key Exists in a Dictionary

person = {
    "name": "Aman",
    "age": 21
}

print("name" in person)
print("city" in person)

# True
# False

# Getting Keys and Values from a Dictionary

person = {
    "name": "Aman",
    "age": 21,
    "city": "Dehradun"
}

print(person.keys())
print(person.values())
# dict_keys(['name', 'age', 'city'])
# dict_values(['Aman', 21, 'Dehradun'])

# looping in a dictionary

student = {
    "name": "Aman",
    "age": 21,
    "marks": 90
}

for key in student:
    print(key)

# name
# age
# marks

# looping through values in a dictionary
for value in student.values():
    print(value)

# Aman

# Looping through key-value pairs in a dictionary
for key, value in student.items():
    print(key, value)

# name Aman
# age 21
# marks 90
  

# Nested Dictionaries

students = {
    "student1": {
        "name": "Aman",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}

print(students["student2"]["age"])
# 21
