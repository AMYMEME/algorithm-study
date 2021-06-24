# https://www.acmicpc.net/problem/1613
# 역사
# pypy

import sys

n, k = map(int, sys.stdin.readline().split())
board = [[0] * n for _ in range(n)]

for _ in range(k):
    before, after = map(int, sys.stdin.readline().split())
    before -= 1
    after -= 1
    board[before][after] = -1
    board[after][before] = 1

for x in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][x] == -1 and board[x][j] == -1:
                board[i][j] = -1
                board[j][i] = 1

s = int(sys.stdin.readline())
for _ in range(s):
    num_1, num_2 = map(int, sys.stdin.readline().split())
    print(board[num_1 - 1][num_2 - 1])
