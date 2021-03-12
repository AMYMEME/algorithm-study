# https://www.acmicpc.net/problem/1916
# 백준 1916 - 최소비용 구하기
# 참고: https://github.com/TheAlgorithms/Python/blob/master/graphs/dijkstra.py

import heapq
import sys
from collections import defaultdict


def dijkstra(_graph, _start, _end):
    pq = [(0, start)]  # weight, end
    visited = set()
    while pq:
        current_weight, current_end = heapq.heappop(pq)
        if current_end in visited:
            continue
        if current_end == _end:
            return current_weight
        visited.add(current_end)
        for next_u, next_weight in _graph[current_end]:
            if next_u in visited:
                continue
            heapq.heappush(pq, (current_weight + next_weight, next_u))


_ = int(sys.stdin.readline())  # cities
M = int(sys.stdin.readline())  # buses
graph = defaultdict(list)

for _ in range(M):
    start_node, end_node, weight = map(int, sys.stdin.readline().split())
    graph[start_node].append((end_node, weight))
start, end = map(int, sys.stdin.readline().split())
print(dijkstra(graph, start, end))
