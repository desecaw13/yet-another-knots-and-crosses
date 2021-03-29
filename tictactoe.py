from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('''+-------+-------+-------+
|       |       |       |
|   {_1}   |   {_2}   |   {_3}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {_4}   |   {_5}   |   {_6}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {_7}   |   {_8}   |   {_9}   |
|       |       |       |
+-------+-------+-------+'''.format(_1=board[0][0],_2=board[0][1],_3=board[0][2],
           _4=board[1][0],_5=board[1][1],_6=board[1][2],
           _7=board[2][0],_8=board[2][1],_9=board[2][2]))


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    try:
        pin = int(input('Enter your move: '))
    except:
        print('You must only enter a number')
        return
    if pin < 1 or pin > 9:
        print('You must enter a number in range')
        return
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == pin:
                board[row][col] = 'O'
                return True
    print('This square already taken.')
    return


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    fs = []
    
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 'X' and board[row][col] != 'O':
                fs.append((row,col))
    return fs


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    for r in range(len(board)):
        g = (True for c in range(len(board[r])) if board[r][c] == sign)
        if next(g,False) and next(g,False) and next(g,False):
            return True
    
    for c in range(len(board)):
        g = (True for r in range(len(board)) if board[r][c] == sign)
        if next(g,False) and next(g,False) and next(g,False):
            return True
    
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) \
    or (board[0][2] == sign and board[1][1] == sign  and board[2][0] == sign):
        return True
    
    return False
    # The function above uses two for loops that iterate through the rows then colunms of board
    # creating generators that contain whether or not a field is equal to sign or not and will return true if there is three matches in a row or colunm.
    # The function then uses an if statment to check if any of the two different diagonals match sign do and return true if one is.
    # If no win conditions are found then it returns false.


def draw_move(board):
    # The function draws the computer's move and updates the board.
    p_moves = make_list_of_free_fields(board)
    r,c = p_moves[randrange(len(p_moves))]
    board[r][c] = 'X'
    display_board(board)


board = [[c+r+r+1 for c in range(r,r+3)] for r in range(3)]# initializes board
board[1][1]='X'# first move, by computer
pturn = True# keeps track of whose turn it is
display_board(board)

while True:
    if pturn:
        if enter_move(board):# true when player successfully made a move, false when there was an error
            display_board(board)
            pturn = False
        else:
            print('Please try again.\n')
        if victory_for(board,'O'):
            print('You have won. Yay!')
            break
    else:
        draw_move(board)
        pturn = True
        if victory_for(board,'X'):
            print('The computor won. Oh no!')
            break
        
    if len(make_list_of_free_fields(board)) <= 0:# checks for a tie, i.e. no free spaces left
        print("Its a cat's game.")
        break
