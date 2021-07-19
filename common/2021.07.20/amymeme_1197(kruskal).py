# https://www.acmicpc.net/problem/1197
# 최소 스패닝 트리

import sys
import heapq


def find(n):
    if parents[n] != n:
        return find(parents[n])
    return parents[n]


def union(n1, n2):
    global parents
    p1 = find(n1)
    p2 = find(n2)
    if p1 < p2:
        parents[p2] = p1
    else:
        parents[p1] = p2


def kruskal(v_count):
    global graph
    final = 0
    answer = 0

    while final < v_count - 1:
        w, n1, n2 = heapq.heappop(graph)
        if find(n1) == find(n2):
            continue
        union(n1, n2)
        final += 1
        answer += w
    return answer


sys.setrecursionlimit(10000)
V, E = map(int, sys.stdin.readline().split())
graph = []
parents = [x for x in range(V + 1)]

for _ in range(E):
    A, B, weight = map(int, sys.stdin.readline().split())
    heapq.heappush(graph, (weight, A, B))

print(kruskal(V))
