
#Reptile_Labyrinth

Reptile Labyrith is a python termial game where users tries to escape the labyrith in as few steps as possible.
Everytime the reptile hits a hidden trap it needs to start over. 

# How to play

First the player needs to choose a name for the reptile and the labyrinth is radomly generated. The reptile is displayed in the labyrith with the first letter its name. The retile will always start in the top left corner of the labyrith. 
Home, displayed with the letter H, is displayed in one of the space in bottom right corner of the labyrinth. The user moves the reptile using the letters E, W, N and S.
The user needs to get to Home with as few steps as possible. Hidden in the labyrinth are a number of traps. Every time the reptile hits a trap the reptile moves back to the start position while the number to steps keeps adding up.

# Existing Features

Random board generation.
    The traps are randomly placed in the labyrinth.
    The user can not see where the traps are.
    Home is randomly place within the four bottom right spaces on the board.
    Traps can not be placed in the start position nor in the home position.

Accepts user input
Input validation. The class method only reacts on N, S, E, W

# Future Features
Leader board



# Bugs resolved 
- N/S/E/W directions did not move the reptile in correct direction. This has been resolved.
- Number of steps were counted even if other then N, S, E or W was inputted. This has been resolved.
- If traps were located in the same positions as 'start' or 'home' position, less traps were active
  in the game. This has been resolved.


# Manual test Plan
- Verified that the reptile moves in the correct directions by entering N/S/E/W.
- Verified that #steps is correct by counting N/S/E/W.
- Verfied that input data other then N/S/E/W (both lower and upper case) is not counted
  in the number of steps.
- Verified that the name of the reptile is capilized.
- Verified that first letter of the name of the reptile is printed in the labyrinth.
- Verified that the game starts over if the reptile moves outside the labyrinth.
- Verified that correct text is displayed when executing the game and at the end of the game.
- Verified that a trap is hit.
- Verified that three traps exist in the game by adding print statements afer creating of the traps.
- Verified that the game ends of Home is reached.


# Validator testing
PEP8 no errors returned





![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!