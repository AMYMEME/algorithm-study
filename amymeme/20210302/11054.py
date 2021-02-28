# https://www.acmicpc.net/problem/11054
# 백준 11054 - 가장 긴 바이토닉 부분 수열

import sys


def lis(A):
    N = len(A)
    dp = [1 for _ in range(N)]
    for cur_idx, current in enumerate(A):
        if cur_idx == 0:
            continue
        for pas_idx, past in enumerate(A[:cur_idx]):
            if current > past:
                dp[cur_idx] = max(dp[pas_idx] + 1, dp[cur_idx])
    return dp


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
result = 0
forward = lis(A)
backward = lis(A[::-1])[::-1]
print(max(list(map(sum, zip(forward, backward)))) - 1)
