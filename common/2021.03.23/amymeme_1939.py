# https://www.acmicpc.net/problem/1939
# 백준 1939 - 중량제한

import heapq
import sys
from collections import defaultdict


def solution(start, end):
    pq = []  # weight, end_node
    visited = set()
    for aux, weight in bridges[start].items():
        heapq.heappush(pq, (-weight, aux))
        visited.add(start)
    while pq:
        weight, aux = heapq.heappop(pq)
        if aux == end:
            return -weight
        if aux not in visited:
            for next_aux, next_weight in bridges[aux].items():
                if next_weight < -weight:
                    heapq.heappush(pq, (-next_weight, next_aux))
                else:
                    heapq.heappush(pq, (weight, next_aux))
                visited.add(aux)


N, M = map(int, sys.stdin.readline().split())
bridges = defaultdict(dict)

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    if B in bridges[A].keys():
        if bridges[A][B] < C:
            bridges[A][B] = C
    else:
        bridges[A][B] = C
    if A in bridges[B].keys():
        if bridges[B][A] < C:
            bridges[B][A] = C
    else:
        bridges[B][A] = C

start, end = map(int, sys.stdin.readline().split())
print(solution(start, end))
