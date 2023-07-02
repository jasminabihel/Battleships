# import random 
import random

class State:
    '''Creates an instance of game variables'''
    def __init__(self, user_score, user_ships, computer_ships, rows, columns, ships):
        self.user_score = user_score
        self.user_ships = user_ships
        self.computer_ships = computer_ships
        self.rows = rows
        self.columns = columns
        self.ships = ships

def create_grid():
    '''Creates the playing area for computer and user'''
    grid = []
    for r in range(state.rows):
        row = []
        for c in range(state.columns):
            row.append(False)
        grid.append(row)
    return grid

def auto_add_ships():
    '''Add ships to the playing area with random number '''
    def auto_add_ships(grid, state):
    added_ships = 0
    while added_ships < state.ships:
        row = random.randint(0, state.rows - 1)
        col = random.randint(0, state.columns - 1)
        if (grid[row][col] is False):
            grid[row][col] = True
            added_ships+=1
    return grid

def get_move():
    ''' Get user input for move'''
    move = input("Whats your next target? (for row 2 and column 3 write '2 3')\n")
    return move 
get_move()

def start_game(user_grid, computer_grid, state):
    '''Starts the game, gets input from computer and user for move and adds a next move'''
    users_turn = True
    while state.user_ships != 0 and state.computer_ships != 0:
        if users_turn:
            move = get_move()
            state = shoot(computer_grid, move, True, state)
            users_turn = False
        else:
            print("computers turn...")
            row = random.randint(1,5)
            col = random.randint(1,5)
            move = str(row) + " " + str(col)
            state = shoot(user_grid, move, False, state)
            users_turn = True

end_game(state)

def shoot(grid, move, is_user ):
    '''Finds the move on the board and returns the value, if user guesses the right row and collumn the value is returned as a "HIT" otherwise it is returned as "Missed shot'''
    try:
        splitted = move.split()
        row = int(splitted[0]) - 1
        col = int(splitted[1]) - 1
        if(row < 0 or row > 4 and col < 0 or col > 4):
            print("Invalid move")
            move = get_move()
            return bomb(grid, move, is_user, state)
        if(grid[row][col] is True):
            grid[row][col] = False
            print("HIT!!!")
            if (is_user):
                state.user_score+=1
                state.computer_ships-=1
            else:
                state.user_ships-=1
        else:
            print("Missed shot")
     
        print(f"Remaining user ships: ", {state.user_ships})
        print(f"Remaining computer ships: ", {state.computer_ships})
        return state

    except AttributeError:
        print("Invalid move")
        move = get_move()
        return shoot(grid, move, is_user, state)

def setup():
    ''''''
    print("Welcome to the best ever Battleship game!!! \n")
    print("The grid is 5x5 and there a total of 5 ships that take up one square each \n")
    print("The objective is to destroy your opponents ships before they destroy yours! \n")
    print("------------------------------------------------------ \n")

    user = input("Enter your user name: ")
    print("Good luck " + user)

    state = State(0, 1, 1, 3, 3, 1)
    return state


setup()

def end_game(state):
    ''' Ends game when the users ships get to zero'''
    if state.user_ships == 0:
        print("The computer won this round...")
        print("Your score was " + state.user_score)
        print("Better luck next time")
    else:
        print("Congratulations!! You won!!!")


def main():

    state = setup()
    usergrid = create_grid(state)
    compgrid = create_grid(state)

    usergrid = auto_add_ships(usergrid, state)
    compgrid = auto_add_ships(compgrid, state)

    start_game(usergrid, compgrid, state)
main()



