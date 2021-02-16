# https://www.acmicpc.net/problem/14500
# 백준 14500 - 테트로미노

import sys


def make_tetromino(ci, cj):
    if len(polyominos) == 4:
        calculate(polyominos)
        return
    for di, dj in diff:
        ni, nj = di + ci, dj + cj
        if -1 < ni < N and -1 < nj < M and (ni, nj) not in polyominos:
            polyominos.add((ni, nj))
            make_tetromino(ni, nj)
            polyominos.remove((ni, nj))


def make_woo(ci, cj):
    if ci < N - 1 and 0 < cj < M - 1:
        calculate({(ci, cj), (ci, cj - 1), (ci, cj + 1), (ci + 1, cj)})  # ㅜ
    if ci > 0 and 0 < cj < M - 1:
        calculate({(ci, cj), (ci, cj - 1), (ci, cj + 1), (ci - 1, cj)})  # ㅗ
    if 0 < ci < N - 1 and cj > 0:
        calculate({(ci, cj), (ci - 1, cj), (ci + 1, cj), (ci, cj - 1)})  # ㅓ
    if 0 < ci < N - 1 and cj < M - 1:
        calculate({(ci, cj), (ci - 1, cj), (ci + 1, cj), (ci, cj + 1)})  # ㅏ


def calculate(polyominos):
    global answer
    sum_value = 0
    for polyomino in polyominos:
        i, j = polyomino
        sum_value += board[i][j]
    answer = max(answer, sum_value)


diff = [(0, 1), (1, 0), (-1, 0), (0, -1)]
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
polyominos = set()
answer = 0

for i in range(N):
    for j in range(M):
        make_tetromino(i, j)
        make_woo(i, j)
print(answer)
