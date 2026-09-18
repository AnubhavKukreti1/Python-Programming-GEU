# Homogenous tuple 

t1 = (1,2,3)
print(type(t1))   #<class 'tuple'>


# Heterogenous tuple

t2 = (1, "Hello", 3.4)
print(type(t2))   #<class 'tuple'>

a = 4
print(id(a))
print(hex(id(a)))

print(a)

b = a
print(id(b))
print(hex(id(b)))

del a 
print(b)


import sys 

a = "A"
b = a 
c = b 

print(sys.getrefcount(a))

d = 1 
e = d 
f = e 

print(sys.getrefcount(d))



a = (1,2,3)

print(id(a))

a = a + (4 , 5)
print(id(a))
print(a)