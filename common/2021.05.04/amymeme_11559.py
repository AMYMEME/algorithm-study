# https://www.acmicpc.net/problem/11559
# 백준 11559 - Puyo Puyo

import sys
from collections import deque


def fall_down():
    global board
    trans_board = zip(*board)
    fall_right = []
    for row in trans_board:
        tmp = list(filter(lambda x: x != 'e', row))
        if len(tmp) != 12:
            tmp = ['.'] * (12 - len(tmp)) + tmp
        fall_right.append(tmp)
    board = list(map(list, zip(*fall_right)))


def bfs():
    global board
    flag = False
    visited = set()

    for i in range(12):
        for j in range(6):
            if board[i][j] == '.':
                continue
            if (i, j) in visited:
                continue
            color = board[i][j]
            q = deque([(i, j)])
            visited.add((i, j))
            save = {(i, j)}
            while q:
                ci, cj = q.popleft()
                for di, dj in diff:
                    ni = ci + di
                    nj = cj + dj
                    if -1 < ni < 12 and -1 < nj < 6:
                        if (ni, nj) in visited:
                            continue
                        if board[ni][nj] == color:
                            q.append((ni, nj))
                            visited.add((ni, nj))
                            save.add((ni, nj))
            if len(save) >= 4:
                for _i, _j in save:
                    board[_i][_j] = 'e'
                flag = True
    return flag


board = [list(sys.stdin.readline().strip()) for _ in range(12)]
diff = [(0, -1), (0, 1), (-1, 0), (1, 0)]
total_cnt = 0
while True:
    flag = bfs()
    if not flag:
        break
    total_cnt += 1
    fall_down()
print(total_cnt)
