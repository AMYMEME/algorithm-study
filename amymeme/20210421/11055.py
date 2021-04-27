# https://www.acmicpc.net/problem/11055
# 백준 11055 - 가장 큰 증가 부분 수열

import sys
import copy


sys.stdin.readline()
A = list(map(int, sys.stdin.readline().split()))
dp = copy.deepcopy(A)

for cur_idx, current in enumerate(A[1:], start=1):
    for past_idx, past in enumerate(A[:cur_idx]):
        if past < current:
            dp[cur_idx] = max(dp[past_idx] + current, dp[cur_idx])
print(max(dp))
