# https://www.acmicpc.net/problem/1005
# ACM Craft

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())

    graph = [[0, 0, 0, set()] for _ in range(N)]  # building_time, sum_building_time, in_degree, out_vertexes

    for idx, value in enumerate(map(int, sys.stdin.readline().split())):
        graph[idx][0] = value
        graph[idx][1] = value  # initialize

    for _ in range(K):
        in_v, out_v = map(int, sys.stdin.readline().split())
        in_v -= 1
        out_v -= 1
        graph[out_v][2] += 1
        graph[in_v][3].add(out_v)

    goal = int(sys.stdin.readline())

    leaves = deque(filter(lambda x: x[2] == 0, graph))

    while leaves:
        building_time, sum_time, in_degree, out_vertexes = leaves.popleft()
        for nxt in out_vertexes:
            graph[nxt][2] -= 1
            graph[nxt][1] = max(graph[nxt][1], graph[nxt][0] + sum_time)
            if graph[nxt][2] == 0:
                leaves.append(graph[nxt])
    print(graph[goal - 1][1])
