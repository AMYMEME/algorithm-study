# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

import sys
from collections import defaultdict
import heapq


def dijkstra(start, to):
    # 모든 정점까지의 거리 배열을 구하지 않고 to까지만 구함
    pq = [(0, start)]  # weight from start, v
    visited = set()

    while pq:
        cur_w, cur_v = heapq.heappop(pq)
        if cur_v in visited:
            continue
        visited.add(cur_v)
        if cur_v == to:
            return cur_w
        for nxt_w, nxt_v in graph[cur_v]:
            if nxt_v in visited:
                continue
            heapq.heappush(pq, (cur_w + nxt_w, nxt_v))
    return -1


def solution(start, aux1, aux2, dest):
    answer = 0
    distance = dijkstra(start, aux1)
    if distance == -1:
        return -1
    answer += distance
    distance = dijkstra(aux1, aux2)
    if distance == -1:
        return -1
    answer += distance
    distance = dijkstra(aux2, dest)
    if distance == -1:
        return -1
    answer += distance
    return answer


graph = defaultdict(set)
N, E = map(int, sys.stdin.readline().split())

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].add((c, b))  # v, weight
    graph[b].add((c, a))

v1, v2 = map(int, sys.stdin.readline().split())
print(min(solution(1, v1, v2, N), solution(1, v2, v1, N)))
