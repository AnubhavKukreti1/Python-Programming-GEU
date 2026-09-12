Python Loops — Complete Notes
1. What are Loops?

A loop is used to execute a block of code repeatedly.

Instead of writing:

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")


we can use a loop:

for i in range(5):
    print("Hello")


Python mainly has two types of loops:

for loop
while loop
2. for Loop

A for loop is used when we want to iterate over a sequence or repeat something a specific number of times.

Syntax
for variable in sequence:
    # code

Example
for i in range(5):
    print(i)


Output:

0
1
2
3
4

3. range() Function

The range() function is commonly used with for loops.

range(stop)
for i in range(5):
    print(i)


Output:

0
1
2
3
4


The stop value is not included.

range(start, stop)
for i in range(2, 7):
    print(i)


Output:

2
3
4
5
6

range(start, stop, step)
for i in range(1, 10, 2):
    print(i)


Output:

1
3
5
7
9


Here:

start = 1
stop = 10
step = 2
4. Reverse Loop

We can use a negative step to loop backwards.

for i in range(10, 0, -1):
    print(i)


Output:

10
9
8
7
6
5
4
3
2
1

5. Looping Through a String

A for loop can iterate through each character of a string.

name = "Python"

for char in name:
    print(char)


Output:

P
y
t
h
o
n

6. Looping Through a List
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


Output:

apple
banana
mango

7. Looping Through a Tuple
numbers = (10, 20, 30, 40)

for num in numbers:
    print(num)

8. Looping Through a Dictionary
Keys
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Delhi"
}

for key in student:
    print(key)

Values
for value in student.values():
    print(value)

Both keys and values
for key, value in student.items():
    print(key, value)

9. while Loop

A while loop executes a block of code as long as a condition is True.

Syntax
while condition:
    # code

Example
i = 1

while i <= 5:
    print(i)
    i += 1


Output:

1
2
3
4
5

10. Important: Updating the Variable

Always make sure the condition of a while loop eventually becomes False.

Correct:

i = 1

while i <= 5:
    print(i)
    i += 1


If we forget i += 1:

i = 1

while i <= 5:
    print(i)


the loop becomes an infinite loop because i always remains 1.

11. Infinite Loop

An infinite loop never stops.

Example:

while True:
    print("Hello")


This keeps running until the program is stopped.

12. break Statement

break is used to immediately stop a loop.

Example:

for i in range(1, 10):
    if i == 5:
        break
    print(i)


Output:

1
2
3
4


When i becomes 5, the loop stops.

13. continue Statement

continue skips the current iteration and moves to the next iteration.

Example:

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


Output:

1
2
4
5


3 is skipped.

14. pass Statement

pass does nothing.

It is useful when we need a statement syntactically but don't want to execute anything yet.

for i in range(5):
    pass

15. break vs continue vs pass
Statement	Purpose
break	Stops the loop completely
continue	Skips current iteration
pass	Does nothing
16. Nested Loops

A loop inside another loop is called a nested loop.

Example:

for i in range(3):
    for j in range(3):
        print(i, j)


The inner loop runs completely for every iteration of the outer loop.

17. Nested Loop Example — Pattern
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()


Output:

*
**
***
****

18. else with Loops

Python allows an else block with loops.

Example:

for i in range(5):
    print(i)
else:
    print("Loop completed")


Output:

0
1
2
3
4
Loop completed


The else block executes when the loop finishes normally.

19. Loop else with break

If the loop is terminated using break, the else block does not execute.

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")


Output:

0
1
2


The else block is skipped because break was used.

20. for Loop vs while Loop
for Loop	while Loop
Used for iterating over sequences	Used when a condition controls repetition
Often used when number of iterations is known	Often used when number of iterations is unknown
Works naturally with strings, lists, tuples, etc.	Mainly condition-based
Example: for x in range(10)	Example: while x < 10
21. Common Loop Mistakes
Mistake 1: Forgetting indentation

Wrong:

for i in range(5):
print(i)


Correct:

for i in range(5):
    print(i)

Mistake 2: Forgetting to update a while loop

Wrong:

i = 1

while i <= 5:
    print(i)


Correct:

i = 1

while i <= 5:
    print(i)
    i += 1

Mistake 3: Confusing break and continue
break


means stop the loop.

continue


means skip this iteration.

22. Useful Loop Patterns
Print numbers 1 to 10
for i in range(1, 11):
    print(i)

Print even numbers
for i in range(2, 11, 2):
    print(i)

Print odd numbers
for i in range(1, 11, 2):
    print(i)

Find sum of numbers
total = 0

for i in range(1, 11):
    total += i

print(total)


Output:

55

Multiplication table
n = 5

for i in range(1, 11):
    print(n * i)

