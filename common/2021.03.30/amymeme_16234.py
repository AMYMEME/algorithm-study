# https://www.acmicpc.net/problem/16234
# 백준 16234 - 인구 이동

import sys
from collections import deque


def bfs(i, j):
    q = deque([(i, j)])
    visited = {(i, j)}
    board_check[i][j] = True
    population = board[i][j]
    while q:
        ci, cj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            ni = di + ci
            nj = dj + cj
            if -1 < ni < N and -1 < nj < N and not board_check[ni][nj] and (ni, nj) not in visited:
                if L <= abs(board[ni][nj] - board[ci][cj]) <= R:
                    q.append((ni, nj))
                    board_check[ni][nj] = True
                    visited.add((ni, nj))
                    population += board[ni][nj]
    return visited, population // len(visited)


N, L, R = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
board_check = [[False] * N for _ in range(N)]
move_count = 0
while True:
    continue_flag = False
    board_check = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board_check[i][j]:
                continue
            visited, next_population = bfs(i, j)
            if len(visited) == 1:
                continue
            continue_flag = True
            for move_i, move_j in visited:
                board[move_i][move_j] = next_population
    if continue_flag:
        move_count += 1
        continue
    break
print(move_count)
