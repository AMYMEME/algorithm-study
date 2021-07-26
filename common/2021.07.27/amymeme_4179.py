# https://www.acmicpc.net/problem/4179
# 불!

import sys
from collections import deque, defaultdict


def bfs(init_set):
    visited = set()
    possibles = defaultdict(int)
    for i, j, _ in init_set:
        visited.add((i, j))
        if 0 < i < R - 1:
            if j == 0 or j == C - 1:
                possibles[(i, j)] = 0
        else:
            possibles[(i, j)] = 0

    q = deque(init_set)
    while q:
        ci, cj, time = q.popleft()
        for di, dj in diff:
            ni = ci + di
            nj = cj + dj
            if ni < 0 or ni > R - 1 or nj < 0 or nj > C - 1:
                continue
            if board[ni][nj] == '#' or (ni, nj) in visited:
                continue
            if 0 < ni < R - 1:
                if nj == 0 or nj == C - 1:
                    possibles[(ni, nj)] = time + 1
            else:
                possibles[(ni, nj)] = time + 1
            visited.add((ni, nj))
            q.append((ni, nj, time + 1))
    return possibles


R, C = map(int, sys.stdin.readline().split())
diff = [(0, -1), (0, 1), (-1, 0), (1, 0)]
fires = set()
jihun = set()

board = []
for i in range(R):
    row = sys.stdin.readline().strip()
    board.append(row)
    for j, value in enumerate(row):
        if value == 'J':
            jihun.add((i, j, 0))
        elif value == 'F':
            fires.add((i, j, 0))

jihun_possibles = bfs(jihun)
fire_possibles = bfs(fires)
for (i, j), time in sorted(jihun_possibles.items(), key=lambda x: x[1]):
    if (i, j) not in fire_possibles.keys() or fire_possibles[(i, j)] > time:
        print(time + 1)
        exit(0)
print("IMPOSSIBLE")

'''
5 5
#####
#...#
#.JF#
#...#
#####
'''