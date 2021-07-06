# https://programmers.co.kr/learn/courses/30/lessons/76503
# 모두 0으로 만들기

from collections import defaultdict, deque


def solution(a, edges):
    answer = 0
    graph = defaultdict(set)

    for v1, v2 in edges:
        graph[v1].add(v2)
        graph[v2].add(v1)

    leaves = deque(filter(lambda x: len(graph[x]) == 1, graph.keys()))
    while leaves:
        leaf = leaves.popleft()
        if not graph[leaf]:
            continue
        connect = graph[leaf].pop()
        if len(graph[connect]) == 2:
            leaves.append(connect)
        graph[connect].remove(leaf)
        a[connect] += a[leaf]
        answer += abs(a[leaf])
        a[leaf] = 0

    return answer if not any(a) else -1
