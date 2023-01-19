import random

print("Welcome to my guessing game!")

# Making sure guess value is an integer
def validate_guess(guess):
    if not guess.isdigit():
        return False
    else:
        return True


def game(min_range, max_range):
    correct_guesses = 0
    total_tries = 0
    hint_used = False
    hint_used2 = False
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
        total_tries += guesses

        if guess == number:
            correct_guesses += 1
            print("Congratulations! You guessed the correct number in", guesses, "tries.")
            hint_used = False
            hint_used2 = False
            play_again = input
            guesses = 0
            break
        elif guess > number:
            print("Too high! Guess again.")
        else:
            print("Too low! Guess again.")


        if guesses == 3 and hint_used == False:
            hint = input("Would you like a hint? (y/n)")
            if hint.lower() == "y":
                hint_used = True
                if number % 2 == 0:
                    print("Hint: the answer is even.")
                else:
                    print("Hint: the answer is odd.")
        if guesses == 6 and hint_used2 == False:
            hint = input("Would you like another hint? (y/n)")
            if hint.lower() == "y":
                hint_used2 = True
                print("Hint: the answer is between",min_range, "and", max_range)

    return correct_guesses, total_tries, hint_used
       
play_again = "y"
correct_guesses = 0
total_tries = 0
hint_used = False
hint_used2 = False
while play_again == "y":
    print("Enter the range of the number you want to guess. ")
    min_range = int(input("Enter the minimum range:"))
    max_range = int(input("Enter the maximum range:"))
    correct_guesses
    play_again = game(min_range, max_range)
    play_again = input("Do you want to play again? (y/n)")
    if play_again == 'n':
        print("Thank you for playing. Goodbye!")
        break