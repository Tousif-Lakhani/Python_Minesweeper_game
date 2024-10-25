import random


def create_board(size):

    '''
    it will create the solution board
    ------
    size: int
        size of the board
    ------
    Returns
        Lists of list
    '''
    sboard = [['#' for aa in range(size)] for bb in range(size)]
    return sboard


def create_uboard(size):

    '''
    it will create the User board
    ------
    size: int
        size of the board
    ------
    Returns
        Lists of list
    '''

    uboard = [['#' for aa in range(size)] for bb in range(size)]
    return uboard


def place_mines(sboard, num_mines):
    '''
    Randomly place mine on the board
    ------
    sboard: int
        helps to get the length of the board
    ------
    num_mines: int
        required number of mines
    ------
    Returns
        lists of lists of "#" with random placement of mines marked X
    '''
    size = len(sboard)
    mines = set()
    while len(mines) < num_mines:
        row = random.randint(0, size-1)
        col = random.randint(0, size-1)
        mines.add((row, col))

    for row, col in mines:
        sboard[row][col] = 'X'

    return mines


def total_mines_around(sboard, row, col):
    '''
    Checks mines around the selected square
    ------
    sboard: int
        helps to get the length of the board
    ------
    row: int
        selected row number by the user
    ------
    col: int
        selected col number by the user
    ------
    r_max,c_max:
        picks the maximum value for the starting point.
        its done to avoid exceeding the board limit.
    ------
    r_min,c_min:
        picks the minimum value for the ending point.
        its done to avoid exceeding the board limit.
    ------
    Returns
        number of mines around the selected square
    '''
    rows = len(sboard)
    cols = len(sboard[0])

    r_max = max(0, row-1)
    r_min = min(row+2, rows)

    c_max = max(0, col-1)
    c_min = min(col+2, cols)

    count = 0

    for i in range(r_max, r_min):
        for j in range(c_max, c_min):
            if sboard[i][j] == 'X':
                count += 1

    return count


def reveal_square(sboard, uboard, row, col):
    '''
    This function will call itself until the count is > 0
    ------
    sboard: int
        helps to get the length of the board
    ------
    row: int
        selected row number by the user
    ------
    col: int
        selected col number by the user
    ------
    r_max,c_max:
        picks the maximum value for the starting point.
        its done to avoid exceeding the board limit.
    ------
    r_min,c_min:
        picks the minimum value for the ending point.
        its done to avoid exceeding the board limit.
    ------
    '''
    if uboard[row][col] != '#':
        return

    rows = len(sboard)
    cols = len(sboard[0])

    r_max = max(0, row-1)
    r_min = min(row+2, rows)

    c_max = max(0, col-1)
    c_min = min(col+2, cols)

    count = total_mines_around(sboard, row, col)

    if count > 0:
        uboard[row][col] = str(count)

    if count == 0:
        uboard[row][col] = "0"

        for i in range(r_max, r_min):
            for j in range(c_max, c_min):
                if i != row or j != col:
                    reveal_square(sboard, uboard, i, j)


def flag_square(uboard, row, col):
    '''
    It flags or unflags the selcted square
     ------
    row: int
        selected row number by the user
    ------
    col: int
        selected col number by the user
    ------
    '''
    if uboard[row][col] == "#":
        uboard[row][col] = "F"
    elif uboard[row][col] == "F":
        uboard[row][col] = "#"


def print_board(uboard):
    '''
    It prints the user board with the borders
    ------
    uboard:
        used to identify the length of the board
    ------
    Chr 8254:
        it is used to draw upperscore sign
    '''
    rows = len(uboard)
    cols = len(uboard)

    print("    ", end="")

    for col in range(1, cols+1):
        if col <= 9:
            print(col,  end="  ")
        if col >= 10:
            print(col,  end=" ")

    print()
    print("   ", end="")
    print("_"*(col*3))
    for row in range(rows):
        print("  ", end="")
        print(chr(65+row), end="|")

        for col in range(cols):
            print(f'{uboard[row][col]} ', end="|")
        print()
        print("   ", end="")
        print((chr(8254)*(col*3))+(4*chr(8254)))


def start_game():
    '''
    Calls all the functions.
    '''
    the_end = False
    while not the_end:
        print("")
        print("Welcome to the Minesweeper game!")
        print("")

        try:
            size = int(input('How big the board should be? '))
        except ValueError:
            print("")
            print("!!!_Please enter a numerical value._!!!")
            print("")
            continue

        while True:
            try:
                num_mines = int(input('How many mines are to be placed? '))
                if num_mines <= ((size*size)-1):
                    break
                else:
                    print("Enter mines that are less than", (size*size)-1,)
            except ValueError:
                print("")
                print("!!!_Please enter a numerical value._!!!")
            print("")

        print("")

        sboard = create_board(size)
        uboard = create_uboard(size)

        place_mines(sboard, num_mines)

        the_end = False
        while not the_end:

            print_board(uboard)
            print("")

            try:
                position = input('Enter square name(eg:A1)or type F to flag: ')

                if position == "F":
                    fp = input("Please enter row and column (eg:A1) to flag: ")
                    row = ord(fp[0]) - 65
                    col = int(fp[1:]) - 1

                    if (row < 0 or row >= size) or (col < 0 or col >= size):
                        print('Incorrect move! Try again.')
                        continue

                    flag_square(uboard, row, col)
                    continue

                row = ord(position[0]) - 65
                col = int(position[1:]) - 1
            except ValueError:
                print("!!!Please enter correct row and column name!!!")
                continue

            if (row < 0 or row >= len(sboard)):
                print("Wrong Move! Please Try Again!!")
                continue

            if (col < 0 or col >= len(sboard)):
                print("Wrong Move! Please Try Again!!!")
                continue

            if sboard[row][col] == "X":
                print("Boom!! You hit a mine. Game Over!!!")
                print("")
                print("Solution Board")
                print_board(sboard)
                break

            elif uboard[row][col] != "#":
                print("")
                print("!!!Please select unidentified square!!!")
                print("")
                continue

            else:
                reveal_square(sboard, uboard, row, col)

                if sum(item.count('#') for item in uboard) == num_mines:
                    print('Congratulations! You won the game.')
                    break
                elif sum(item.count('F') for item in uboard) == num_mines:
                    print('Congratulations! You won the game.')
                    break

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print(" ")
            print("Thank you for playing Minesweeper. Have a nice day :) !!!")
            break


start_game()











#SOURCES

'''
Nested Lists/List comprehension/Range - https://www.freecodecamp.org/news/list-within-a-list-in-python-initialize-a-nested-list/#:~:text=A%20list%20within%20another%20list,list%2C%20this%20can%20be%20helpful.

List comprehension - https://flaviocopes.com/books-dist/python-handbook.pdf - pg 88

Understanding functions - https://pythontutor.com/python-compiler.html#mode=edit

mines logic - https://www.youtube.com/watch?v=bGr-j89FaRM

Bord Design logic - https://www.youtube.com/watch?v=bGr-j89FaRM

chr and ord logic - https://www.javatpoint.com/python-chr-function - example 3

r_max,r_min logic - https://bedford-computing.co.uk/learning/wp-content/uploads/2015/10/No.Starch.Python.Oct_.2015.ISBN_.1593276036.pdf - pg 377

winning game logic (sum(item.count)) - https://bedford-computing.co.uk/learning/wp-content/uploads/2015/10/No.Starch.Python.Oct_.2015.ISBN_.1593276036.pdf - pg 241

Other functionality practiced from  - https://www.w3schools.com/python/python_functions.asp

'''
