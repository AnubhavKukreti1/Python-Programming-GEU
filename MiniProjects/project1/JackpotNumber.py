""" This is my project 1 for the mini projects. The project is to create a simple game where the user has to guess a randomly generated number between 1 and 100. The program will give hints if the guess is too low or too high, and will continue to prompt the user until they guess the correct number. Once the correct number is guessed, the program will congratulate the user. """

import random 

JackpotNumber = random.randint(1, 100)

guess = int(input("Guess the Jackpot Number (between 1 and 100): "))


while guess != JackpotNumber :
    if guess < JackpotNumber:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    guess = int(input("Guess the Jackpot Number (between 1 and 100): ")) 

else :
    print("Congratulations! You've guessed the Jackpot Number:", JackpotNumber)



