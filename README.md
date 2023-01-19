# Command Line Interface Python Guessing Game
_________________________________________

![pexels-black-ice-1314543](https://user-images.githubusercontent.com/108287233/213469981-2d843716-1d00-455c-a195-46be5c0bf4fa.jpg)
![responsePP3](https://user-images.githubusercontent.com/108287233/213483220-a3ff5669-80d9-4bfe-a626-bec4e7f04295.png)


### This is a guessing game written in Python.

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
11. Te game will restart if you slected 'y' or end with a goodbye message if you slected 'n'.

## Built with
______________________________

- **[Python](https://www.python.org/)**
- **[Flask](https://flask.palletsprojects.com/en/2.2.x/)**

## Deployment
___________________________________

The app is deployed with **[Heroku](https://dashboard.heroku.com/apps/guessinggamepy/deploy/github)**



## Credit
**[guessinggamepy](https://guessinggamepy.herokuapp.com/)** - initial work

Spencer Barriball

Code Institute - Tutor Scott


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






















