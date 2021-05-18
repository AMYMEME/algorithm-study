# https://www.acmicpc.net/problem/2458
# 백준 2458 - 키 순서
# pypy 제출

import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[0] * N for _ in range(N)]  # 0 for unknown

for i in range(N):
    graph[i][i] = 1  # 1 for self

for _ in range(M):
    smaller, taller = map(int, sys.stdin.readline().split())
    graph[smaller - 1][taller - 1] = -1
    graph[taller - 1][smaller - 1] = 1

# i -> k -> j
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == -1 and graph[k][j] == -1:
                graph[i][j] = -1
                graph[j][i] = 1

cnt = 0
for i in range(N):
    if all(graph[i]):
        cnt += 1
print(cnt)
