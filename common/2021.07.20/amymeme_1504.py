# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

import sys

inf = float('INF')


def floyd():
    global graph
    for aux in range(N):
        for start in range(N):
            for to in range(N):
                if graph[start][aux] < inf and graph[aux][to] < inf:
                    graph[start][to] = min(graph[start][to], graph[start][aux] + graph[aux][to])


def solution(start, aux1, aux2, dest):
    if graph[start][aux1] == inf or graph[aux1][aux2] == inf or graph[aux1][dest] == inf:
        return -1
    return graph[start][aux1] + graph[aux1][aux2] + graph[aux2][dest]


N, E = map(int, sys.stdin.readline().split())
graph = [[inf] * N for _ in range(N)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
v1, v2 = map(int, sys.stdin.readline().split())
floyd()
print(min(solution(0, v1 - 1, v2 - 1, N - 1), solution(0, v2 - 1, v1 - 2, N - 1)))
