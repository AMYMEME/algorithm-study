# https://www.acmicpc.net/problem/1956
import sys

INF = 1e9
V, E = map(int, sys.stdin.readline().split())
board = [[INF] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    board[a][b] = c

# 플로이드 와샬
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

result = INF
for i in range(1, V + 1):
    result = min(result, board[i][i])

print(result if result != INF else -1)
