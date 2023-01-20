# Command Line Interface Python Guessing Game
_________________________________________

![responsePP3](https://user-images.githubusercontent.com/108287233/213483220-a3ff5669-80d9-4bfe-a626-bec4e7f04295.png)

_______________________________________________

A simple web-based guessing game built using Python and Flask that generates a random number and prompts the user to guess the number. The program will then check if the user's guess is correct and provide feedback on whether the guess is too high or too low. The user can continue guessing until they correctly guess the number. The program can also keep track of the number of guesses the user has made and provide a message of congratulations upon guessing the correct number.

## How to Play
__________________________________
1. Visit the website at **[Guessing Game](https://guessinggamepy.herokuapp.com/)**.
2. The game will prompt you to enter a minimum number and a maximum number, you decide. Press enter to confirm.
3. Now enter your guess between the mimimum and maximum numbers you set. Press enter to confirm.
4. The game will indicate if you guessed correctly on your first try or if you should guess again because the guess was incorrect.
5. The game will give clues along the way whether you inserted a number that was to high or to low.
6. After 3 incorrect guess the game will ask if you would like a hint.  By using the letters 'y' or 'n' you can indictae your response. Press enter to confirm.
7. If you selected 'y', the game will spill out another hint wether the number is odd or even.
8. If after 3 more tries you cannot guess the number the game will spill out yet another hint.
9. If you do guess the correct number a message of congratulations will appear.
10. The game will then prompt you to either play again or end the game using the 'y' for yes and 'n' for no. Press enter to confirm.
11. The game will restart if you selected 'y' or end with a goodbye message if you slected 'n'.
12. If the user would enter the numbers in the wromg order, for example: a 10 for minimum and a 5 for maximum, the game will tell display the following message: **"You really need to know what minimum and maximum means,
                  just to help you I am going to swap the numbers around
                  in order to have a game today and not next week!"**
13. The game will then swap the numbers around and the game will commence. 

### User enters minimum and maximum range
![enterMinMax](https://user-images.githubusercontent.com/108287233/213653249-2161fd75-0fa9-4708-bbe8-266b61269388.png)

### Reverse values if user enter incorrectly
![gamePlayMinMaxReverse](https://user-images.githubusercontent.com/108287233/213515754-51d793a8-6b1c-404f-8a01-fe1504fd9575.png)

### Only enter answers within the set range
![invalidRange](https://user-images.githubusercontent.com/108287233/213654262-f2150edb-ded7-4e47-af4f-f92c8c4b22a4.png)

### Only intergers are valid - The game can only accept number values
![enterNumber001](https://user-images.githubusercontent.com/108287233/213653803-9d082578-e456-4fe2-9a02-621ebcc3ad8a.png)
![validNumbers](https://user-images.githubusercontent.com/108287233/213653958-a0a7d557-30e7-41a9-a4a7-93f9d4874b60.png)

### Initial clues - Number enterd is too high or too low
![oddOrEven](https://user-images.githubusercontent.com/108287233/213652964-6572436b-1ae6-42f7-ab24-be38d4a33764.png)

### First hint - Is the number odd or even?
![oddOrEven](https://user-images.githubusercontent.com/108287233/213652988-df119ce9-9546-4bfa-97cf-fe5a856b8571.png)

### Second hint - The answer is a number!
![secondHint](https://user-images.githubusercontent.com/108287233/213653116-75d7a4eb-d5b8-44df-961c-d80be237805a.png)

### Guess counter - The game will keep track of your guesses

![countGuess](https://user-images.githubusercontent.com/108287233/213653447-d493beb5-5c7d-4523-bd4b-804e03d9109a.png)


## End game with 'n' prompt
![no](https://user-images.githubusercontent.com/108287233/213519501-cdf0b3cc-2ca2-47d9-af49-2f200d85f3be.png)


## Built with
______________________________

- **[Python](https://www.python.org/)**
- **[Flask](https://flask.palletsprojects.com/en/2.2.x/)**
_________________

# Bugs and Testing
_____________________________

### Problem 001
__________

 * Implement functionality to provide additional hints to the user upon unsuccessful attempts to correctly answer the question, following the initial hint, with a maximum of three additional hint opportunities.
![walkThroughHintAgainAfter3Tries](https://user-images.githubusercontent.com/108287233/213493027-cb18268c-f5d6-4b90-900f-85757d9f8cf4.png)

![hintAgainAfterInitial3Guesses](https://user-images.githubusercontent.com/108287233/213493384-91ef7558-5ad8-47a0-a740-2846ebfa4996.png)


### Solution 001
_____________________________
*  This code segment is responsible for determining if and when to provide hints to the player during the course of the guessing game. It evaluates the player's progress by checking if they have used up three guesses and have not yet utilized the first hint option. If this criteria is met, the player is prompted to request a hint by entering "y" for yes or "n" for no. If the player chooses to receive a hint, the variable tracking the use of hints is set to true, and the code proceeds to determine if the answer is even or odd, providing a corresponding hint accordingly. The same process is repeated when the player reaches six guesses without utilizing the second hint option. The code then prompts the player for a hint and provides a hint that the answer is a number.

![hintAgainCode](https://user-images.githubusercontent.com/108287233/213494452-e9836770-4ba5-4468-abc1-9bc75dcbfa15.png)

### Problem 002
_________________________

* After a user has failed 3 times to achieve a correct answer the game will prompt the user if they would like a hint.  After a futher 3 more tires the game will again ask the user if they would like a hint.  The game therafter runs into infinity as the `if` statement applied to break the loop did not fire. 


![hintUsed2](https://user-images.githubusercontent.com/108287233/213497217-136b833d-ba89-4da0-8ee2-fba40658dddf.png)


### Solution 002
__________________

* By using formatted strings to help the values stand out in the terminal, in this manner one can determine where the issue might lie. 
The solution was to place an `exit()` statement atthe very end of the cone inplace of a `break` statement.  An additional `if` statement was used to break out of the `while loop` after 9 failed attempts at guessing the correct answer. 

![breakLoop](https://user-images.githubusercontent.com/108287233/213656209-80432d39-717c-4f1f-b327-353e1de48cc4.png)


### ***[PEP8](https://www.pythonchecker.com/)*** Python Validator Testing
_______________________________
![pep8](https://user-images.githubusercontent.com/108287233/213509983-db4ad1fb-e0db-4410-884f-3ba4e8b9ad28.png)

* The code initially made out with a 87% Exellent rating.
1. The suggestions to imporve the code revolved around adding whitespace.
2. Warning that a line of Python code should not be longer than 79 chatacters.
3. Add whitespace between operators.

## Bugs
_______________________________________________
* When a hint prompt is presented to the user, it is possible to input any value other than 'y' and the game will interpret this as a decline of the hint option and proceed without providing a hint to the player.

![bug](https://user-images.githubusercontent.com/108287233/213657975-2318141f-773e-43cb-b5a7-586416a37c8a.png)

## Deployment
___________________________________

The app is deployed with **[Heroku](https://dashboard.heroku.com/apps/guessinggamepy/deploy/github)**

1. Open an account with Heroku
2. On the homepage navigate to the "New" tab and select "Create new app"
3. Add a name in the "App name" field and choose the appropriate region
4. Select "Create app" this will bring you to the "Deploy" page 
5. Navigate to the "Deployment method" and select "GitHub"
6. In the "repo-name" field enter the name of the repo you would like to deploy
7. If the repo reflects in the dropdown menu, "connect" the repo
8. Scroll down and slect the 'main' branch
9. Select "Deploy Branch"
10. Wait a few moments while the repo is being deployed
11. Select "Deploy to Heroku"
________________________________________

## Credit
_____
**[guessinggamepy](https://guessinggamepy.herokuapp.com/)** - initial work

Spencer Barriball - Mentor

Code Institute - Tutor Scott

**[Jamal](https://codereview.stackexchange.com/questions/69333/number-guessing-game-with-maximum-and-minimum-values)** - **[StackExchange](https://stackexchange.com/)**

















