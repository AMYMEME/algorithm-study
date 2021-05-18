# https://programmers.co.kr/learn/courses/30/lessons/72413

from collections import defaultdict, deque


def bfs(graph, start):
    distance = defaultdict(int)
    distance[start] = 0
    q = deque([(start, 0)])
    while q:
        cur_node, cur_weight = q.popleft()
        for next_node, weight in graph[cur_node]:
            if next_node == start:
                continue
            if not distance[next_node] or distance[next_node] > cur_weight + weight:
                q.append((next_node, cur_weight + weight))
                distance[next_node] = cur_weight + weight
    return distance


def solution(n, s, a, b, fares):
    answer = 0
    graph = defaultdict(list)

    for v1, v2, weight in fares:
        graph[v1].append((v2, weight))
        graph[v2].append((v1, weight))

    shared_fares = bfs(graph, s)
    only_a_fares = bfs(graph, a)
    only_b_fares = bfs(graph, b)

    for i in range(1, n + 1):
        if i not in shared_fares.keys():
            continue
        if answer:
            answer = min(answer, shared_fares[i] + only_a_fares[i] + only_b_fares[i])
        else:
            answer = shared_fares[i] + only_a_fares[i] + only_b_fares[i]
    return answer
