# import random
import random


class State:
    """Creates an instance of game variables"""

    def __init__(self, user_score, user_ships, com_ships, ships):
        self.user_score = user_score
        self.user_ships = user_ships
        self.computer_ships = computer_ships
        #self.rows = rows
        #self.columns = columns
        self.ships = ships


def auto_add_ships(grid, state):
    """Add ships to the playing area with random number"""
    added_ships = 0
    while added_ships < state.ships:
        row = random.randint(0, state.rows - 1)
        col = random.randint(0, state.columns - 1)
        if grid[row][col] is False:
            grid[row][col] = True
            added_ships += 1
    return grid


def create_grid(state):
    """Creates the playing area for computer and user"""
    grid = []
    for r in range(state.rows):
        row = []
        for c in range(state.columns):
            row.append(False)
        grid.append(row)
    return grid


def get_move():
    """Get user input for move"""
    move = input("Whats your next target? (row 2 and column 3 = '2 3')\n")
    return move


def shoot(grid, move, is_user, state):
    """Finds the move on the board and returns the value"""
    try:
        splitted = move.split()
        row = int(splitted[0]) - 1
        col = int(splitted[1]) - 1
        if row < 0 or row > 4 and col < 0 or col > 4:
            print("Invalid move \n")
            move = get_move()
            return shoot(grid, move, is_user, state)
        if grid[row][col] is True:
            grid[row][col] = False
            print("HIT!!!\n -------")
            if is_user:
                state.user_score += 1
                state.computer_ships -= 1
            else:
                state.user_ships -= 1
        else:
            print("Missed shot\n")

        print(f"Remaining user ships: ,{state.user_ships}")
        print(f"Remaining computer ships: , {state.computer_ships}")
        return state

    except AttributeError:
        print("Invalid move")
        move = get_move()
        return shoot(grid, move, is_user, state)


def end_game(state):
    """Ends game when the users ships get to zero"""
    if state.user_ships == 0:
        print("The computer won this round...\n")
        print("Your score was " + state.user_score)
        print("Better luck next time\n")
    else:
        print("Congratulations!! You won!!!")
        print("-----------------------------")


def start_game(user_grid, computer_grid, state):
    """Starts the game, gets input from user for move and adds a next move"""
    users_turn = True
    while state.user_ships != 0 and state.computer_ships != 0:
        if users_turn:
            move = get_move()
            state = shoot(computer_grid, move, True, state)
            users_turn = False
        else:
            print("computers turn...")
            row = random.randint(1, 5)
            col = random.randint(1, 5)
            move = str(row) + " " + str(col)
            state = shoot(user_grid, move, False, state)
            users_turn = True

    end_game(state)


def setup():
    """Information about the game and input for user_name"""

    print("Welcome to the best ever Battleship game!!! \n")
    print("The grid is 5x5 and has 5 ships \n")
    print("Destroy your opponents ships before they destroy yours! \n")
    print("------------------------------------------------------ \n")

    user = input("Enter your user name: ")
    print("Good luck " + user)

    state = State(1, 1, 1, 1,5)
    return state


def main():
    """Main"""
    state = setup()
    usergrid = create_grid(state)
    compgrid = create_grid(state)

    usergrid = auto_add_ships(usergrid, state)
    compgrid = auto_add_ships(compgrid, state)

    start_game(usergrid, compgrid, state)


main()

