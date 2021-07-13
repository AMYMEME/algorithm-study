# https://www.acmicpc.net/problem/7579
import sys

N,M=map(int,sys.stdin.readline().split())
mem=[0]+list(map(int,sys.stdin.readline().split()))
cost=[0]+list(map(int,sys.stdin.readline().split()))

max_cost=sum(cost)
result=max_cost

# i번째 앱까지 사용해서 cost j 만드는 최대 byte
dp=[[0]*(max_cost+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,max_cost+1):
        if cost[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-cost[i]]+mem[i])

        if dp[i][j]>=M:
            result=min(j,result)
print(result if M else 0)
