# Set up

## Game overview
column = ["1", "2", "3"]
line1 = ["", "", ""]
line2 = ["", "", ""]
line3 = ["", "", ""]
list_of_lines = [line1, line2, line3]

print("Welcome to tic tac toe. Player 1 controls the symbol 'O' and Player 2 controls the symbol 'X'.\n"
      "Please name the row and column where you want to place your 'O' or 'X'. Please \n"
      "indicate the row first and the column. In the following format 1,3). 1,3 means that you want to \n"
      "place your 'O' or 'X' in the first row and the third column")
print("The format is row,column (first row then column) separated by a comma.")

print("This is the current status of the game.")
print("col:", column)
print("row 1", line1)
print("row 2", line2)
print("row 3", line3)

blocked_spots_line1 = []
blocked_spots_line2 = []
blocked_spots_line3 = []

game_is_on = True

curr = 1

def show_game_status():
    global curr
    print("This is the current status of the game.")
    print("col:", column)
    print("row 1", line1)
    print("row 2", line2)
    print("row 3", line3)
    if curr == 1:
        curr = 2
    elif curr == 2:
        curr = 1

def get_user_input():
    user_command = str(input(f"Player{curr}! Please name the row and column where you want to place your '0' or 'X'. E.g.: 1,3: "))
    chosen_row = user_command.split(",")[0]
    chosen_col = user_command.split(",")[1]
    #adjust here so that only valid formats can be posted
    try:
        chosen_row = int(chosen_row)
        chosen_col = int(chosen_col)
    except ValueError:
        print('Please reconsider the format of the position you typed')
        get_user_input()
    finally:
        if (chosen_col > 3 or chosen_col < 1) or (chosen_row > 3 or chosen_row < 1):
            print('The position you have chosen is either not available. Please try again:')
            get_user_input()
        update_game(chosen_row, chosen_col)
        find_a_winner()
        show_game_status()

def update_game(row, column):
    get_possible_indices()
    if curr == 1:
        item = "O"
    elif curr == 2:
        item = "X"
    if row == 1:
        if column not in blocked_spots_line1:
            line1[column-1] = item
        else:
            print("This position is already taken. Please try another spot.")
            get_user_input()
    elif row == 2:
        if column not in blocked_spots_line2:
            line2[column-1] = item
        else:
            print("This position is already taken. Please try another spot.")
            get_user_input()
    elif row == 3:
        if column not in blocked_spots_line3:
            line3[column-1] = item
        else:
            print("This position is already taken. Please try another spot.")
            get_user_input()

def get_possible_indices():
    counter = 0
    for line in list_of_lines:
        counter += 1
        for i, j in enumerate(line):
            if j == "O" or j == "X":
                not_possible = i+1
                if counter == 1 :
                    blocked_spots_line1.append(not_possible)
                if counter == 2:
                    blocked_spots_line2.append(not_possible)
                elif counter == 3:
                    blocked_spots_line3.append(not_possible)


def find_a_winner():
    global game_is_on
    list_of_indexes_x = []
    list_of_indexes_o = []

    for line in list_of_lines:
        indices_o = [i for i, x in enumerate(line) if x == "O"]
        indices_x = [i for i, x in enumerate(line) if x == "X"]
        list_of_indexes_x.append(indices_x)
        list_of_indexes_o.append(indices_o)

        # horizontal
    for list in list_of_indexes_x:
        if len(list) == 3:
            print("The Winner is player 2")
            game_is_on = False
            return game_is_on

    for list in list_of_indexes_o:
        if len(list) == 3:
            print("The Winner is player 1")
            print(list)
            game_is_on = False
            return game_is_on

    #vertical
    vertical = [[row[i] for row in list_of_lines] for i in range(3)]

    for lst in vertical:
        if lst == ['O', 'O', 'O']:
            print("The Winner is player 1")
            game_is_on = False
            return game_is_on
        if lst == ['X', 'X', 'X']:
            print("The Winner is player 2")
            game_is_on = False
            return game_is_on

    #diagional
    diagonal_o = []
    diagonal_x = []
    for lst in list_of_lines:
        for index, letter in enumerate(lst):
            if letter == 'O':
                diagonal_o.append(index)
            elif letter == 'X':
                diagonal_x.append(index)

    if len(diagonal_x) == 3 and diagonal_x[1] == 1:
        if diagonal_x[0] == 0 or 2:
            if diagonal_x[2] == (0 or 2):
                print("The Winner is player 2")
                game_is_on = False
                return game_is_on
    if len(diagonal_o) == 3 and diagonal_o[1] == 1:
        if diagonal_o[0] == 0 or 2:
            if diagonal_o[2] == 0 or 2:
                print("The Winner is player 1")
                game_is_on = False
                return game_is_on

while game_is_on:

    get_user_input()
























