board=[list(map(int, input())) for _ in range(9)]

def valid(col, row, value):
    #가로
    for i in range(9):
        if board[col][i]==value:
            return False
    #세로
    for i in range(9):
        if board[i][row]==value:
            return False
    #상자
    box_row=(row//3)*3
    box_col=(col//3)*3
    for i in range(box_col, box_col+3):
        for j in range(box_row, box_row+3):
            if board[i][j]==value:
                return False
    return True

def empty():
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return i, j
    return None, None

def sol():
    col, row = empty()
    if col==None:
        return True
    else:
        for i in range(1, 10):
            if valid(col, row, i):
                board[col][row]=i
                if sol():
                    return True
                board[col][row]=0
        return False

sol()
for row in board:
    print(''.join(map(str, row)))
