# https://www.acmicpc.net/problem/4485
import sys
import heapq

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def game():
    q = [(board[0][0], 0, 0)]
    visited = set()
    visited.add((0, 0))
    while q:
        cost, x, y = heapq.heappop(q)
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if -1 < nx < N and -1 < ny < N and (nx, ny) not in visited:
                visited.add((nx, ny))
                total = cost + board[nx][ny]
                heapq.heappush(q, (total, nx, ny))
                if nx == N - 1 and ny == N - 1:
                    return total


tc = 1
while True:
    N = int(sys.stdin.readline())
    if not N:
        break
    board = []
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    print("Problem {0}: {1}".format(tc, game()))
    tc += 1
