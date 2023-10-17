import random
roll = random.randint(1,6)
guess = int(input("Guess the dice roll:\n"))
if guess == roll:
    print("You guessed it correctly!")
else: 
    print("Wrong!")