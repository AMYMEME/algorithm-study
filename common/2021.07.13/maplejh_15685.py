# https://www.acmicpc.net/problem/15685
import sys

# (y,x)
direction = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
board = [[0] * 101 for _ in range(101)]

N = int(sys.stdin.readline())
for _ in range(N):
    x, y, d, g = map(int, sys.stdin.readline().split())
    move = [d]
    # 0 세대
    board[y][x] = 1
    x += direction[d][1]
    y += direction[d][0]
    board[y][x] = 1
    for _ in range(g):  # 1 ~ n 세대
        temp = []
        for m in move[::-1]:
            m = (m + 1) % 4
            x += direction[m][1]
            y += direction[m][0]
            board[y][x] = 1
            temp.append(m)
        move.extend(temp)

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            if board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
                answer += 1

print(answer)
