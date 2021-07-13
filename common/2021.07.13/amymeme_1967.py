# https://www.acmicpc.net/problem/1967
# 트리의 지름

from collections import defaultdict, deque
import sys


def bfs(start_leaf):
    q = deque([(start_leaf, 0)])
    visited = {start_leaf: 0}
    while q:
        cur_node, cur_w = q.popleft()
        for nxt_node, nxt_w in graph[cur_node]:
            if nxt_node in visited.keys():
                continue
            visited[nxt_node] = nxt_w + cur_w
            q.append((nxt_node, nxt_w + cur_w))
    return sorted(visited.items(), key=lambda x: x[1], reverse=True)[0]


n = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(n - 1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    graph[child].append((parent, weight))
    graph[parent].append((child, weight))

start_leaf = bfs(1)[0]

print(bfs(start_leaf)[1])
