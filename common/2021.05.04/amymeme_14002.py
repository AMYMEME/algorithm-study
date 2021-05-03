# https://www.acmicpc.net/problem/14002
# 백준 14002 - 가장 긴 증가하는 부분 수열 4

import copy
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [[] for _ in range(N)]

for cur_idx, cur_value in enumerate(A):
    if cur_idx == 0:
        dp[cur_idx].append(cur_value)
        continue
    for past_idx, past_value in enumerate(A[:cur_idx]):
        if past_value < cur_value and len(dp[cur_idx]) < len(dp[past_idx]) + 1:
            dp[cur_idx] = copy.deepcopy(dp[past_idx])
            dp[cur_idx].append(cur_value)
    if not dp[cur_idx]:
        dp[cur_idx].append(cur_value)
lengths = map(lambda x: (len(x), x), dp)
result = sorted(lengths, reverse=True)[0]
print(result[0])
for elem in result[1]:
    print(elem, end=' ')
