import random
from itertools import count

enter_menu = "Please select difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n\nEnter your choice:"

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have a certain amount of chances to guess the correct number.\n ")
difficulty_choice = input(enter_menu)

difficulty_option = {
    "1": {"name": "Easy", "chances": 10},
    "2": {"name": "Medium", "chances": 5},
    "3": {"name": "Hard", "chances": 3}
}

difficulty = difficulty_option.get(difficulty_choice)

if difficulty:
    guess = int(input(f"Great! You have selected {difficulty['name']}.\nLet's start the game!\n\n Enter your guess: "))
    chances = difficulty["chances"]
    correct_number = random.randint(1, 11)
    while chances >0:
        if guess != correct_number:
            print("Guess again!")
            chances -= 1
            if guess >= correct_number:
                print("Lower")
            elif guess <= correct_number:
                print("Higher")
            guess = int(input("What's your guess? "))
        else:
            print("You guessed it! ")
            break
    else:
        print("You ran out of guesses! ")
    print(chances)
else:
    print("Invalid choice")

#Fin