# https://www.acmicpc.net/problem/3055
# 백준 3055 - 탈출

import copy
import sys
from collections import deque


def water_move():
    global board, waters
    water_q = deque(waters)

    while water_q:
        ci, cj = water_q.popleft()
        for di, dj in diff:
            ni = ci + di
            nj = cj + dj
            if -1 < ni < R and -1 < nj < C:
                if board[ni][nj] == stone:
                    continue
                if board[ni][nj] == 'D':
                    continue
                board[ni][nj] = water
                waters.add((ni, nj))


def hedge_move():
    global board, hedges
    hedge_q = deque(hedges)

    while hedge_q:
        ci, cj, cur_cnt = hedge_q.popleft()
        for di, dj in diff:
            ni = ci + di
            nj = cj + dj
            if -1 < ni < R and -1 < nj < C:
                if board[ni][nj] == stone:
                    continue
                if board[ni][nj] == water:
                    continue
                if board[ni][nj] == 'D':
                    return True, cur_cnt + 1
                if board[ni][nj] == blank:
                    board[ni][nj] = cur_cnt + 1
                    hedges.add((ni, nj, cur_cnt + 1))
    return False, 0


def start():
    global board, waters, hedges

    while True:
        past = copy.deepcopy(hedges)

        water_move()
        flag, cnt = hedge_move()
        if flag:
            return True, cnt

        if hedges == past or not hedges:
            return False, 0


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
stone = 'X'
water = '*'
blank = '.'
waters = set()
goals = set()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            hedge = (i, j)
            # init hedgehog distance 0
            board[i][j] = 0
        if board[i][j] == water:
            waters.add((i, j))

if hedge in goals:
    print(1)
    exit(0)
hi, hj = hedge
hedges = {(hi, hj, 0)}

flag, time = start()
if flag:
    print(time)
else:
    print("KAKTUS")
