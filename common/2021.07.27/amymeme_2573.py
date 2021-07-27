# https://www.acmicpc.net/problem/2573
# 빙산

import sys
from collections import deque, defaultdict


def bfs(ice):
    k = next(iter(ice))  # get one key
    q = deque([k])
    visited = {k}

    while q:
        i, j = q.popleft()
        for di, dj in diff:
            if board[i + di][j + dj] and (i + di, j + dj) not in visited:
                q.append((i + di, j + dj))
                visited.add((i + di, j + dj))

    if len(visited) == len(ice):
        return True
    return False


N, M = map(int, sys.stdin.readline().split())
board = []
diff = [(0, 1), (0, -1), (-1, 0), (1, 0)]
ice = defaultdict(int)
time = 0

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
    for j, value in enumerate(row):
        if value:
            ice[(i, j)] = value

while True:
    if not ice:
        time = 0
        break
    if not bfs(ice):
        break
    time += 1
    melted = set()
    for (i, j), value in ice.items():
        count = 0
        for di, dj in diff:
            if board[i + di][j + dj] == 0:
                count += 1
        if count >= value:
            melted.add((i, j))
        else:
            ice[(i, j)] -= count
    for i, j in melted:
        del ice[(i, j)]
        board[i][j] = 0
    for (i, j), value in ice.items():
        board[i][j] = value
print(time)
