import random

def validate_guess(guess):
    if not guess.isdigit():
       return False
    else:
      return True

def game(min_range, max_range):
    number = random.randint(min_range, max_range)

    print(f"Welcome to the guessing game! I am thinking of a number between {min_range} and {max_range}.")
    print("Try to guess what it is.")

guesses = 0


while True:
    guess = input("Enter your guess: ")
    if not validate_guess(guess):
        print("Invalid input, please enter a number.")
        continue
    guess = int(guess)
    guesses += 1

    hint = input("Would you like a hint? (y/n)")

    if hint.lower() == "yes":
        if answer % 2 == 0:
            print("Hint: the answer is even.")