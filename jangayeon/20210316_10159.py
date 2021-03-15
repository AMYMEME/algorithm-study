#https://www.acmicpc.net/problem/10159



n=int(input())
m=int(input())

adj=[[0]*n for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    adj[a-1][b-1]=1

for i in range(n):
    for j in range(n):
        for k in range(n):
            if adj[j][i] and adj[i][k]:
                adj[j][k]=1

for i in range(n):
    cnt=0
    for j in range(n):
        if not adj[i][j] and not adj[j][i]:
            cnt+=1
    print(cnt-1)