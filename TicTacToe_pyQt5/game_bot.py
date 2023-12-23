import main
def minimax(board, depth = 0, is_max = True):

    #Terimation Condition
    if check_game_state(board) == 1:
        return 1
    elif check_game_state(board) == 2:
        return -1
    elif not check_game_state(board):
        return 0

    #Max
    if is_max:
        best_score = -100
        for i in board:
            for j in board:
                if board[i][j] != " ":
                    board[i][j] = "1"
                    score = minimax(board, depth + 1, is_max = False)
                    board[i][j] = " "
                    best_score = max((score, best_score))
                    return best_score
    elif not is_max:
        best_score = 100
        for i in board:
            for j in board:
                if board[i][j] != " ":


def check_game_state(board):
        for i in board: #Horizontal Check
            if i[0] == i[1] == i[2] and i[0] !=" ":
                return i[0]
        
        for i, r in enumerate(board): #Vertical Check
            column = [x[i] for x in board]
            if column[0] == column[1] == column[2] and column[0] !=" ":
                return column[0]
        
        diag1 = [r[i] for i, r in enumerate(board)] #Return diagonals
        diag2 = [r[-i-1] for i, r in enumerate(board)]

        if diag1[0] == diag1[1] == diag1[2] and diag1[0] != " ": #Diagonal check
            return diag1[0]
        if diag2[0] == diag2[1] == diag2[2] and diag2[0] != " ":
            return diag2[0]
        
        is_full = False
        for i in board:
            if not " " in 

        return False