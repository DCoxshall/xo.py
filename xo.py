import time

board = [[7,8,9],[4,5,6],[1,2,3]]

def printBoard(b):
    print("   #   #")
    print(" ", b[0][0], " # ", b[0][1], " # ", b[0][2], sep='')
    print("###########")
    print(" ", b[1][0], " # ", b[1][1], " # ", b[1][2], sep='')
    print("###########")
    print(" ", b[2][0], " # ", b[2][1], " # ", b[2][2], sep='')
    print("   #   #")

def validMove(move):
    if move == 1:
        move = board[2][0]
    elif move== 2:
        move = board[2][1]
    elif move== 3:
        move = board[2][2]
    elif move== 4:
        move = board[1][0]
    elif move== 5:
        move = board[1][1]
    elif move== 6:
        move = board[1][2]
    elif move== 7:
        move = board[0][0]
    elif move== 8:
        move = board[0][1]
    elif move== 9:
        move = board[0][2]
    
    if move == 'X' or move == 'O':
        return False
    else:
        return True

def takeMove(move):
    if move == 1:
        board[2][0] = turn
    if move == 2:
        board[2][1] = turn
    if move == 3:
        board[2][2] = turn
    if move == 4:
        board[1][0] = turn
    if move == 5:
        board[1][1] = turn
    if move == 6:
        board[1][2] = turn
    if move == 7:
        board[0][0] = turn
    if move == 8:
        board[0][1] = turn
    if move == 9:
        board[0][2] = turn
        

def boardTerminal():
    if board[0][0] == board[0][1] == board [0][2]:
        return True
    elif board[1][0] == board[1][1] == board [1][2]:
        return True
    elif board[2][0] == board[2][1] == board [2][2]:
        return True

    elif board[1][0] == board[2][0] == board [0][0]:
        return True
    elif board[1][1] == board[2][1] == board [0][1]:
        return True
    elif board[1][2] == board[2][2] == board [0][2]:
        return True

    elif board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[2][0] == board[1][1] == board[0][2]:
        return True
    else:
        return False


turn = 'X'
while boardTerminal() == False:
    printBoard(board)

    move = 10

    while move > 9 or move < 1 or not validMove(move):
        move = int(input(f"Input the position to go, {turn}: "))
    takeMove(move)
    if boardTerminal() == True:
        print("Game Over")
        printBoard(board)
        time.sleep(5)
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'




    


