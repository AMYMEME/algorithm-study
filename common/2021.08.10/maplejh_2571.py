# https://www.acmicpc.net/problem/2571
import sys

n = int(sys.stdin.readline())
board = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            board[x + i][y + j] = 1

for r in range(1, 100):  # 연속되는 높이 기록
    for c in range(100):
        if board[r][c]:
            board[r][c] += board[r - 1][c]

answer = 0
for a in range(100):
    for b in range(100):  # 시작점 (a,b)
        h = 100  # 높이
        for d in range(100 - b):  # 가로로 움직이면서 최소 높이 찾기
            h = min(h, board[a][b + d])
            answer = max(answer, h * (d + 1))  # 최대 넓이 찾기

print(answer)
