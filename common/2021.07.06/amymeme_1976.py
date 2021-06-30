# https://www.acmicpc.net/problem/1976
# 여행 가자
from collections import deque
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for x in range(N):
    board[x][x] = 1

for x in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][x] and board[x][j] and not board[i][j]:
                board[i][j] = 1
                board[j][i] = 1

print(board)
want_cities = deque(map(lambda k: int(k) - 1, sys.stdin.readline().split()))
flag = 'YES'
while want_cities:
    want_city = want_cities.popleft()
    if not want_cities:
        break
    if not board[want_city][want_cities[0]]:
        flag = 'NO'
        break
print(flag)
