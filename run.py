# import random
import random


class State:
    """Creates an instance of game variables"""

    def __init__(self, ships, rows, cols):
        self.user_score = 0
        self.ships = ships
        self.user_ships = self.ships
        self.com_ships = self.ships
        self.rows = rows
        self.columns = cols


def setup():
    """Information about the game and input for user_name.
    In the setup stage the user chooses username and sets up the playing grid.
    The player chooses the number of rows, columns and ships for the game."""

    print("Welcome to the best ever Battleship game!!! \n")
    print("Choose your grid!\n")
    print("Destroy the computer ships before the computer destroys yours! \n")
    print("------------------------------------------------------ \n")

    user = input("Enter your user name:\n")
    print("Good luck " + user)

    print("Let`s set up the grid!\n")
    while True:
        try:
            rows = int(input("How many rows:\n"))
            cols = int(input("How many columns:\n"))
            ships = int(input("How many ships:\n"))
            break
        except ValueError:
            print("That's not a valid option! Please choose a number")

    state = State(ships, rows, cols)
    return state


def create_grid(state):
    """Creates the playing area for computer and user"""
    grid = []
    for r in range(state.rows):
        row = []
        for c in range(state.columns):
            row.append(False)
        grid.append(row)
    return grid


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


def get_move():
    """Get user input for move"""
    move = input("Input your target (row 2 and column 3 = '2 3')\n")
    if move == "":
        print("Invalid move, try again\n")
        return get_move()
    return move


def shoot(grid, move, is_user, state):
    """Finds the move on the board and returns the value,
     the game continues until the ships number is zero."""
    try:
        splitted = move.split()
        row = int(splitted[0]) - 1
        col = int(splitted[1]) - 1
        max_row = state.rows - 1
        max_col = state.columns - 1
        if row < 0 or row > max_row and col < 0 or col > max_col:
            print("Invalid move, number of row or column outside of grid")
            move = get_move()
            return shoot(grid, move, is_user, state)
        if grid[row][col] is True:
            grid[row][col] = False
            print("HIT!!!")
            if is_user:
                state.user_score += 1
                state.com_ships -= 1
            else:
                state.user_ships -= 1
        else:
            print("Missed shot`\n---------")

        print(f"Rows:{state.rows}\nColumns:{state.columns}")

        print(f"Remaining user ships: {state.user_ships}")
        print(f"Remaining computer ships: {state.com_ships}")
        return state

    except ValueError:
        print("Please input number")
        move = get_move()
        return shoot(grid, move, is_user, state)
 
    except IndexError:
        print("Please input two numbers with space e.g `5 6`")
        move = get_move()
        return shoot(grid, move, is_user, state)


def start_game(user_grid, computer_grid, state):
    """Starts the game, gets input from user for move and adds a next move"""
    users_turn = True
    while state.user_ships != 0 and state.com_ships != 0:
        if users_turn:
            move = get_move()
            state = shoot(computer_grid, move, True, state)
            users_turn = False
        else:
            print("computers turn...")
            row = random.randint(1, state.rows)
            col = random.randint(1, state.columns)
            move = str(row) + " " + str(col)
            state = shoot(user_grid, move, False, state)
            users_turn = True

    end_game(state)


def end_game(state):
    """Ends game when the users ships get to zero"""
    if state.user_ships == 0:
        print("The computer won this round...\n")
        print(f"Your score was {state.user_score}")
        print("Better luck next time\n")
    else:
        print("Congratulations!! You won!!!")
        print("-----------------------------")


def main():
    """Main"""
    state = setup()
    usergrid = create_grid(state)
    compgrid = create_grid(state)

    usergrid = auto_add_ships(usergrid, state)
    compgrid = auto_add_ships(compgrid, state)

    start_game(usergrid, compgrid, state)


main()
