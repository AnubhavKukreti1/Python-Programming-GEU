"""
PYTHON PRACTICE PROGRAMS
========================

1. Frequency Counter
2. Anagram Checker
3. Find Missing Number
4. Number Guessing Game
5. Password Strength Checker
6. Simple Calculator
7. Student Grade System
8. To-Do List
"""


# ============================================================
# 1. FREQUENCY COUNTER
# ============================================================

def frequency_counter():
    """
    Frequency Counter
    Given a string, count how many times each character appears.

    Example:
    "banana"

    Output:
    b → 1
    a → 3
    n → 2
    """

    text = input("Enter a string: ")

    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    print("\nCharacter Frequency:")

    for char, count in frequency.items():
        print(char, "→", count)


# ============================================================
# 2. ANAGRAM CHECKER
# ============================================================

def anagram_checker():
    """
    Anagram Checker
    Check whether two strings are anagrams.

    Example:
    "listen" and "silent" → Anagram
    """

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if sorted(str1) == sorted(str2):
        print("Anagram")
    else:
        print("Not an Anagram")


# ============================================================
# 3. FIND MISSING NUMBER
# ============================================================

def find_missing_number():
    """
    Find Missing Number

    You have numbers from 1 to n,
    but one number is missing.

    Example:
    [1, 2, 3, 5, 6]

    Output:
    4
    """

    numbers = [1, 2, 3, 5, 6]

    print("Numbers:", numbers)

    n = len(numbers) + 1

    # Sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2

    # Sum of numbers in the list
    actual_sum = sum(numbers)

    # Difference is the missing number
    missing_number = expected_sum - actual_sum

    print("Missing number:", missing_number)


# ============================================================
# 4. NUMBER GUESSING GAME
# ============================================================

def number_guessing_game():
    """
    Number Guessing Game

    Generate a random number between 1 and 100.
    Keep asking the user to guess until they find it.
    """

    import random

    secret_number = random.randint(1, 100)

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!")

    attempts = 0

    while True:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low!")

        elif guess > secret_number:
            print("Too high!")

        else:
            print("Congratulations! You guessed it!")
            print("Number of attempts:", attempts)
            break


# ============================================================
# 5. PASSWORD STRENGTH CHECKER
# ============================================================

def password_strength_checker():
    """
    Password Strength Checker

    Password must:
    - Have at least 8 characters
    - Contain an uppercase letter
    - Contain a lowercase letter
    - Contain a number
    - Contain a special character
    """

    password = input("Enter your password: ")

    has_length = len(password) >= 8
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    for char in password:

        if char.isupper():
            has_uppercase = True

        elif char.islower():
            has_lowercase = True

        elif char.isdigit():
            has_number = True

        else:
            has_special = True

    if (
        has_length
        and has_uppercase
        and has_lowercase
        and has_number
        and has_special
    ):
        print("Strong password!")

    else:
        print("Weak password!")

        print("\nRequirements:")

        if has_length:
            print("✓ At least 8 characters")
        else:
            print("✗ At least 8 characters")

        if has_uppercase:
            print("✓ Uppercase letter")
        else:
            print("✗ Uppercase letter")

        if has_lowercase:
            print("✓ Lowercase letter")
        else:
            print("✗ Lowercase letter")

        if has_number:
            print("✓ Number")
        else:
            print("✗ Number")

        if has_special:
            print("✓ Special character")
        else:
            print("✗ Special character")


# ============================================================
# 6. SIMPLE CALCULATOR
# ============================================================

def simple_calculator():
    """
    Simple Calculator

    Accepts:
    number operator number

    Example:
    10 + 5

    Output:
    15
    """

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Please enter valid numbers.")
        return

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":

        if num2 == 0:
            print("Cannot divide by zero.")
            return

        result = num1 / num2

    else:
        print("Invalid operator.")
        return

    print("Output:", result)


# ============================================================
# 7. STUDENT GRADE SYSTEM
# ============================================================

def student_grade_system():
    """
    Student Grade System

    Take marks for 5 subjects.
    Calculate percentage and assign grade.

    90+  → A
    80-89 → B
    70-79 → C
    60-69 → D
    Below 60 → F
    """

    total = 0

    print("\nEnter marks for 5 subjects.")

    for i in range(1, 6):

        while True:

            try:
                marks = float(input(f"Enter marks for subject {i}: "))

                if 0 <= marks <= 100:
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

        total += marks

    percentage = total / 5

    if percentage >= 90:
        grade = "A"

    elif percentage >= 80:
        grade = "B"

    elif percentage >= 70:
        grade = "C"

    elif percentage >= 60:
        grade = "D"

    else:
        grade = "F"

    print("\n===== RESULT =====")
    print("Total marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)


# ============================================================
# 8. TO-DO LIST
# ============================================================

def todo_list():
    """
    Bonus Challenge: To-Do List

    Options:
    1. Add a task
    2. View tasks
    3. Remove a task
    4. Exit
    """

    tasks = []

    while True:

        print("\n===== TO-DO LIST =====")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Add task
        if choice == "1":

            task = input("Enter task: ")

            if task.strip():
                tasks.append(task)
                print("Task added!")

            else:
                print("Task cannot be empty.")

        # View tasks
        elif choice == "2":

            if len(tasks) == 0:
                print("No tasks available.")

            else:
                print("\nYour Tasks:")

                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        # Remove task
        elif choice == "3":

            if len(tasks) == 0:
                print("No tasks to remove.")

            else:

                print("\nYour Tasks:")

                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

                try:
                    task_number = int(
                        input("Enter task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):

                        removed_task = tasks.pop(task_number - 1)

                        print("Removed:", removed_task)

                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        # Exit
        elif choice == "4":

            print("Exiting To-Do List...")
            break

        else:
            print("Invalid choice. Please try again.")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 50)
        print("       PYTHON PRACTICE PROGRAMS")
        print("=" * 50)

        print("1. Frequency Counter")
        print("2. Anagram Checker")
        print("3. Find Missing Number")
        print("4. Number Guessing Game")
        print("5. Password Strength Checker")
        print("6. Simple Calculator")
        print("7. Student Grade System")
        print("8. To-Do List")
        print("9. Exit")

        print("=" * 50)

        choice = input("Choose a program (1-9): ")

        if choice == "1":
            frequency_counter()

        elif choice == "2":
            anagram_checker()

        elif choice == "3":
            find_missing_number()

        elif choice == "4":
            number_guessing_game()

        elif choice == "5":
            password_strength_checker()

        elif choice == "6":
            simple_calculator()

        elif choice == "7":
            student_grade_system()

        elif choice == "8":
            todo_list()

        elif choice == "9":
            print("Thank you! Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-9.")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()
