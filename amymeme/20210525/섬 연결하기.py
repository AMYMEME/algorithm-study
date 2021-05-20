import heapq
from collections import defaultdict


def prim(n, graph, start=0):
    distances = dict()
    distances[start] = 0
    visited = {start}
    while len(visited) < n:
        pq = []
        for v in visited:
            for adj_v, weight in graph[v]:
                if adj_v in visited:
                    continue
                heapq.heappush(pq, (weight, adj_v))
        distance, next_visit = heapq.heappop(pq)
        distances[next_visit] = distance
        visited.add(next_visit)
    return distances


def solution(n, costs):
    graph = defaultdict(list)
    for cost in costs:
        v1, v2, weight = cost
        graph[v1].append((v2, weight))
        graph[v2].append((v1, weight))
    distances = prim(n, graph)
    return sum(distances.values())
