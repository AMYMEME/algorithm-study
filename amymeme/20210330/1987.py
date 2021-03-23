# https://www.acmicpc.net/problem/1987
# 백준 1987 - 알파벳

import sys


def dfs(i, j, cnt, _visited):
    global max_cnt
    for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        ni = di + i
        nj = dj + j
        if -1 < ni < R and -1 < nj < C and not _visited[ord(board[ni][nj]) - 65]:
            _visited[ord(board[ni][nj]) - 65] = True
            dfs(ni, nj, cnt + 1, _visited)
            _visited[ord(board[ni][nj]) - 65] = False  # back-tracking
    if max_cnt < cnt:
        max_cnt = cnt


R, C = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(R)]
visited = [False] * 26
visited[ord(board[0][0]) - 65] = True
max_cnt = 1
dfs(0, 0, 1, visited)
print(max_cnt)
