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
     
    *   ### Wireframes

    -   Home Page Wireframe - [View](https://github.com/)

    -   Mobile Wireframe - [View](https://github.com/)

    -   Contact Us Page Wireframe - [View](https://github.com/)

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
- Press enter to start the game 
- Enter your Name
- Generation Random board 
- The player can't see where the computer's ships are
- Ships are randomly placed on both of the lines of the player and computer boards

<img width="740" alt="Screenshot 2024-04-09 at 20 47 05" src="https://github.com/giacoren6/battleship8040/assets/142323106/706ef957-ab62-4f85-b247-5ae75ad8d76a">

 - Play against the computer
 - check your score
 - choose the user input

<img width="732" alt="Screenshot 2024-04-09 at 23 41 26" src="https://github.com/giacoren6/battleship8040/assets/142323106/07534470-ffd3-4ec8-b16e-0e79453bab14">

  - Once the game finish the player can see where was the ship hidden

<img width="728" alt="Screenshot 2024-04-09 at 23 49 31" src="https://github.com/giacoren6/battleship8040/assets/142323106/b1189579-2fbc-4533-960e-018ea110be0c">

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

# Bugs
No bugs find it 

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
## Credits
- Code Institute for the deployment terminal
- Wikipedia for the details of the Battleships game








