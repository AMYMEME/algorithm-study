# https://programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque, defaultdict


def start(graph):
    q = deque([(1, 0)])  # vertex, distance
    visited = {1}
    distance_dict = defaultdict(list)
    while q:
        cur_v, cur_distance = q.popleft()
        for next_v in graph[cur_v]:
            if next_v in visited:
                continue
            q.append((next_v, cur_distance + 1))
            visited.add(next_v)
            distance_dict[cur_distance + 1].append(next_v)
    max_distance = sorted(distance_dict.keys())[-1]
    return distance_dict[max_distance]


def solution(n, vertex):
    graph = defaultdict(list)
    for v1, v2 in vertex:
        graph[v1].append(v2)
        graph[v2].append(v1)

    return len(start(graph))
