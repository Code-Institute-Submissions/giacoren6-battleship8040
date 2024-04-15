# Battleship-8040
Battleship-8040 is a Python game terminal, which runs on Heroku,The User can try to beat the computer by finding all of the computer's battleships, The user have 10 rounds to find the computer's battleships, The user have 6 rounds to defeat the computer,Each battleship occupies one square on the board.

Here is the live project, [Battleship8040](https://battleship8040-71d219516351.herokuapp.com/)

<img width="1453" alt="Screenshot 2024-04-09 at 14 20 43" src="https://github.com/giacoren6/battleship8040/assets/142323106/4db42904-1568-40ae-9df5-1d59ff0b66ef">

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the Game.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the Game.
        3. As a First Time Visitor, I want to look for testimonials to understand what Talk about this Game and check if is trusted.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to find Out more about The Game and find new challenges.
  


    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if there are New updated regarding the game .
     
    -   ### Design
    -   #### Colour Scheme
        -   Are used 2 main colors (black and white).
     
# Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

[Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  
## How to play the game

Battleship-8040 is based on the classic game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).
In this version, the user choose the ship choosing a number between 1 to 9  the user have 10 turns avalible to discover the computer's battleships,
after the ship is choose the user need to enter a ship column choosing a letter between A and I,Hit the ship with X miss the ship with -.

The player and the computer then take it in turns to make guesses and try to sink each other's battleships.
The winner is the player who sinks all of their opponent's battleships first.

## Features 

## Existing Features
- Type enter to start the game 
- Enter your Name
- Generation Random board 
- The player can't see where the computer's ships are
- Ships are randomly placed on both of the lines of the player and computer boards

<img width="733" alt="Screenshot 2024-04-15 at 15 12 53" src="https://github.com/giacoren6/battleship8040/assets/142323106/e84da858-f3c8-4e4d-95e2-872c52a29d9a">

 - Play against the computer
 - check your score
 - choose the user input

<img width="730" alt="Screenshot 2024-04-15 at 15 22 36" src="https://github.com/giacoren6/battleship8040/assets/142323106/a6124fc5-9a6d-45b0-b0ea-83e71d737742">

  - Once the game finish the player can see where was the ship hidden

<img width="729" alt="Screenshot 2024-04-15 at 15 30 13" src="https://github.com/giacoren6/battleship8040/assets/142323106/773d636e-b070-45f2-a138-ac062ebb8cc4">

  - Once the game finish the player can see the proper guess location board
 
<img width="732" alt="Screenshot 2024-04-09 at 23 57 05" src="https://github.com/giacoren6/battleship8040/assets/142323106/7fb26ad9-f916-415e-b087-2417c3397393">

 - input validation and error
 - the player need to put a number 1 to 9 if are not those will be an error(Invalid input).
 - the player need to put a column A to I if are not those will be an error(Invalid input).
 - The player cannot use the same number with the same letter.

<img width="731" alt="Screenshot 2024-04-12 at 14 45 24" src="https://github.com/giacoren6/battleship8040/assets/142323106/68b0ad1d-cabb-4f4b-abcc-b9fc9f0aa3e0">


## Future Features 
- Allow player to position ships by themselves manually.
- Have more ships avalible to let expand the game.
- Allow the player to let close the game manually and restart the game.


## Data Model
- I decided to use a Board Function as my model. The game creates one Board to hold the player's board.
- The print_board Funcion stores the board size, the letter between A and I ,and the row number between 1 and 9.
- The Function ship_create in ship range of 6,
- The Function ship_location, is in a row number between 1 to 9,
- The Function count_hit and the Function ship_create where i've decided to put 10 turns for the game.
- The player win if hit 6 times a battleship.

# Testing
- I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no errors.
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice
- Tested in my local terminal and the Code Institute Heroku terminal

- #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the Game and understand what Game is it.

        1. The Game is easy to understand for the User/Player.
        2. The main Goal is made for the Player's to let them interact with the game and find new challenges.
        3. The Player have to press enter button to start the game, and will come out the rules of the game.
        4. The Player can write his hown name.

    2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the Game.

        1. The Game has been designed to be fluid and never to entrap the Player/User.
  
    2. As a First Time Visitor, I want to look for testimonials to understand what their Users/Player's think of them and see if they are trusted.

        - #### Returning Visitor Goals

    1. As a Returning Visitor, I want To do always a better score and find new challeges.

        1. The Computer's board is hide to the Player.
        2. The Computer's board will come out when the game round finish.

- #### Frequent User Goals

    1. As a Frequent  User, I want to check to see if there are Update to some new different style of the game.

        1. The User/Player would already be comfortable with the Game layout and can easily click the letters and numbers and check the score.

# Bugs
- Solved Bugs.
- All Bugs are Solved.
- No Bugs Find it.

## Validator Testing
PEP8
No errors find in [PEP8online.com](https://pep8ci.herokuapp.com/#)

## Remaining Bugs
- No bugs remaining

## Deployment
- This project was deployed using Code Institute's mock terminal for Heroku.
- Steps for deployment:
-  Fork or clone this repository
-  Create a new Heroku app
-  Set the buildbacks to Python and Nodes in that order
-  ink the Heroku app to the repository
 o Click on Deploy
- [Live link here](https://battleship8040-71d219516351.herokuapp.com/)

## Credits
- Code Institute for the deployment terminal
- Wikipedia for the details of the Battleships game








