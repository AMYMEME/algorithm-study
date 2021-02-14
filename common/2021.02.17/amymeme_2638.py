# https://www.acmicpc.net/problem/2638
# 백준 2638 - 치즈
import sys
from collections import deque


def check():
    global board
    # outer space check
    new_board = [[0]*M for _ in range(N)]
    new_board[0][0] = -1
    outer_space = deque([(0, 0)])
    while outer_space:
        ci, cj = outer_space.popleft()
        for di, dj in diff:
            ni, nj = di + ci, dj + cj
            if -1 < ni < N and -1 < nj < M:
                if board[ni][nj] == 0 and new_board[ni][nj] == 0:
                    outer_space.append((ni, nj))
                    new_board[ni][nj] = -1
    current_cheese = set()
    bye_cheese = set()
    # cheese check
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                current_cheese.add((i, j))
                count = 0
                for di, dj in diff:
                    ni, nj = i + di, j + dj
                    if new_board[ni][nj] == -1:
                        count += 1
                    if count > 1:
                        break
                if count > 1:
                    bye_cheese.add((i, j))
    for i, j in bye_cheese:
        board[i][j] = 0
    if current_cheese == bye_cheese:
        return False
    return True


diff = [(0, 1), (0, -1), (-1, 0), (1, 0)]
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time = 0
while True:
    time += 1
    if not check():
        break

print(time)