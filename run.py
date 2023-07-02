# import random 
import random

def create_grid():
    '''Creates the playing area for both the players,computer and user'''
    grid = []
    for r in range(rows):
        row = []
        for c in range(columns):
            row.append(False)
        grid.append(row)
    return grid

def auto_add_ships():
    '''Add ships to the playing area with random number '''
    added_ships = 0
    while added_ships < 5:
        row = random.randint(0, 5)
        col = random.randint(0, 5)
        if (grid[row][col] is False):
            grid[row][col] = True
            added_ships+=1
    return grid

def setup():
    '''Starts the game, gets input from computer and user for move and adds a next move'''
    print("Welcome to the best ever Battleship game!!! \n")
    print("The grid is 5x5 and there a total of 5 ships that take up one square each")
    print("The objective is to destroy your opponents ships before they destroy yours! \n")
    print("------------------------------------------------------ \n")

    user = input("Enter your user name: ")
    print("Good luck " + user)
setup()

def get_move():
    move = input("Whats your next target? (for row 2 and column 3 write '2 3')\n")
    return move 
get_move()



def score():
    ''' Tracks the score of the players'''
    pass
def end_game():
    ''' The game ends when either the player or the computer have zero battleships '''
    pass

