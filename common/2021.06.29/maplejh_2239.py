# https://www.acmicpc.net/problem/2239
import sys


def check(r, c, value):
    for i in range(9):
        if board[r][i] == value or board[i][c] == value:
            return False
    br = (r // 3) * 3
    bc = (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == value:
                return False
    return True


def dfs(cnt):
    if cnt == 81:
        for row in board:
            print("".join(map(str,row)))
        sys.exit(0)
    r = cnt // 9
    c = cnt % 9
    if board[r][c]:
        dfs(cnt + 1)
    else:
        for i in range(1, 10):
            if check(r, c, i):
                board[r][c] = i
                dfs(cnt + 1)
        board[r][c] = 0  # 바로 전 cnt 보다 더 많이 돌아갈 때


board = []
for i in range(9):
    board.append(list(map(int, list(sys.stdin.readline().strip()))))
dfs(0)
