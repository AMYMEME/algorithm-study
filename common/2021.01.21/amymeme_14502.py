# https://www.acmicpc.net/problem/14502
# 백준 14502

import copy
import sys
from collections import deque
from itertools import combinations


def safe_scope_size(after_wall_lab):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(N):
        for j in range(M):
            if after_wall_lab[i][j] == 2:
                q = deque()
                q.append((i, j))
                while q:
                    row_idx, col_idx = q.popleft()
                    for d in range(4):
                        next_row_idx, next_col_idx = row_idx + dx[d], col_idx + dy[d]
                        if -1 < next_row_idx < N and -1 < next_col_idx < M:
                            if after_wall_lab[next_row_idx][next_col_idx] == 0:
                                q.append((next_row_idx, next_col_idx))
                                after_wall_lab[next_row_idx][next_col_idx] = 2
    return sum(row.count(0) for row in after_wall_lab)


N, M = map(int, sys.stdin.readline().split())
lab = []
walls = []
result = []

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    lab.append(line)
    for j, value in enumerate(line):
        if value == 0:
            walls.append((i, j))

for case in combinations(walls, 3):
    after_wall_lab = copy.deepcopy(lab)
    for predict_wall_row_idx, predict_wall_col_idx in case:
        after_wall_lab[predict_wall_row_idx][predict_wall_col_idx] = 1
    result.append(safe_scope_size(after_wall_lab))

print(max(result))
