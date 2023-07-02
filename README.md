# *Battleship*

Battleships is Python Terminal game that is deployed on Heroku. 

Players compete against the computer to try to find the ships before the computer does. 
![alttext]()


## **Features** ##

### *Existing features* ###
* Player is informed that there are 5 ships randomly placed for the player to find.
* After input of the players user name, the player chooses two numbers for row and collumn. 
![alttext]()

* If its a right guess the player gets "HIT!" message and the turn goes over to the computer.
![alttext]()

* The player takes turns with the computer until the player or the computer ships are destroyed.
* The remaining ships are displayed on the screen.
![alttext]()

#### Error-checkling ####
* The player must enter numbers for the row and collumn .

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


* The live link can be found here:<a href=>Battleship</a>