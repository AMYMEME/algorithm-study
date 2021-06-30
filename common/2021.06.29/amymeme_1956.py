# https://www.acmicpc.net/problem/1956
# 운동
# pypy
import sys

V, E = map(int, sys.stdin.readline().split())
graph = [[float('inf')] * V for _ in range(V)]

for road in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start - 1][end - 1] = weight

for x in range(V):
    for i in range(V):
        for j in range(V):
            if graph[i][x] != -1 and graph[x][j] != -1:
                graph[i][j] = min(graph[i][j], graph[i][x] + graph[x][j])

result = float('inf')
for i in range(V):
    result = min(result, graph[i][i])
if result == float('inf'):
    print(-1)
else:
    print(result)
