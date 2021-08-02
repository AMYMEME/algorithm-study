# https://www.acmicpc.net/problem/1520
# 내리막 길


import sys
from collections import deque

diff = [(0, 1), (1, 0), (-1, 0), (0, -1)]
M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

goal_value = board[-1][-1]
q = deque([(board[0][0], 0, 0)])  # value, i , j
count = 0

while q:
    value, i, j = q.popleft()
    value *= -1
    for di, dj in diff:
        ni = i + di
        nj = j + dj
        if -1 < ni < M and -1 < nj < N and board[ni][nj] < value:
            if ni == M - 1 and nj == N - 1:
                count += 1
                continue
            if board[ni][nj] <= goal_value:
                continue
            q.append((board[ni][nj], ni, nj))
print(count)
