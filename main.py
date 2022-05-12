import random
import copy as cp
# NOTE use cp.deepcopy() so the temp variable isn't linked with the other

class Cell:
    def __init__(self, position, location, max_val, min_val):
        self.position = position
        self.location = location # NOTE this is a list, [0] is row info and [1] is col info
        self.min_val = min_val
        self.max_val = max_val

def generate_cells(board):
    uboard = cp.deepcopy(board)
    for i in range(len(uboard)):
        for j in range(len(uboard[i])):
            if uboard[i][j] != 'X' and uboard[i][j] != 'O':
                uboard[i][j] = Cell(uboard[i][j], [i,j], 0, 0)
                uboard[i][j].max_val = max_val(board, [i, j])
                uboard[i][j].min_val = min_val(board, [i, j])
                # NOTE convert uboard[i][j] into list of maxval and minval from objects
                uboard[i][j] = [uboard[i][j].position, uboard[i][j].max_val, uboard[i][j].min_val]
    return uboard

def max_val(board, location): # NOTE only generates one max_val by a given location, not entire board
    maxval = 0
    if board[location[0]][location[1]] != 'O' and board[location[0]][location[1]] != 'X':
        maxval += check_horizontal(board, location[0], 'max') # need row
        maxval += check_vertical(board, location[1], 'max') # need column
        # NOTE diagonal check is splitted into left and right diagonal for convienence
        maxval += left_diagonal(board, location[0], location[1], 'max')
        maxval += right_diagonal(board, location[0], location[1], 'max')
    
    return maxval

def min_val(board, location):
    minval = 0
    if board[location[0]][location[1]] != 'O' and board[location[0]][location[1]] != 'X':
        minval -= check_horizontal(board, location[0], 'min')
        minval -= check_vertical(board, location[1], 'min')
        minval -= left_diagonal(board, location[0], location[1], 'min')
        minval -= right_diagonal(board, location[0], location[1], 'min')
    
    return minval

def check_horizontal(board, row, u_type):
    opposed = 'X'
    sign = 'O'
    if u_type == 'min':
        opposed = 'O'
        sign = 'X'

    v = 0
    unfilled = 0
    for i in range(3): # 3 == len(board)'s row
        if board[row][i] != opposed:
            unfilled += 1
            if board[row][i] == sign:
                v += 1

    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def check_vertical(board, col, u_type):
    opposed = 'X'
    sign = 'O'
    if u_type == 'min':
        opposed = 'O'
        sign = 'X'

    v = 0
    unfilled = 0
    for i in range(3): # 3 == len(board)'s column
        if board[i][col] != opposed:
            unfilled += 1
            if board[i][col] == sign:
                v += 1

    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def left_diagonal(board, row, col, u_type): # NOTE top_left to bottom_right diagonal check
    opposed = 'X'
    sign = 'O'
    if u_type == 'min':
        opposed = 'O'
        sign = 'X'
        
    v = 0
    unfilled = 0
    if row == col:
        for i in range(3):
            if board[i][i] != opposed:
                unfilled += 1
                if board[i][i] == sign:
                    v += 1

    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def right_diagonal(board, row, col, u_type):
    opposed = 'X'
    sign = 'O'
    if u_type == 'min':
        opposed = 'O'
        sign = 'X'

    v = 0
    unfilled = 0
    state = False
    for i in range(len(board)):
        if board[i][abs(i-2)] == board[row][col]:
            state = True
        if board[i][abs(i-2)] != opposed:
            unfilled += 1
            if board[i][abs(i-2)] == sign:
                v +=1
    
    if unfilled == 3 and state == True:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def dispUboard(uboard):
    print('\n')
    count = 0
    print("Utility Board:\n")
    for i in range(len(uboard)):
        for j in range(len(uboard[i])):
            count += 1
            if uboard[i][j] == 'O' or uboard[i][j] == 'X':
                print('  ',uboard[i][j],end='     ')
            else:
                print(uboard[i][j],end='  ')
            if count%3 == 0:
                print('\n')


def checkWin(board, sign):
    if checkHorizontal(board, sign) == True:
        return True
    if checkVertical(board, sign) == True:
        return True
    if checkDiagonal(board, sign) == True:
        return True
    return False

def checkTie(board):
    filled = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O' or board[i][j] == 'X':
                filled += 1
    if filled == 9:
        return True
    return False

def checkDiagonal(board, sign):
    for i in range(len(board)):
        filled = 0
        if board[0][0] == sign:
            for j in range(len(board[i])):
                if board[j][j] == sign:
                    filled += 1
        elif board[0][2] == sign:
            for j in range(len(board[i])):
                if board[0+j][2-j] == sign:
                    filled += 1
    if filled == 3:
        return True
    return False

def checkHorizontal(board, sign): # NOTE BUGGY so fix it
    for i in range(len(board)):
        if board[i][0] == sign:
            filled = 0
            for j in range(len(board[i])):
                if board[i][j] == sign:
                    filled += 1
            if filled == 3:
                return True
    return False

def checkVertical(board, sign):
    for i in range(len(board)):  
        if board[0][i] == sign:
            filled = 0
            for j in range(len(board[i])):
                if board[j][i] == sign:
                    filled += 1
            if filled == 3:
                return True
    return False

def dispboard(board):
    print('\n')
    count = 0
    print('Tictactoe Board:\n')
    for i in range(len(board)):
        for j in range(len(board[i])):
            count += 1
            print(board[i][j],end='  ')
            if count%3 == 0:
                print('\n')

def checkCompatible(board, move, sign):
    i = 2
    if move <= 2:
        i = 0
    elif move >= 3 and move <= 5:
        i = 1
    
    loc = [i,(move-(i*3))]

    if board[loc[0]][loc[1]] == move:
        board[loc[0]][loc[1]] = sign
        return True
    else:
        print("Please select an empty spot and try again.")
        return False

def computerDecision(board):
    while (checkTie(board) == False) and (checkWin(board, 'X') == False):
        uboard = generate_cells(board)
        dispUboard(uboard)
        dispboard(board)

        # TODO run minimax algorithm here
        computer_decision = minimax_algorithm(uboard)
        computer_decision = int(computer_decision)

        if checkCompatible(board, computer_decision, 'O') == True:
            if checkTie(board) == True:
                dispboard(board)
                play_again = input("\nThis is a tie game, to play again enter any key, otherwise enter 'q' to quit.\nYour decision: ")
                if play_again == 'q':
                    return
                else:
                    board = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
                    GameInitializer(board)

            elif checkWin(board, 'O') == True:
                dispboard(board)
                print("The computer won!")
                return
            else:
                playerDecision(board)
        else:
            computerDecision(board)

def playerDecision(board):
    while (checkTie(board) == False) and (checkWin(board, 'O') == False):
        dispboard(board)
        player_decision = input("\n(The player's turn) Enter the empty position you want to place your 'X': ")
        player_decision = int(player_decision)

        if checkCompatible(board, player_decision, 'X') == True:
            if checkTie(board) == True:
                dispboard(board)
                play_again = input("\nThis is a tie game, if you want to play again enter 'p', to quit enter any key.\nYour decision: ")
                if play_again == 'q':
                    return
                else:
                    board = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
                    GameInitializer(board)

            elif checkWin(board, 'X') == True:
                dispboard(board)
                print("The player won!")
                return
            else:
                computerDecision(board)
        else:
            playerDecision(board)

def GameInitializer(board):
    choice = input("\nDo you want to go first or the computer goes first?\nEnter 'c' for computer first, or 'p' if you would like to go first\nYour Choice: ")
    if choice == 'c':
        computerDecision(board)
    elif choice == 'p':
        playerDecision(board)
    else:
        print("\nPlease enter 'c' or 'p' and try again.")
        GameInitializer(board)

def minimax_algorithm(ub): # should return a pos, such as 4, not index[1,1]
    optimal = 0
    options = []
    redundant_optimal = [] # This adds the random feature for the computer decision.
    for i in range(len(ub)):
        for j in range(len(ub[i])):
            if ub[i][j] != 'X' and ub[i][j] != 'O':
                # NOTE uboard[i][j's 0 is position, 1 is maxval, 2 is minval
                if ub[i][j][1] >= 10:
                    return ub[i][j][0]
                elif ub[i][j][2] <= -10:
                    return ub[i][j][0]
                else:
                    if abs(ub[i][j][1]) == abs(ub[i][j][2]):
                        # NOTE if abs of max = abs of min, add 1 to their sum. Why? because we want to win more more than limiting the enemy
                        options.append([abs(ub[i][j][1]) + abs(ub[i][j][2])+1, ub[i][j][0]])
                    else: # NOTE, [0] is the total val of abs(max + min). [1] is the index
                        options.append([abs(ub[i][j][1]) + abs(ub[i][j][2]), ub[i][j][0]])

    optimal = max(options) # NOTE for redundant_optimal, [0] is index, [1] is val
    for i in range(len(options)):
        if options[i][0] == optimal[0]:
            redundant_optimal.append(options[i][1])

#     redundant_optimal.append(optimal[1])
#     randnum = random.randint(0,len(redundant_optimal)-1)
#     return redundant_optimal[randnum]
    return redundant_optimal[0]


# NOTE play game here

init_board = [[0, 1, 2], 
              [3, 4, 5],
              [6, 7, 8]]

GameInitializer(init_board)