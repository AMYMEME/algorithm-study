# https://www.acmicpc.net/problem/14500
# 백준 14500 - 테트로미노

import sys


def make_tetromino(ci, cj, sum_value, count):
    global answer
    if count == 4:
        answer = max(answer, sum_value)
        return
    for di, dj in diff:
        ni = di + ci
        nj = dj + cj
        if -1 < ni < N and -1 < nj < M and check[ni][nj] == 0:
            check[ni][nj] = 1
            make_tetromino(ni, nj, sum_value + board[ni][nj], count + 1)
            check[ni][nj] = 0


def make_woo(ci, cj):
    global answer
    if ci < N - 1 and 0 < cj < M - 1:
        sum_value = board[ci][cj] + board[ci][cj - 1] + board[ci][cj + 1] + board[ci + 1][cj]
        answer = max(answer, sum_value)
    if ci > 0 and 0 < cj < M - 1:
        sum_value = board[ci][cj] + board[ci][cj - 1] + board[ci][cj + 1] + board[ci - 1][cj]
        answer = max(answer, sum_value)
    if 0 < ci < N - 1 and cj > 0:
        sum_value = board[ci][cj] + board[ci - 1][cj] + board[ci + 1][cj] + board[ci][cj - 1]
        answer = max(answer, sum_value)
    if 0 < ci < N - 1 and cj < M - 1:
        sum_value = board[ci][cj] + board[ci - 1][cj] + board[ci + 1][cj] + board[ci][cj + 1]
        answer = max(answer, sum_value)


diff = [(0, 1), (1, 0), (-1, 0), (0, -1)]
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        check[i][j] = 1
        make_tetromino(i, j, board[i][j], 1)
        check[i][j] = 0
        make_woo(i, j)
print(answer)
