# https://www.acmicpc.net/problem/1967
import sys
from collections import defaultdict, deque


def bfs(start):
    distance = defaultdict(int)
    distance[start] = 0
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        for child, cost in tree[node]:
            if child not in distance.keys():
                q.append(child)
                distance[child] = cost + distance[node]
    return sorted(distance.items(), reverse=True, key=lambda x: x[1])[0]


n = int(sys.stdin.readline())
tree = defaultdict(list)
for _ in range(n - 1):
    parent, children, value = map(int, sys.stdin.readline().split())
    tree[parent].append((children, value))
    tree[children].append((parent, value))

print(bfs(bfs(1)[0])[1])
