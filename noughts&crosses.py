# Joe Olpin
# tic-tac-toe
# 8/18/2021

def main():
    turn = 0
    while True:
        for i in range(1, 3):
            print(str(i)+"'s turn")
            move = getInput()  # returns [row,column]
            while not move:  # try again if move returned an error
                move = getInput()

            board[move[0]][move[1]] = i  # makes the move official

            print(drawBoard(board))

            winner = whoWon(board)
            if winner:  # 1 and 2 are both true, a tie and no win are both false
                return winner

            turn += 1
            if turn >= 9:  # after 9 turns all spots on board have been taken
                return 0  # Tie, all moves have been made


def getInput():
    p = input('Enter row,column: ')
    try:
        p = p.split(',')
        p = [int(v.strip()) - 1 for v in p]  # '1'=0, '2'=1, '3'=2
    except ValueError:
        print('Please use whole numbers.')
        return
    if len(p) != 2:
        print('You must have only two numbers and only one comma.')
        return
    elif not (0 <= p[0] <= 2 and 0 <= p[1] <= 2):
        print('You need to keep the numbers between 1 and 3.')
        return
    elif board[p[0]][p[1]] != 0:
        print("This spot is already taken.")
        return
    else:
        return p


def whoWon(b):
    for x in b:
        if x[0] == x[1] == x[2] != 0:  # checks for horizontal wins
            return x[0]
    for y in range(len(b)):
        if b[0][y] == b[1][y] == b[2][y] != 0:  # checks for vertical wins
            return b[0][y]
    if b[0][0] == b[1][1] == b[2][2] != 0:  # checks for diagonal wins
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != 0:  # checks for diagonal wins
        return b[1][1]
    return False


def drawBoard(b):
    nts = {0: ' ', 1: 'X', 2: 'O'}  # integer in board to string for printing
    s = len(b)
    out = ''
    for i in range(s):
        out += (' ---' * s) + '\n|'
        for j in range(s):
            out += ' {0} |'.format(nts[b[i][j]])
        out += '\n'
    out += (' ---' * s)

    return out


if __name__ == '__main__':
    print('Two Player Tic-Tac-Toe:\n'
          'Player 1 is Xs and player 2 in Os. Input the row, then a comma, and then the column.\n'
          'The top left is 1,1 and bottom right is 3,3. Make sure your values are in that range.\n')
    board = [[0 for _ in range(3)] for __ in range(3)]
    w = main()
    if w == 0:
        print('No more moves left. It was a tie.')
    elif w == 1:
        print('Player 1 (X) won.')
    elif w == 2:
        print('Player 2 (O) won.')
