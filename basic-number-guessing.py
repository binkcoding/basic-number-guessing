import random

guess = int(input("What's your guess? "))

correct_number = random.randint(1, 11)

while guess != correct_number:
    print("Guess again!")
    if guess >= correct_number:
        print("Lower")
    elif guess <= correct_number:
        print("Higher")
    guess = int(input("What's your guess? "))
else:
    print("You guessed it! ")