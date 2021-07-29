# https://www.acmicpc.net/problem/1937
# 욕심쟁이 판다

import sys
import heapq

diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n = int(sys.stdin.readline())
board = []
pq = []

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
    for j, value in enumerate(row):
        heapq.heappush(pq, (-value, i, j))

dp = [[0] * n for _ in range(n)]
answer = 0

while pq:
    value, i, j = heapq.heappop(pq)
    value *= -1
    near_max = 0
    for di, dj in diff:
        ni = i + di
        nj = j + dj
        if -1 < ni < n and -1 < nj < n and board[ni][nj] > value:
            near_max = max(near_max, dp[ni][nj])
    dp[i][j] = near_max + 1
    answer = max(answer, near_max + 1)

print(answer)
