# https://www.acmicpc.net/problem/2239
# 스도쿠
import sys


def get_checking_set(i, j):
    checking_set = set()
    si = i // 3 * 3
    sj = j // 3 * 3

    checking_set = checking_set.union(set(board[i]))
    for idx in range(9):
        checking_set.add(board[idx][j])
    for row in [row[sj:sj + 3] for row in board[si:si + 3]]:
        for x in row:
            checking_set.add(x)
    return checking_set


def dfs(blanks_idx):
    global board
    if blanks_idx == len(blanks):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=' ')
            print()
        exit(0)

    i, j = blanks[blanks_idx]
    checking_set = get_checking_set(i, j)

    for x in range(1, 10):
        if x in checking_set:
            continue
        board[i][j] = x
        dfs(blanks_idx + 1)
        board[i][j] = 0


board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
dfs(0)
