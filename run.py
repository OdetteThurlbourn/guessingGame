import random

print("Welcome to my guessing game!")

# min_range = int(input("Enter a minimum number: "))
# max_range = int(input("Enter a maximum number: ")) 
# answer = random.randint(min_range, max_range)
# guesses = 0

# Making sure guess value is an integer
def validate_guess(guess):
    if not guess.isdigit():
        return False
    else:
        return True

def game(min_range, max_range):
    number = random.randint(min_range, max_range)
    guesses = 0
    while True:
        # Get users guess
        guess = input("Enter your guess: ")
        if not validate_guess(guess):
            print("Invalid input, please enter a number.")
            continue
        guess = int(guess)
        guesses += 1

        if guess == number:
            print("Congratulations! You guessed the correct number in", guesses, "tries.")
            play_again = input("Do you want to play again? (y/n) ")
            break
        elif guess > number:
            print("Too high! Guess again.")
        else:
            print("Too low! Guess again.")
            
        hint = input("Would you like a hint? (y/n)")

        if hint.lower() == "y":
            if number % 2 == 0:
                print("Hint: the answer is even.")
            else:
                print("Hint: the answer is odd.")

play_again ="y"
while play_again == "y":
    print("Enter the range of the number you want to guess. ")
    min_range = int(input("Enter the minimum range:"))
    max_range = int(input("Enter the maximum range:"))
    if game(min_range, max_range):
        play_again = input("Do you want to play again? (y/n) ")
    else:
        print("Something went wrong! Please try again.")
