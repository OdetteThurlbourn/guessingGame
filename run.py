import random


# Making sure guess value is an integer
def validate_guess(guess):
    if guess.isdigit():
        if not min_range <= int(guess) <= max_range:
            print(f"You need to enter a number... you managed that part, but the number needs "
                    f"to be in the range from {min_range} to {max_range}")
            return False
        return True
    return False


# Defining the random number, min and max range
def game(min_inputted, max_inputted):
    number = random.randint(min_inputted, max_inputted)
    guesses = 0
    while True:
        # Get users guess
        guess = input("Enter your guess: ")
        if not validate_guess(guess):
            print("Invalid input, please enter a number.")
            continue
        # Tally users guess
        guess = int(guess)
        guesses += 1
        another_go = "Guess again"
        # Keeps track of guesses so it knows when to prompt for a hint
        if guesses == 9:
            another_go = "Oh dear..."
        if guess == number:
            plural = "tries"
            if guesses == 1:
                plural = "try"
            print(f"Congratulations! You guessed the correct number in {guesses} {plural}.")
            break
        # Clues for user before hints are prompted
        elif guess > number:
            print(f"Too high! {another_go}.")
        else:
            print(f"Too low! {another_go}.")
        # Breaking loop after failed attempts with 2 hints
        if guesses == 3:
            hint = input("Would you like a hint? (y / n)")
            if hint.lower() == "y":
                if number % 2 == 0:
                    print("Hint: the answer is even.")
                else:
                    print("Hint: the answer is odd.")
        if guesses == 6:
            hint = input("Would you like hint? (y / n)")
            if hint.lower() == "y":
                print("Hint: the answer is a number! \U0001f60a")

        if guesses == 9:
            print("Wow! I can't believe in nine guesses you couldn't get it...lol...Game Over!")
            break
        print(f"You've had {guesses} Guesses so far, only {9 - guesses} to go.")


""" This code block is part of the main function of the program and serves as the initial setup 
for the guessing game."""

if __name__ == "__main__":
    print("Welcome to my guessing game! Try to guess the number and win....nothing!")
    answer = "y"
    correct_guesses = 0
    total_tries = 0
    while answer == "y":
        print("Enter the range of the number you want to guess. ")
        min_range = ""
        max_range = ""
        while min_range == "":
            min_range = input("Enter the minimum range from number:").strip()
            if min_range.isdigit():
                min_range = int(min_range)
            else:
                print("You did not enter a number, please enter a number next time!")
                min_range = ""
        while max_range == "":
            max_range = input("Enter the maximum range from number:").strip()
            if max_range.isdigit():
                max_range = int(max_range)
            else:
                print("You did not enter a number, please enter a number next time!")
                max_range = ""


        """ This code block checks that the minimum value entered is less than the maximum value entered.
        If the user failed to differentiate between the two, the game will swap the two value around
        and the game ill commence. """

        if min_range > max_range:
            print("You really need to know what minimum and maximum means, "
                    "just to help you I am going to swap the numbers around "
                    "in order to have a game today and not next week!")
            temp_holder = max_range
            max_range = min_range
            min_range = temp_holder
        if min_range == max_range:
            print("There really is no hope for you, the number had to be different")
            print("So I am going to use my initiative and make your minimum 1 and your maximum 1000")
            min_range = 1
            max_range = 1000
        print(f"Hey now your minimum is {min_range} and your maximum is {max_range}")
        game(min_range, max_range)
        answer = input("Do you want to play again? (y / n)")
        if answer == "n":
            print("Thank you for playing. Goodbye!")
            exit()