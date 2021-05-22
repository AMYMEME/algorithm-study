"""
https://www.acmicpc.net/problem/13913
"""
import sys
from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = -1
    worse=(2*K-N)
    while q:
        vx = q.popleft()
        for m in [-1, 1, vx]:
            nx = vx + m
            # +1 씩 증가해서 가는 경우 가장 오래 걸림 (2*를 하는 경우 이 경우보다 빠르게)
            # ex) 0에서 시작하고 2*k 이상으로가면 출발점에서 +1 씩해서 가는 것보다 더 오래걸림-> 고려할 필요 x
            if nx not in visited.keys() and 0 <= nx <= worse:
                visited[nx] = vx
                q.append(nx)
            if nx == K:
                start = visited[nx]
                ans = deque()
                ans.append(nx)
                while start != -1:
                    ans.appendleft(start)
                    start = visited[start]
                print(len(ans) - 1)
                print(*ans)
                return


N, K = map(int, sys.stdin.readline().split())
visited = dict()

if N > K:
    print(N - K)
    for i in range(N, K - 1, -1):
        print(i, end=' ')
else:
    bfs(N)
