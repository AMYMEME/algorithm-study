# https://www.acmicpc.net/problem/1697
# 백준 1697 - 숨바꼭질

import sys
from collections import deque

MAX = 100001
diff = [-1, 1]
N, K = map(int, sys.stdin.readline().split())
q = deque([(N, 0)])
visited = {N}

while q:
    current, time = q.popleft()
    if current == K:
        print(time)
        break

    for d in diff:
        _next = current + d
        if -1 < _next < MAX and _next not in visited:
            q.append((_next, time + 1))
            visited.add(_next)

    teleport = current * 2
    if -1 < teleport < MAX and teleport not in visited:
        q.append((teleport, time + 1))
        visited.add(teleport)
