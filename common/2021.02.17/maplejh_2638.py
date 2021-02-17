'''
https://www.acmicpc.net/problem/2638
'''
import sys
from itertools import chain

def dfs(x,y):
    cheese[x][y]=-1 # visit대신
    for dx,dy in direction:
        vx=x+dx
        vy=y+dy
        if -1<vx<N and -1<vy<M:
            if cheese[vx][vy]>0:
                cheese[vx][vy]+=1
            elif cheese[vx][vy]==0:
                dfs(vx,vy)

def melt():
    for x in range(N):
        for y in range(M):
            if 0<cheese[x][y]<3:
                cheese[x][y]=1
            else:
                cheese[x][y]=0
    return 1

sys.setrecursionlimit(10000) # 재귀제한 (recursion error)
direction=[(1,0),(-1,0),(0,1),(0,-1)]
N,M=map(int,sys.stdin.readline().split())
cheese=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

count=0
while (max(chain(*cheese))):
    dfs(0,0)
    count+=melt()
print(count)