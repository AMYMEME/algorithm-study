# https://www.acmicpc.net/problem/17144
# 백준 17144 - 미세먼지 안녕!
import sys
from collections import defaultdict


def spread():
    temp_board = defaultdict(int)
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                count = 0
                value = board[i][j]
                mini_value = value // 5
                for di, dj in diff:
                    ni, nj = i + di, j + dj
                    if -1 < ni < R and -1 < nj < C and (ni, nj) and (ni, nj) not in cleaner:
                        count += 1
                        temp_board[(ni, nj)] += mini_value
                board[i][j] = value - mini_value * count
    for i, j in temp_board.keys():
        board[i][j] += temp_board[(i, j)]


def work():
    top = cleaner[0][0]
    down = cleaner[1][0]

    for i in range(top - 1, 0, -1):
        board[i][0] = board[i - 1][0]

    for i in range(down + 1, R - 1):
        board[i][0] = board[i + 1][0]

    for i in range(C - 1):
        board[0][i] = board[0][i + 1]
        board[R - 1][i] = board[R - 1][i + 1]

    for i in range(top):
        board[i][C - 1] = board[i + 1][C - 1]
    for i in range(R - 1, down, -1):
        board[i][C - 1] = board[i - 1][C - 1]

    for i in range(C - 1, 1, -1):
        board[top][i] = board[top][i - 1]
        board[down][i] = board[down][i - 1]
    board[top][1] = 0
    board[down][1] = 0


diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
R, C, T = map(int, sys.stdin.readline().split())
cleaner = []
board = []
for i in range(R):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)
    if line[0] == -1:
        cleaner.append((i, 0))
time = 0
while T:
    T -= 1
    spread()
    work()

result = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            result += board[i][j]
print(result)
