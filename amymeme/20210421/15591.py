# https://www.acmicpc.net/problem/15591
# 백준 15591 - MooTube (Silver)
# Pypy 제출

import sys
from collections import defaultdict, deque

N, Q = map(int, sys.stdin.readline().split())
graph = defaultdict(dict)


def find(_from, value_limit):
    global graph
    q = deque([(_from, 1000000001)])
    visited = {_from}
    count = 0

    while q:
        to, weight = q.popleft()
        for next_to, next_weight in graph[to].items():
            if next_to in visited:
                continue
            if weight > next_weight:
                q.append((next_to, next_weight))
                if next_weight >= value_limit:
                    count += 1
            else:
                q.append((next_to, weight))
                if weight >= value_limit:
                    count += 1
            visited.add(next_to)
    return count


for _ in range(N - 1):
    node1, node2, weight = map(int, sys.stdin.readline().split())
    graph[node1][node2] = weight
    graph[node2][node1] = weight

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(find(v, k))
