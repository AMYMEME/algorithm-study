# https://www.acmicpc.net/problem/15683
# 백준 15683 - 감시

import copy
import sys
from itertools import chain


def dfs(cnt):
    global ans, board
    if cnt == len(cctv):
        if check() < ans:
            ans = check()

        return

    ci, cj = cctv[cnt]
    cctv_num = board[ci][cj]
    if cctv_num == 1:
        circle = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]
    elif cctv_num == 2:
        circle = [(1, 0, 1, 0), (0, 1, 0, 1)]
    elif cctv_num == 3:
        circle = [(1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1)]
    else:
        circle = [(1, 1, 1, 0), (0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1)]

    tmp = copy.deepcopy(board)
    for c in circle:
        for idx, value in enumerate(c):
            if value:
                di, dj = diff[idx]
                monitor(ci, cj, di, dj)
        dfs(cnt + 1)
        board = copy.deepcopy(tmp)


def monitor(ci, cj, di, dj):
    ni = ci + di
    nj = cj + dj
    while -1 < ni < N and -1 < nj < M and board[ni][nj] != 6:
        if board[ni][nj] == 0:
            board[ni][nj] = 7
        ni += di
        nj += dj


def check():
    return list(chain(*board)).count(0)


diff = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # left, up, right, down
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cctv = []
ans = N * M - len(cctv)

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            continue
        if board[i][j] == 5:  # 어차피 dfs와 관련 없이 모든 방향이니 맨 먼저 해줌
            for di, dj in diff:
                monitor(i, j, di, dj)
        elif board[i][j] < 6:
            cctv.append((i, j))
        ans -= 1
dfs(0)
print(ans)
