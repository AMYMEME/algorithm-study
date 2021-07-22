# # https://www.acmicpc.net/problem/1197
import sys
from collections import defaultdict
import heapq

V, E = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges[A].append((C, B))
    edges[B].append((C, A))

q = [(0, 1)]
cost = 0
visited = set()
while q:
    if len(visited) == V:
        break
    c, n = heapq.heappop(q)
    if n not in visited:
        cost += c
        visited.add(n)
        for i in edges[n]:
            heapq.heappush(q, i)

print(cost)
