# acmicpc.net/problem/2667

import sys
from collections import deque


def bfs(row_idx, col_idx):
    count = 0
    q = deque()
    q.append((row_idx, col_idx))
    visit.add((row_idx, col_idx))
    while q:
        row_idx, col_idx = q.popleft()
        count += 1
        for d in range(4):
            next_row_idx, next_col_idx = row_idx + dx[d], col_idx + dy[d]
            if -1 < next_row_idx < N and -1 < next_col_idx < N:
                if house_map[next_row_idx][next_col_idx] == 1 and (next_row_idx, next_col_idx) not in visit:
                    q.append((next_row_idx, next_col_idx))
                    visit.add((next_row_idx, next_col_idx))
    return count


N = int(sys.stdin.readline().strip())

house_map = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visit = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for i in range(N):
    for j in range(N):
        if house_map[i][j] == 1 and (i, j) not in visit:
            result.append(bfs(i, j))
result.sort()
print(len(result))
for i in result:
    print(i)
