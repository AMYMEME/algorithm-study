# https://www.acmicpc.net/problem/17142
from collections import deque
import itertools
import sys

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, M = map(int, sys.stdin.readline().split())
board = []
virus = []
zeros = 0
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j, b in enumerate(board[i]):
        if b == 2:
            virus.append((0, i, j))
            board[i][j] = 2
    zeros += board[i].count(0)

ans = sys.maxsize
for c in list(itertools.combinations(virus, M)):
    q = deque(c)
    cnt = zeros  # len(visited) == zeros 로 비교하면 시간초과
    visited = set()
    activated = set(map(lambda k: (k[1], k[2]), c))
    while q:
        t, x, y = q.popleft()
        if t >= ans:
            break
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not board[nx][ny] and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((t + 1, nx, ny))
                    cnt -= 1
                elif board[nx][ny] == 2 and (nx, ny) not in activated and cnt:  # 비활성화된 바이러스인 경우
                    q.append((t + 1, nx, ny))
                    activated.add((nx, ny))
    if not cnt:
        ans = t
print(ans if ans != sys.maxsize else -1)
