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
![enterMinMax](https://user-images.githubusercontent.com/108287233/213516858-66ad230b-d0cb-445f-8040-dea5ada98794.png)

### Reverse values if user enter incorrectly
![gamePlayMinMaxReverse](https://user-images.githubusercontent.com/108287233/213515754-51d793a8-6b1c-404f-8a01-fe1504fd9575.png)

### Initial clues
![clues](https://user-images.githubusercontent.com/108287233/213517087-3dbf61a0-211f-418a-845b-bb307f526637.png)


### First hint
![firstHint](https://user-images.githubusercontent.com/108287233/213516118-f7778efe-39b0-4603-b946-67419392577c.png)


### Second hint
![secondHint](https://user-images.githubusercontent.com/108287233/213516448-70660c1e-045d-472e-8725-559469a34d55.png)

## End game with 'n' prompt
![no](https://user-images.githubusercontent.com/108287233/213519501-cdf0b3cc-2ca2-47d9-af49-2f200d85f3be.png)


## Built with
______________________________

- **[Python](https://www.python.org/)**
- **[Flask](https://flask.palletsprojects.com/en/2.2.x/)**
_________________

# Testing and solving
_____________________________

### Problem 001
__________

 * Implement functionality to provide additional hints to the user upon unsuccessful attempts to correctly answer the question, following the initial hint, with a maximum of three additional hint opportunities.
![walkThroughHintAgainAfter3Tries](https://user-images.githubusercontent.com/108287233/213493027-cb18268c-f5d6-4b90-900f-85757d9f8cf4.png)

![hintAgainAfterInitial3Guesses](https://user-images.githubusercontent.com/108287233/213493384-91ef7558-5ad8-47a0-a740-2846ebfa4996.png)


### Solution 001
_____________________________
*  The code checks if the player has used up 3 guesses and have not used the first hint yet. If that's the case, it asks the player if they would like a hint by prompting them to enter "y" for yes and 'n' for no. If the player enters "y", the `hint_used` variable is set to True, and the code then checks if the answer is even or odd, and gives the player a hint accordingly. Similarly, it checks if the player has used up 6 guesses and haven't used the second hint yet, and if so, it again prompts the player if they would like a hint and if yes, gives a hint that the answer is a number.

![hintAgainCode](https://user-images.githubusercontent.com/108287233/213494452-e9836770-4ba5-4468-abc1-9bc75dcbfa15.png)

### Problem 002
_________________________

* After a user has failed 3 times to achieve a correct answer the game will prompt the user if they would like a hint.  After a futher 3 more tires the game will again ask the user if they would like a hint.  The game therafter runs into infinity as the `if` statement applied to break the loop did not fire. 


![hintUsed2](https://user-images.githubusercontent.com/108287233/213497217-136b833d-ba89-4da0-8ee2-fba40658dddf.png)


### Solution 002
__________________

* By using formatted strings to help the values stand out in the terminal, in this manner one can determine where the issue might lie. 
* In this case the `hint_used` statement was proving `False` when infact it needed to be proven `True`.  This will allow the all three conditions to be met and the `if` statement to `break` and the game will end.


### ***[PEP8](https://www.pythonchecker.com/)*** Python Validator Testing
_______________________________
![pep8](https://user-images.githubusercontent.com/108287233/213509983-db4ad1fb-e0db-4410-884f-3ba4e8b9ad28.png)

* The code initially made out with a 87% Exellent rating.
1. The suggestions to imporve the code revolved arounf adding whitespace.
2. Warning that a line of Python code should not be longer than 79 chatacters.
3. Add whitespace between operators.

## Bugs
_______________________________________________
* The game will continue to run after the second hint. 
Once the user has failed 3 attempts a hint will be provided, this will allow 3 more turns before a second hint is provided.  
Thereafter the game will run continually until the user gets a correct answer.  They will be presesnted with a congratulations message and asked if they would like to play again.

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

















