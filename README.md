# *Battleship*

Battleships is Python Terminal game that is deployed on Heroku. 

Players compete against the computer to try to find the ships before the computer does.

![alt text](/images/Battleship%20Game.png)


## **Features** ##

### *Existing features* ###
* Player is requested to input name and also how many columns and rows will the player want to play with.
* After input of the players user name, the player chooses two numbers for row and column. 
* If its a right guess the player gets "HIT!" message and the turn goes over to the computer.
* The player takes turns with the computer until the player or the computer ships are destroyed.
* The remaining ships are displayed on the screen.

#### Error-checking ####
* The program crashed because the try except block was not implemented. The code was updated and now it works as it should. 

## **Testing** ##
The code was continuasly tested in Visual Studio Code.

## **Bugs** ##

No bugs found.

## **Code Validation** ##

#### PEP8

* No errors were found when the code was tested in PEP8 Python Validator.

## **Deployment** ##
* This project was deployed in Heroku using the followings steps:
    - Go to the Heroku website, login and from the Heroku dashboard click on "Create New App"
    - In the app settings, set the config_var and add the bulidpcks to python and node.js. 
    - When the settings are complete go to the deploy and link the GitHub repository to the app
    - Click on deploy


* The live link can be found here:<a href="https://battleship11-1b9d344f69d7.herokuapp.com/">Battleship</a>