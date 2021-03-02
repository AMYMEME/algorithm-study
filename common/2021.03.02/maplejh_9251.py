'''
https://www.acmicpc.net/problem/9251
'''
import sys

X=sys.stdin.readline().strip()
Y=sys.stdin.readline().strip()
N=len(X)
M=len(Y)
dp=[[0]*(N+1) for _ in range (M+1)]

for i in range(1,M+1):
    for j in range(1,N+1):
        if Y[i-1]==X[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])