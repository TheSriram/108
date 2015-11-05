# Tic Tac Toe

def win(board):
    # look for horizontal, vertical and diagonal matches
    size = len(board)
    count = 0
    criss = []
    cross = []
    for i in board:
        curr_row = []
        curr_col = []
        for j in range(0, len(i)):
            if board[count][j] != '-':
                curr_row.append(board[count][j])
            if board[j][count] != '-':
                curr_col.append(board[j][count])
            if (count == j):
                if board[count][j] != '-':
                    criss.append(board[count][j])
            if ((count + j + 1)) == size:
                if board[count][j] != '-':
                    cross.append(board[count][j])
        count = count + 1

        if len(curr_row) == size:
            if set(curr_row) == {'X'}:
                return 'X'
            elif set(curr_row) == {'O'}:
                return 'O'

        if len(curr_col) == size:
            if set(curr_col) == {'X'}:
                return 'X'
            elif set(curr_col) == {'O'}:
                return 'O'

        if len(criss) == size:
            if set(criss) == {'X'}:
                return 'X'
            elif set(criss) == {'O'}:
                return 'O'

        if len(cross) == size:
            if set(cross) == {'X'}:
                return 'X'
            elif set(cross) == {'O'}:
                return 'O'


def move(board, player):

    size = len(board) * len(board)
    count = 0
    i_count = 0
    for i in board:
        for j in range(0, len(i)):
            if board[i_count][j] == '-':
                count = count + 1
        i_count = i_count + 1
    if count == size:
        # Empty
        return 0, (len(board)/2, len(board)/2)
    if count == 0:
        # Full Board
        return 0, -1

    nextplayer = 'O' if player == 'X' else 'X'
    winner = win(board)
    if winner == 'X':
        # if the winner is X, then current player is 'O'
        # But does it lead to a winning situation for 'X'? Yes 
        # return +1, -1 (since we are maximizing for X (+1), and -1 since game is over)
        return 1, -1
    elif winner == 'O':
        # if the winner is O, then current player is 'X'
        # But does it lead to a winning situation for 'X'? No
        # return -1, -1 (since we are minimizing for X (+1), and -1 since game is over)

        return -1, -1

    list_indexes = []
    res_list = []
    i_count = 0
    for i in board:
        for j in range(0, len(i)):
            if board[i_count][j] == '-':
                list_indexes.append((i_count,j))
        i_count = i_count + 1

    # list_indexes contains all the indexes where element is '-'
    for position in list_indexes:
        i, j = position
        board[i][j] = player
        # recursively call move, for every position that is unfilled.
        ret, _ = move(board, nextplayer)
        res_list.append(ret)
        # important to go back and mark the postion tried as unfilled again.
        board[i][j] = '-'

    if player == 'X':
        # since we are maximizing for X (remember note from earlier), we return
        # 1 if X is in a winning position. if there is a winning position, we 
        # find the index of the position, and use that as index on list_indexes.
        max_elem = max(res_list)
        return max_elem, list_indexes[res_list.index(max_elem)]

    else:
        # similair in the case of O, except we are minimizing.
        min_elem = min(res_list)
        return min_elem, list_indexes[res_list.index(min_elem)]

