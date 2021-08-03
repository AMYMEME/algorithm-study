# https://www.acmicpc.net/problem/1520
# 내리막 길


import sys
import heapq

diff = [(0, 1), (1, 0), (-1, 0), (0, -1)]
M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[0] * N for _ in range(M)]

pq = []
dp[0][0] = 1
heapq.heappush(pq, (-board[0][0], 0, 0))  # min heap

while pq:
    value, i, j = heapq.heappop(pq)
    value *= -1

    for di, dj in diff:
        ni = i + di
        nj = j + dj
        if -1 < ni < M and -1 < nj < N and board[ni][nj] < value:
            if dp[ni][nj]:
                dp[ni][nj] += dp[i][j]
                continue
            dp[ni][nj] += dp[i][j]
            heapq.heappush(pq, (-board[ni][nj], ni, nj))


print(dp[-1][-1])
'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''