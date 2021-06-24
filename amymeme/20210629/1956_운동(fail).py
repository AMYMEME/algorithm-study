# https://www.acmicpc.net/problem/1956
# 운동
import heapq
import sys
from collections import defaultdict


def bfs(start_v):
    visited = set()
    pq = []
    for v, weight in graph[start_v]:
        heapq.heappush(pq, (weight, v))
        visited.add(v)

    while pq:
        weight, v = heapq.heappop(pq)
        if v == start_v:
            return weight
        for next_v, add_w in graph[v]:
            if next_v in visited:
                continue
            heapq.heappush(pq, (weight + add_w, next_v))
    return None


V, E = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
has_in = set()

for road in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start - 1].append((end - 1, weight))
    has_in.add(end)

result = float('inf')
for v in has_in:
    tmp = bfs(v)
    if tmp is not None:
        result = min(result, tmp)

if result == float('inf'):
    print(-1)
else:
    print(result)
