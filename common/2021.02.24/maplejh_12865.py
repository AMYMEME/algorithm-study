'''
https://www.acmicpc.net/problem/12865
'''
import sys

N,K=map(int,sys.stdin.readline().split())
item=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[0]*(K+1) for _ in range(N+1)]

for i in range (1,N+1):
    for j in range(1,K+1):
        if item[i-1][0]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-item[i-1][0]]+item[i-1][1])

print(dp[N][K])