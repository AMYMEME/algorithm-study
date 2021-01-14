# 백준 #19640
# https://www.acmicpc.net/problem/19640

import sys
from itertools import repeat, islice


N, M, K = map(int, sys.stdin.readline().split())
lines = [[] for i in repeat(None, M)]
result = 0

for original_turn in range(N):
    D, H = map(int, sys.stdin.readline().split())
    lines[(original_turn + M) % M].append([D, H, original_turn])

while lines:
    next_turn = [0, 0]
    next_index = 0

    for i in range(M):
        if lines[i] and lines[i][0][:2] > next_turn[:2]:
            next_turn = lines[i][0]
            next_index = i
    if lines[next_index].pop(0)[2] == K:
        print(result)
        break
    result += 1
