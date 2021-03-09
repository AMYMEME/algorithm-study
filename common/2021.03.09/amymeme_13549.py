# https://www.acmicpc.net/problem/13549
# 백준 13549 - 숨바꼭질 3

import heapq
import sys

MAX = 100001
diff = [-1, 1]
N, K = map(int, sys.stdin.readline().split())
q = []
heapq.heappush(q, (0, N))
visited = {N}

while q:
    time, current = heapq.heappop(q)
    if current == K:
        print(time)
        break

    teleport = current * 2
    if -1 < teleport < MAX and teleport not in visited:
        heapq.heappush(q, (time, teleport))
        visited.add(teleport)

    for d in diff:
        _next = current + d
        if -1 < _next < MAX and _next not in visited:
            heapq.heappush(q, (time + 1, _next))
            visited.add(_next)
    """"
    teleport를 먼저 heapq에 집어넣어야 한다. 
    어차피 heapq니까 우선순위 큐로 자동 정렬된다고 생각하고 _next부터 넣었더니 
    반례가 생겼다.
    반례 : 1 32
    답 : 0
    리턴값 : 1
    """
