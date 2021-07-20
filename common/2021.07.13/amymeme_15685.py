# https://www.acmicpc.net/problem/15685
# 드래곤 커브

import sys

N = int(sys.stdin.readline())
board = [[0] * 101 for _ in range(101)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    cur_gen_directs = [d]
    all_gen_directs = [d]
    board[x][y] = 1
    for _ in range(g + 1):
        for j in cur_gen_directs:
            x += dx[j]
            y += dy[j]
            board[x][y] = 1
        cur_gen_directs = [(i + 1) % 4 for i in all_gen_directs]
        cur_gen_directs.reverse()
        all_gen_directs += cur_gen_directs
result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j] == 1 and board[i + 1][j + 1] == 1:
            result += 1
print(result)
