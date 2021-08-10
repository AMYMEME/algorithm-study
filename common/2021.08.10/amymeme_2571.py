# https://www.acmicpc.net/problem/2571
# 색종이


import sys


def print_board():
    for _i in range(100):
        for _j in range(100):
            print(board[_i][_j], end=' ')
        print()


board = [[0] * 100 for _ in range(100)]
N = int(sys.stdin.readline())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            board[i][j] = 1

for x in range(100):
    for y in range(100):
        if board[x][y]:
            board[x][y] += board[x - 1][y]
print_board()

answer = 0
for x in range(100):
    for y in range(100):
        h = 100
        for z in range(y, 100):
            h = min(h, board[x][z])
            answer = max(answer, h * (z - y + 1))
print(answer)
