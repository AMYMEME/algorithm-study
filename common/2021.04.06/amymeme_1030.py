# https://www.acmicpc.net/problem/1030
# 백준 1030 - 프렉탈 평면

import sys


def fractal():
    global board
    new_board = []
    board_len = len(board)
    for i in range(N):
        if i < middle_start or i >= middle_start + K:
            for row in board:
                new_board.append(row * N)
        else:
            for row in board:
                new_row = row * middle_start + [1] * board_len * K + row * middle_start
                new_board.append(new_row)
    board = new_board


s, N, K, R1, R2, C1, C2 = map(int, sys.stdin.readline().split())
middle_start = (N - K) // 2
board = [[0]]

clock = 0
while clock < s:
    clock += 1
    fractal()

only_rows = board[R1:R2 + 1]
for row in only_rows:
    for c_idx, value in enumerate(row):
        if C1 <= c_idx <= C2:
            print(value, end='')
    print()
