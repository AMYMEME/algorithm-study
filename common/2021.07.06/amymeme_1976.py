# https://www.acmicpc.net/problem/1976
# 여행 가자
from collections import deque, defaultdict
import sys


def bfs(v):
    q = deque([v])
    visited = {v}

    while q:
        v = q.popleft()
        for next_v in graph[v]:
            if next_v in visited:
                continue
            q.append(next_v)
            visited.add(next_v)
    return visited


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = defaultdict(set)
for start in range(N):
    row = map(int, sys.stdin.readline().split())
    for end, value in enumerate(row):
        if value:
            graph[start].add(end)

want_cities = deque(map(lambda x: int(x) - 1, sys.stdin.readline().split()))

connected = defaultdict(set)

bfs_checked = set()
while want_cities:
    cur_city = want_cities.popleft()
    if not want_cities:
        break
    if cur_city not in bfs_checked:
        connected[cur_city] = bfs(cur_city)
    if not want_cities[0] in connected[cur_city]:
        print('NO')
        exit(0)
print('YES')
