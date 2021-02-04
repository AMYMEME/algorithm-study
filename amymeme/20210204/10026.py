# https://www.acmicpc.net/problem/10026
# 백준 10026 - 적록 색약
import sys
from collections import deque


def normal_bfs(ci, cj, color):
    q = deque([(ci, cj)])
    while q:
        i, j = q.popleft()
        for di, dj in diff:
            ni, nj = i + di, j + dj
            if -1 < ni < N and -1 < nj < N and (ni, nj) not in normal_visited:
                if painting[ni][nj] == color:
                    q.append((ni, nj))
                    normal_visited.add((ni, nj))


def color_weakness_bfs(ci, cj, color):
    q = deque([(ci, cj)])
    while q:
        i, j = q.popleft()
        for di, dj in diff:
            ni, nj = i + di, j + dj
            if -1 < ni < N and -1 < nj < N and (ni, nj) not in color_weakness_visited:
                if color == 'B':
                    if painting[ni][nj] == 'B':
                        q.append((ni, nj))
                        color_weakness_visited.add((ni, nj))
                else:
                    if painting[ni][nj] != 'B':
                        q.append((ni, nj))
                        color_weakness_visited.add((ni, nj))


diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N = int(sys.stdin.readline())
painting = [list(sys.stdin.readline().strip()) for _ in range(N)]
normal_visited, color_weakness_visited = set(), set()
normal_result, color_weakness_result = 0, 0

for i in range(N):
    for j in range(N):
        if (i, j) not in normal_visited:
            normal_bfs(i, j, painting[i][j])
            normal_result += 1
        if (i, j) not in color_weakness_visited:
            color_weakness_bfs(i, j, painting[i][j])
            color_weakness_result += 1

print("{0} {1}".format(normal_result, color_weakness_result))
