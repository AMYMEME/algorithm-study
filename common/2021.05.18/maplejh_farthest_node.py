'''
https://programmers.co.kr/learn/courses/30/lessons/49189
'''
from collections import deque, defaultdict


def solution(n, edge):
    distance = [10e9] * (n + 1)
    distance[0] = 0
    distance[1] = 0

    # 그래프를 [[0]*n for _ in range(n)] 으로하면 시간초과
    graph = defaultdict(list)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    q = deque()
    q.append(1)
    while q:
        nx = q.popleft()
        for g in graph[nx]:
            if distance[nx] + 1 < distance[g]:
                distance[g] = distance[nx] + 1
                q.append(g)

    distance.sort(reverse=True)
    answer = distance.count(distance[0])

    return answer
