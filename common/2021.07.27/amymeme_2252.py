# https://www.acmicpc.net/problem/2252
# 줄 세우기

import sys
from collections import defaultdict, deque

N, M = map(int, sys.stdin.readline().split())

graph = defaultdict(set)
in_count = defaultdict(int)

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    # A가 B보다 작음: A -> B
    graph[A].add(B)
    in_count[B] += 1

leaves = deque(filter(lambda x: x not in in_count.keys(), [x for x in range(1, N + 1)]))

result = []
while leaves:
    leaf = leaves.popleft()
    result.append(leaf)
    for adj in graph[leaf]:
        in_count[adj] -= 1
        if in_count[adj] == 0:
            leaves.append(adj)

print(*result, sep=' ')
