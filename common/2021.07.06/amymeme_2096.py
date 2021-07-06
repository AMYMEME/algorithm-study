# https://www.acmicpc.net/problem/2096
# BOJ 2096 - 내려가기

import sys

N = int(sys.stdin.readline())

dp_min = [0, 0, 0]
dp_max = [0, 0, 0]

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))

    pre_dp_min = [min(dp_min[:2]), min(dp_min), min(dp_min[1:])]
    pre_dp_max = [max(dp_max[:2]), max(dp_max), max(dp_max[1:])]

    dp_min = [x + y for (x, y) in zip(row, pre_dp_min)]
    dp_max = [x + y for (x, y) in zip(row, pre_dp_max)]

print(max(dp_max), min(dp_min))
