# https://programmers.co.kr/learn/courses/30/lessons/43162
from collections import defaultdict, deque

visited = set()


def bfs(start, graph):
    global visited
    visited.add(start)
    q = deque([start])
    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if next_node in visited:
                continue
            q.append(next_node)
            visited.add(next_node)


def solution(n, computers):
    answer = 0
    graph = defaultdict(set)

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                graph[i].add(j)
                graph[j].add(i)

    for i in range(n):
        if i in visited:
            continue
        bfs(i, graph)
        answer += 1
    return answer
