# Battleship-8040
 Battleship- 8040 is a Python game terminal, which runs on Heroku,
Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each
battleship occupies one square on the board.

Here is the live project, [Battleship8040](https://battleship8040-71d219516351.herokuapp.com/)

<img width="1265" alt="Screenshot 2024-01-01 at 17 52 27" src="https://github.com/giacoren6/battleship8040/assets/142323106/dea73ff8-fe25-412f-8024-87ae302c99cb">

## How to play the game

- Battleship-8040 is based on the classic game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).
 In this version, the player choose the ship choosing a number between 1 and 9 max the user have max 9 turns against the computer,
 after the ship is choose the user need to enter a ship column choosing a letter between A and I,
Hit the ship with X miss the ship with -,

The player and the computer then take it in turns to make guesses and try to sink each other's battleships.
The winner is the player who sinks all of their opponent's battleships first.

## Features 
## Existing Features
-  Generation Random board 
- The player can't see where the computer's ships are
- Ships are randomly placed on both of the lines of the player and computer boards

 <img width="1265" alt="Screenshot 2024-01-01 at 18 14 33" src="https://github.com/giacoren6/battleship8040/assets/142323106/4515bb68-25bc-4ec8-89f4-7ceb53bf9259">

 - Play against the computer
 - check your score
 - choose the user input

<img width="250" alt="Screenshot 2024-01-01 at 18 18 52" src="https://github.com/giacoren6/battleship8040/assets/142323106/1f5ea93c-d24f-426b-826e-f2e2bf982a1b">

Future Features 
- Allow player to select the board size and number of ships manually
- Allow player to position ships by themselves manually 
- Have more ships avalible to let expand the game

## Data Model
- I decided to use a Board class as my model. The game creates one Board class to hold the player's and
- the computer's board.
- The print_board class stores the board size, the letter between A and I ,and the row number,
- The class ship_create in ship range of 6,
- class ship_location i've put a row number between 1 to 9,
- class count_hit and the class ship_create where i've decided to put 10 turns for the game.

# Testing
- I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are some errors but no warning
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
- Tested in my local terminal and the Code Institute Heroku terminal

# Bugs
No bugs find it 
## Remaining Bugs
- No bugs remaining
## Validator Testing
PEP8
o some error were returned from [PEP8online.com](https://pep8ci.herokuapp.com/#)


## Deployment
- This project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
-  Fork or clone this repository
-  Create a new Heroku app
-  Set the buildbacks to Python and Nodes in that order
-  ink the Heroku app to the repository
 o Click on Deploy
## Credits
- Code Institute for the deployment terminal
- Wikipedia for the details of the Battleships game








