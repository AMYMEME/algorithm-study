# https://programmers.co.kr/learn/courses/30/lessons/42861

from collections import deque

parent = []


def find_parent(v1):
    global parent
    if parent[v1] != v1:
        return find_parent(parent[v1])
    return parent[v1]


def union(v1, v2):
    global parent
    v1_parent = find_parent(v1)
    v2_parent = find_parent(v2)
    if v1_parent < v2_parent:
        parent[v2_parent] = v1_parent
    else:
        parent[v1_parent] = v2_parent


def kruskal(n, distances):
    cnt = 0
    answer = 0
    while cnt < n - 1:
        for i in range(len(distances)):
            distance, v1, v2 = distances[i]
            if find_parent(v1) == find_parent(v2):
                continue
            # not cycle
            union(v1, v2)
            distances.pop(i)
            answer += distance
            cnt += 1
            break
    return answer


def solution(n, costs):
    global parent
    for i in range(n):
        # initial parent
        parent.append(i)
    distances = deque([])
    for cost in costs:
        v1, v2, weight = cost
        distances.append((weight, v1, v2))

    return kruskal(n, sorted(distances))
