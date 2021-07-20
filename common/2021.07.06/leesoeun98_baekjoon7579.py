import sys
n, m = map(int, sys.stdin.readline().split())
memory=[0]+list(map(int, sys.stdin.readline().split()))
cost=[0]+list(map(int, sys.stdin.readline().split()))

#냅색 문제 (초반에 백트래킹으로 시도했다가 실패...냅색인거 다른 사람 코드보고 깨달음)
dp=[[0]*(sum(cost)+1) for _ in range(n+1)]
res=sum(cost)

# i번째 app까지로 j의 cost로 만들 수 있는 memory 최대가 dp[i][j]
for i in range(1, n+1):
    for j in range(1, sum(cost)+1):
        if cost[i]>j:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-cost[i]]+memory[i])
        if dp[i][j]>=m:
            res=min(res, j)
if m!=0:
    print(res)
else:
    print(0)
