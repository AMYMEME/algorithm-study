# https://www.acmicpc.net/problem/3190
# 백준 3190 - 뱀
import sys
from collections import deque


def direct_change(direct, change):
    directs = ['right', 'down', 'left', 'up']
    for idx, d in enumerate(directs):
        if d == direct:
            if change == 'L':
                return directs[(idx - 1) % 4]
            else:
                return directs[(idx + 1) % 4]


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apples = set()
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    apples.add((i - 1, j - 1))  # for list index
L = int(sys.stdin.readline())
direct_info = dict()
for _ in range(L):
    time, C = sys.stdin.readline().split()
    direct_info[int(time)] = C
snake = deque([(0, 0)])
time = 1
ni, nj = 0, 1  # next
current_direct = 'right'

while -1 < ni < N and -1 < nj < N and (ni, nj) not in snake:
    snake.append((ni, nj))

    if (ni, nj) not in apples:
        snake.popleft()
    else:
        apples.remove((ni, nj))

    if time in direct_info.keys():
        current_direct = direct_change(current_direct, direct_info[time])
    if current_direct == 'right':
        nj += 1
    elif current_direct == 'left':
        nj -= 1
    elif current_direct == 'up':
        ni -= 1
    else:
        ni += 1
    time += 1

print(time)
