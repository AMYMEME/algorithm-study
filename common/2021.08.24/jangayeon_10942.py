import sys

n=int(input())
d=[int(i) for i in sys.stdin.readline().split()]
dp=[[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    dp[i][i]=1

for i in range(n-1):
    if d[i]==d[i+1]:
        dp[i][i+1]=1

for k in range(2,n):
    for i in range(n-k):
        if d[i]==d[i+k] and dp[i+1][i+k-1]==1:
            dp[i][i+k]=1



q=int(input())
for _ in range(q):
    i,j=[int(a) for a in sys.stdin.readline().split()]
    print(dp[i-1][j-1])

