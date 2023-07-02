# import random 
import random

def create_grid():
    '''Creates the playing area for both the players,computer and user'''
    grid = []
    for row in range(rows):
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
    ''' Get user input for move'''
    move = input("Whats your next target? (for row 2 and column 3 write '2 3')\n")
    return move 
get_move()

def start_game(user_grid, computer_grid):
    users_turn = True
    while user_ships != 0 and computer_ships != 0:
        if users_turn:
            move = get_move()
            users_turn = False
        else:
            print("computers turn...")
            row = random.randint(1,5)
            col = random.randint(1,5)
            move = str(row) + " " + str(col)
            users_turn = True

def shoot(grid, move, is_user ):
    '''Finds the move on the board and returns the value, if user guesses the right row and collumn the value is returned as a "HIT" otherwise it is returned as "Missed shot'''
    try:
        splitted = move.split()
        row = int(splitted[0]) - 1
        col = int(splitted[1]) - 1
        if(row < 0 or row > 4 and col < 0 or col > 4):
            print("Invalid move \n")
            move = get_move()
            return shoot(grid, move)
        if(grid[row][col] is True):
            grid[row][col] = False
            print("HIT!!!\n")
            if (is_user):
                user_score+=1
                computer_ships-=1
            else:
                user_ships-=1
        else:
            print("Missed shot\n")
     
        print(f"Remaining user ships: ", {user_ships})
        print(f"Remaining computer ships: ", {computer_ships})

    except AttributeError:
        print("Invalid move")
        move = get_move()
        return shoot(grid, move)
usergrid = create_grid()
compgrid = create_grid()

usergrid = auto_add_ships(usergrid)
compgrid = auto_add_ships(compgrid)

start_game(usergrid, compgrid)



def score():
    ''' Tracks the score of the players'''
    pass
def end_game():
    ''' The game ends when either the player or the computer have zero battleships '''
    pass


