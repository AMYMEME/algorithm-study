# https://www.acmicpc.net/problem/1328
import sys

N, L, R = map(int, sys.stdin.readline().split())
# dp 이용 - dp[k][i][j] k개의 건물중에서 왼쪽에서는 i개 오른쪽에서는 j개가 보이는 경우의수
dp = [[[0 for a in range(R + 1)] for b in range(L + 1)] for c in range(N + 1)]
dp[1][1][1] = 1

# 큰 빌딩부터 배치
for k in range(2, N + 1):
    for i in range(1, L + 1):
        for j in range(1, R + 1):
            # k번째로 큰 빌딩을 배치
            dp[k][i][j] = (dp[k - 1][i - 1][j] +  # k-1개 배치에서 맨 왼쪽에 배치
                           dp[k - 1][i][j - 1] +  # k-1개 배치에서 맨 오른쪽에 배치
                           dp[k - 1][i][j] * (k - 2)) % 1000000007  # k-1개 배치에서 건물 사이에 배치
print(dp[N][L][R])
