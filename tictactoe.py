def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    bordertype1 = "+-------+-------+-------+\n"
    bordertype2 = "|       |       |       |\n"
    row0 = f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n"
    row1 = f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n"
    row2 = f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n"
    buildrow0=(bordertype1+bordertype2+row0+bordertype2)
    buildrow1=(bordertype1+bordertype2+row1+bordertype2)
    buildrow2=(bordertype1+bordertype2+row2+bordertype2)
    print(buildrow0+buildrow1+buildrow2+bordertype1)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            user_move = int(input("Enter a number between 1-9: "))
            if user_move in make_list_of_free_fields(board):
                for x in range(0,3):
                    for y in range(0,3):
                        if user_move == board[x][y]:
                            board[x][y] = "O"
                break
            else:
                print("That didn't work, please choose a free field between 1-9")
                continue
        except:
            print("That isn't a number between 1-9, try again")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    free_fields = []
    for row in board:
        for tile in row:
            if isinstance(tile, int):
                free_fields.append(tile)
    return free_fields

def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    if board[0][0] == board [0][1] == board [0][2]:
        return True
    elif board[1][0] == board[1][1] == board[1][2]:
        return True
    elif board[2][0] == board[2][1] == board[2][2]:
        return True
    elif board[0][0] == board[1][0] == board[2][0]:
        return True
    elif board[0][1] == board[1][1] == board[2][1]:
        return True
    elif board[0][2] == board[1][2] == board[2][2]:
        return True
    elif board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True
    else:
        return

def draw_move(board):
    from random import randrange
    computer_choice = randrange(1,10)
    while not computer_choice in make_list_of_free_fields(board):
        computer_choice = randrange(1,10)
    for x in range(0,3):
        for y in range(0,3):
            if computer_choice == board[x][y]:
                board[x][y] = "X"

board = [[1,2,3],[4,5,6],[7,8,9]]
while True:
    display_board(board)
    enter_move(board)
    if victory_for(board):
        display_board(board)
        print("Congrats O won the game")
        break
    if len(make_list_of_free_fields(board)) > 0:
        display_board(board)
        print("Computer please take your turn:")
        draw_move(board)
        if victory_for(board):
            display_board(board)
            print("Congrats X won the game")
            break
    else:
        display_board(board)
        print("There is no winner this time")
        break
   
