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

    

