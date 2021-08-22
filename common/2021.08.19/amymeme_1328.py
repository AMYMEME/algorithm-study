# https://www.acmicpc.net/problem/1328
# 고층 빌딩

import sys
from collections import defaultdict


def start():
    if N == 1:
        return 1
    if N == 2:
        return 1
    for n in range(3, N):
        for l in range(1, L + 1):
            for r in range(1, R + 1):
                dp[(n, l, r)] = (dp[(n - 1, l - 1, r)] + dp[(n - 1, l, r - 1)] + dp[(n - 1, l, r)] * (n - 2)) % MOD
    return (dp[(N - 1, L - 1, R)] + dp[(N - 1, L, R - 1)] + dp[(N - 1, L, R)] * (N - 2)) % MOD


MOD = 1000000007
dp = defaultdict(int)
dp[(1, 1, 1)] = 1
dp[(2, 1, 2)] = 1
dp[(2, 2, 1)] = 1

N, L, R = map(int, sys.stdin.readline().split())
print(start())
