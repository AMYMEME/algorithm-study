'''
https://www.acmicpc.net/problem/16234
'''
import sys
from collections import deque

def bfs(location):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dq=deque()
    dq.append(location)
    v=set()
    total=0
    while dq:
        vr,vc=dq.popleft()
        total+=A[vr][vc]
        v.add((vr,vc))
        for dr,dc in directions:
            nr,nc=vr-dr,vc-dc
            if -1<nr<N and -1<nc<N and visited[nr][nc]==0:
                if L<=abs(A[vr][vc]-A[nr][nc])<=R:
                    dq.append((nr,nc))
                    visited[nr][nc]=1
    population=total//len(v)
    for cr,cc in v:
        A[cr][cc]=population
    return 1 if len(v)>1 else 0

N,L,R=map(int,sys.stdin.readline().split())
A=[]

for _ in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))

move=0
while True:
    flag=0
    visited=[[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c]==0:
                visited[r][c]=1
                flag|=bfs((r,c))
    if flag:
        move+=1
    else:
        break

print(move)