# https://www.acmicpc.net/problem/4179
# 불!

import sys


def start(fires, jihun):
    time = 0
    while jihun:
        time += 1
        tmp_fires = []
        for fi, fj in fires:
            for di, dj in diff:
                ni = fi + di
                nj = fj + dj
                if -1 < ni < R and -1 < nj < C and board[ni][nj] != '#' and board[ni][nj] != 'F':
                    tmp_fires.append((ni, nj))
                    board[ni][nj] = 'F'
        fires = tmp_fires
        tmp_jihun = []
        for ji, jj in jihun:
            for di, dj in diff:
                ni = ji + di
                nj = jj + dj
                if -1 < ni < R and -1 < nj < C:
                    if board[ni][nj] == '.':
                        tmp_jihun.append((ni, nj))
                        board[ni][nj] = str(time)
                else:
                    return time
        jihun = tmp_jihun
    return "IMPOSSIBLE"


R, C = map(int, sys.stdin.readline().split())
diff = [(0, -1), (0, 1), (-1, 0), (1, 0)]

fires = []
jihun = []

board = []
for i in range(R):
    row = list(sys.stdin.readline().strip())
    board.append(row)
    for j, value in enumerate(row):
        if value == 'J':
            jihun.append((i, j))
        elif value == 'F':
            fires.append((i, j))

print(start(fires, jihun))
