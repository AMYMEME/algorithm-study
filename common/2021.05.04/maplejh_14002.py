"""
https://www.acmicpc.net/problem/14002
"""
import sys

N= int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

dp=[1]*N
for cur in range(1,N):
    for past in range(cur):
        if A[cur]>A[past]:
            if dp[cur]<dp[past]+1:
                dp[cur]=dp[past]+1

cnt=max(dp)
print(cnt)

idx=dp.index(cnt)
answer=[]
while cnt>0:
    if cnt==dp[idx]:
        answer.append(A[idx])
        cnt-=1
    idx-=1
print(*answer[::-1])
