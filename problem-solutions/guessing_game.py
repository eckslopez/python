import random 
number = random.randint(0,10) 
print(number)
guess = int(input("Guess a number between 0 and 10\n"))

if guess > number:
    print("You guessed too high!")
elif guess < number:
    print("You guess too low!")
elif guess == number:
    print("You're a winner in life!")
