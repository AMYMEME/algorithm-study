# https://www.acmicpc.net/problem/2252
import sys
from collections import deque, defaultdict

N, M = map(int, sys.stdin.readline().split())
indegree = [0] * (N + 1)
order = defaultdict(list)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    order[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, N + 1):
    if not indegree[i]:
        q.append(i)

answer = []
while q:
    pre_node = q.popleft()
    answer.append(pre_node)
    for post_node in order[pre_node]:
        indegree[post_node] -= 1
        if not indegree[post_node]:
            q.append(post_node)
print(*answer)
