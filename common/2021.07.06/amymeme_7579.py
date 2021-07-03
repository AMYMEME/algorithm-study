# https://www.acmicpc.net/problem/7579
# 앱
import sys

N, M = map(int, sys.stdin.readline().split())
memories = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))

# dp[cost] : cost일 떄 얻을 수 있는 최대 M
# cost 범위는 N <= 100이고, ci <= 100이므로, 10000이 최대
dp = [0] * 10001

for i, cost in enumerate(costs):
    for j in range(10000, cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + memories[i])

# dp[i]는 cost가 i일 때 최대 메모리 이므로, 탐색하면서 M이 나오는 최소 i를 찾으면 됨
for idx, max_mem in enumerate(dp):
    if max_mem >= M:
        print(idx)
        break
