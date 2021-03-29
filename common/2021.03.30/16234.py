# https://www.acmicpc.net/problem/16234
# 백준 16234 - 인구 이동

import sys
from collections import deque, defaultdict


def dfs(i, j, flag):
    global visited, count_dict
    q = deque([(i, j)])
    visited[i][j] = flag
    count_dict[flag].add((i, j))
    while q:
        ci, cj = q.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni = ci + di
            nj = cj + dj
            if -1 < ni < N and -1 < nj < N and not visited[ni][nj]:
                if L <= abs(board[ci][cj] - board[ni][nj]) <= R:
                    dfs(ni, nj, flag)


def population_move():
    global visited, count_dict
    visited = [[0] * N for _ in range(N)]
    count_dict = defaultdict(set)
    flag = 1
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, flag)
                flag += 1
    if flag == N * N + 1:
        return False
    population_calculate()
    return True


def population_calculate():
    global board
    for key in count_dict.keys():
        total_population = 0
        country_count = len(count_dict[key])
        for i, j in count_dict[key]:
            total_population += board[i][j]
        result_value = total_population // country_count
        for i, j in count_dict[key]:
            board[i][j] = result_value


sys.setrecursionlimit(10**6)
N, L, R = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = list()
count_dict = defaultdict(set)
move_count = 0

while True:
    restart = population_move()
    if not restart:
        break
    move_count += 1
print(move_count)
