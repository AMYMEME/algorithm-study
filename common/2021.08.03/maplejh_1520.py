# https://www.acmicpc.net/problem/1520
import sys
from collections import deque

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
M, N = map(int, sys.stdin.readline().split())
board = []
dp = [[0] * N for _ in range(M)]

for _ in range(M):
    board.append(list(map(int, sys.stdin.readline().split())))

dp[0][0] = 1
q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if -1 < nx < M and -1 < ny < N:
            if board[nx][ny] < board[x][y]:
                q.append((nx, ny))
                dp[x][y] += 1

print(dp[-1][-2] + dp[-2][-1])
