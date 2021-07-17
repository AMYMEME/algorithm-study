# https://www.acmicpc.net/problem/1504
import sys
from collections import defaultdict
import heapq


def cal(start):
    q = [(0, start)]
    visited = [INF] * (N + 1)
    visited[start] = 0
    while q:
        now_cost, now_node = heapq.heappop(q)
        for next_cost, next_node in board[now_node]:
            total = now_cost + next_cost
            if total < visited[next_node]:
                visited[next_node] = total
                heapq.heappush(q, (total, next_node))
    return visited


INF = 10e9
N, E = map(int, sys.stdin.readline().split())
board = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    board[a].append((c, b))
    board[b].append((c, a))
one, two = map(int, sys.stdin.readline().split())

# 1->one->two->N / 1->two->one->N
d = [cal(i) for i in [1, one, two]]
answer = min(d[0][one] + d[1][two] + d[2][N], d[0][two] + d[1][N] + d[2][one])
print(answer if answer < INF else -1)
