import random

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
                print("Hint: the answer is a number! \U0001f60a")

        if guesses == 9 and hint_used == hint_used2 and guess != number:
            print("Sorry! Game Over!")
            break
        print(f"Guesses: {guesses}")
        print(f"Hint Used: {hint_used}")
        print(f"Guess: {guess}")
        print(f"Number: {number}")
        print(f"hint_used2: {hint_used2}")
            

    return correct_guesses, total_tries, hint_used

# The code below was in collaboration with Mentor Spencer Barriball
if __name__ == '__main__':
    print("Welcome to my guessing game! Try to guess the number and win....nothing!")
    answer = "y"
    correct_guesses = 0
    total_tries = 0
    hint_used = False
    hint_used2 = False
    while answer == "y":
        print("Enter the range of the number you want to guess. ")
        min_range = ''
        max_range = ''
        while min_range == '':
            min_range = input("Enter the minimum range from number:").strip()
            if min_range.isdigit():
                min_range = int(min_range)
            else:
                print('You did not enter a number, please enter a number next time!')
                min_range = ''
        while max_range == '':
            max_range = input("Enter the maximum range from number:").strip()
            if max_range.isdigit():
                max_range = int(max_range)
            else:
                print('You did not enter a number, please enter a number next time!')
                max_range = ''
        # check that min is less than max
        if min_range > max_range:
            print('You really need to know what minimum and maximum means, '
                  'just to help you I am going to swap the numbers around '
                  'in order to have a game today and not next week!')
            temp_holder = max_range
            max_range = min_range
            min_range = temp_holder
        if min_range == max_range:
            print('There is really is no hope for you, the number had to be different')
            print('So I am going to use my initiative and make your minimum 1 and your maximum 1000')
            min_range = 1
            max_range = 1000
        print(f'Hey now your minimum is {min_range} and your maximum is {max_range}')
        play_again = game(min_range, max_range)
        answer = input("Do you want to play again? (y/n)")
        if answer == 'n':
            print("Thank you for playing. Goodbye!")
            break

