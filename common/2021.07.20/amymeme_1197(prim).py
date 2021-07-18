# https://www.acmicpc.net/problem/1197
# 최소 스패닝 트리


import sys
from collections import defaultdict
import heapq


def prim(start, v_count):
    answer = 0
    pq = []
    final = {start}
    for v, w in graph[start]:
        heapq.heappush(pq, (w, v))

    while len(final) != v_count:
        weight, cur_v = heapq.heappop(pq)
        if cur_v in final:
            continue
        final.add(cur_v)
        answer += weight
        for nxt_v, w in graph[cur_v]:
            heapq.heappush(pq, (w, nxt_v))
    return answer


graph = defaultdict(list)
V, E = map(int, sys.stdin.readline().split())

for i in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

print(prim(1, V))
