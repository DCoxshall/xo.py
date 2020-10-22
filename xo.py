import time, math

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

def takeMove(move, turn):
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

def get_possible_moves():
    validMoves = []
    for j in board:
        for i in j:
            if i != 'X' and i != 'O':
                if board.index(j) == 0:
                    if j.index(i) == 0:
                        validMoves.append(7)
                    elif j.index(i) == 1:
                        validMoves.append(8)
                    elif j.index(i):
                        validMoves.append(9)    
                elif board.index(j) == 1:
                    if j.index(i) == 0:
                        validMoves.append(4)
                    elif j.index(i) == 1:
                        validMoves.append(5)
                    elif j.index(i) == 2:
                        validMoves.append(6)   
                else:
                    if j.index(i) == 0:
                        validMoves.append(1)
                    elif j.index(i) == 1:
                        validMoves.append(2)
                    elif j.index(i) == 2:
                        validMoves.append(3)
    return(validMoves)

def get_board_state():
    if boardTerminal():
        return 'OVER'
    else:
        over = True
        for j in board:
            for i in j:
                if i != 'X' and 'i' != 'O':
                    over = False
        if over:
            return 'DRAW'
        

def undo(move):
    if move == 1:
        board[2][0] = move
    elif move == 2:
        board[2][1] = move
    elif move == 3:
        board[2][2] = move
    elif move == 4:
        board[1][0] = move
    elif move == 5:
        board[1][1] = move
    elif move == 6:
        board[1][2] = move
    elif move == 7:
        board[0][0] = move
    elif move == 8:
        board[0][1] = move
    elif move == 9:
        board[0][2] = move

def winner():
    if board[0][0] == board[0][1] == board [0][2] == 'X':
        return 'X'
    elif board[1][0] == board[1][1] == board [1][2] == 'X':
        return 'X'
    elif board[2][0] == board[2][1] == board [2][2] == 'X':
        return 'X'

    elif board[1][0] == board[2][0] == board [0][0] == 'X':
        return 'X'
    elif board[1][1] == board[2][1] == board [0][1] == 'X':
        return 'X'
    elif board[1][2] == board[2][2] == board [0][2] == 'X':
        return 'X'

    elif board[0][0] == board[1][1] == board[2][2] == 'X':
        return 'X'
    elif board[2][0] == board[1][1] == board[0][2] == 'X':
        return 'X'

    
    if board[0][0] == board[0][1] == board [0][2] == 'O':
        return 'O'
    elif board[1][0] == board[1][1] == board [1][2] == 'O':
        return 'O'
    elif board[2][0] == board[2][1] == board [2][2] == 'O':
        return 'O'

    elif board[1][0] == board[2][0] == board [0][0] == 'O':
        return 'O'
    elif board[1][1] == board[2][1] == board [0][1] == 'O':
        return 'O'
    elif board[1][2] == board[2][2] == board [0][2] == 'O':
        return 'O'

    elif board[0][0] == board[1][1] == board[2][2] == 'O':
        return 'O'
    elif board[2][0] == board[1][1] == board[0][2] == 'O':
        return 'O'

def minimax(isMaxTurn, maximizerMark, turn):
    state = get_board_state()
    if state == 'DRAW':
        return 0
    elif state == 'OVER':
        if winner() == maximizerMark:
            return 1
        else:
            return -1

    scores = [0]

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    for move in get_possible_moves():
        takeMove(move, turn)
        scores.append(minimax(not isMaxTurn, maximizerMark, turn))
        undo(move)
    
    if isMaxTurn:
        return(max(scores))
    else:
        return(min(scores))

        


def make_best_move():
    bestScore = -math.inf
    bestMove = None
    for move in get_possible_moves():
        takeMove(move, turn)
        score = minimax(False, 'O', 'O')
        undo(move)
        if score > bestScore:
            bestScore = score
            bestMove = move
    return(bestMove)

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

    while (move > 9 or move < 1 or not validMove(move)) and (turn == 'X'):
        move = int(input(f"Input the position to go, {turn}: "))

    if turn == 'O':
        move = make_best_move()

    takeMove(move, turn)
    if boardTerminal() == True:
        print(f"Game Over: {turn} wins!")
        printBoard(board)
        time.sleep(5)
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'





    


