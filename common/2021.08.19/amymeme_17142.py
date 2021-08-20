# https://www.acmicpc.net/problem/17142
# 연구소 3

import sys
from collections import deque
from itertools import combinations


def start(com, answer):
    count = len(empty)
    visited = set()
    for i, j, _ in com:
        visited.add((i, j))

    _virus = deque(com)
    while _virus:
        ci, cj, time = _virus.popleft()
        if time >= answer:
            break
        for di, dj in diff:
            ni = ci + di
            nj = cj + dj
            if -1 < ni < N and -1 < nj < N:
                if (ni, nj) in wall or (ni, nj) in visited:
                    continue
                _virus.append((ni, nj, time + 1))
                visited.add((ni, nj))
                if (ni, nj) in empty:
                    count -= 1
                    if count == 0:
                        return time + 1
    return answer


MAX = float('inf')
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N, M = map(int, sys.stdin.readline().split())
virus = set()
empty = set()
wall = set()

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j, value in enumerate(row):
        if value == 0:
            empty.add((i, j))
        elif value == 1:
            wall.add((i, j))
        elif value == 2:
            virus.add((i, j, 0))

answer = MAX
if not empty:
    answer = 0
else:
    for c in combinations(virus, M):
        answer = start(c, answer)
    if answer == MAX: answer = -1

print(answer)
