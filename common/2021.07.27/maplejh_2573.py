# https://www.acmicpc.net/problem/2573
import sys
from collections import deque
from itertools import chain

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def bfs(start): # 빙산 녹이기
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)
    while q:
        x, y = q.popleft()
        cnt = 0
        for dx, dy in d:
            nx = dx + x
            ny = dy + y
            if (nx, ny) not in visited:
                if not board[nx][ny]:
                    cnt += 1
                    continue
                visited.add((nx, ny))
                q.append((nx, ny))
        board[x][y] -= cnt
        if board[x][y] < 0:
            board[x][y] = 0
    return len(visited)


N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

year = 0
while True:
    # 빙산이 처음 나오는 곳 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                find = (i, j)
                break
    ice = N * M - list(chain(*board)).count(0)
    if not ice:  # 빙산이 다 녹은 경우
        year = 0
        break
    if bfs(find) != ice:  # 빙산이 분리되는 경우
        break
    year += 1
print(year)
