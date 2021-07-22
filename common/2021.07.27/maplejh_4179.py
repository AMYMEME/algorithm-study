# https://www.acmicpc.net/problem/4179
import sys
from collections import deque

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def bfs():
    cnt = 1
    while jq:
        fire = len(fq)
        for _ in range(fire):
            fx, fy = fq.popleft()
            for dx, dy in d:
                nx = fx + dx
                ny = fy + dy
                if -1 < nx < R and -1 < ny < C:
                    if board[nx][ny] != '#' and board[nx][ny] != 'F':
                        board[nx][ny] = 'F'
                        fq.append((nx, ny))
        jh = len(jq)
        for _ in range(jh):
            jx, jy = jq.popleft()
            for dx, dy in d:
                nx = jx + dx
                ny = jy + dy
                if -1 < nx < R and -1 < ny < C:
                    if board[nx][ny] == '.':
                        board[nx][ny] = 'J'
                        jq.append((nx, ny))
                else:
                    return cnt
        cnt += 1
    return "IMPOSSIBLE"


R, C = map(int, sys.stdin.readline().split())
board = []
jq = deque()
fq = deque()
for i in range(R):
    board.append(list(sys.stdin.readline().strip()))
    for j, b in enumerate(board[i]):
        if b == 'J':
            jq.append((i, j))
        elif b == 'F':
            fq.append((i, j))

print(bfs())
