import sys
from collections import deque
input=sys.stdin.readline

n,m=map(int, input().split())
adj=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,w=map(int,input().split())
    adj[a].append((b,w))
    adj[b].append((a,w))

start,end=map(int,input().split())
min_=1
max_=1000000000


def bfs(c):
    queue=deque()
    queue.append(start)
    visit=[False]*(n+1)
    visit[start]=True
    while queue:
        x=queue.popleft()
        for y,weight in adj[x]:
            if not visit[y] and c<=weight:
                queue.append(y)
                visit[y]=True
    
    return visit[end]

while min_<=max_:
    mid=(min_+max_)//2

    if bfs(mid):
        result=mid
        min_=mid+1
    else:
        max_=mid-1

print(result)


