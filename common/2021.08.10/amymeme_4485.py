# https://www.acmicpc.net/problem/4485
# 녹색 옷 입은 애가 젤다지?

import sys
import heapq

diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def start(n):
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    distance = [[float('inf')] * n for _ in range(n)]

    distance[0][0] = board[0][0]  # init board[0][0] not 0
    visited = {(0, 0)}

    pq = [(board[0][0], 0, 0)]
    while pq:
        value, ci, cj = heapq.heappop(pq)
        if ci == n - 1 and cj == n - 1:
            return value
        for di, dj in diff:
            ni = ci + di
            nj = cj + dj
            if -1 < ni < n and -1 < nj < n and (ni, nj) not in visited:
                distance[ni][nj] = min(distance[ni][nj], value + board[ni][nj])
                heapq.heappush(pq, (distance[ni][nj], ni, nj))
                visited.add((ni, nj))


count = 0
while True:
    count += 1
    N = int(sys.stdin.readline())
    if N:
        print("Problem {0}: {1}".format(count, start(N)))
    else:
        break
