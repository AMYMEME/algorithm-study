'''
https://www.acmicpc.net/problem/17144
'''
# python으로하면 시간초과 PyPy로하면 통과...

import sys
from itertools import chain

direction=[(1,0),(-1,0),(0,1),(0,-1)]
R,C,T=map(int,sys.stdin.readline().split())
A, ac=[], []
cycle1,cycle2=[],[]
for r in range(R):
    A.append(list(map(int,sys.stdin.readline().split())))
    for c,a in enumerate(A[r]):
        if a==-1:
            ac.append(r)

for _ in range(T):
    tmp=[[0]*C for x in range(R)]
    for r in range (R):
        for c in range (C):
            if A[r][c]>=5:
                cnt=0
                for dr,dc in direction:
                    nr,nc=r+dr,c+dc
                    if -1<nr<R and -1<nc<C and A[nr][nc]!=-1:
                        cnt+=1
                        tmp[nr][nc]+=A[r][c]//5
                A[r][c]-=(A[r][c]//5)*cnt
    A=[[A[r][c]+tmp[r][c] for c in range(C)]for r in range(R)]

    for r in range(ac[0]-1,0,-1):
        A[r][0]=A[r-1][0]
    A[0][:-1]=A[0][1:]
    for r in range(ac[0]):
        A[r][-1]=A[r+1][-1]
    A[ac[0]][2:]=A[ac[0]][1:-1]
    A[ac[0]][1]=0
    for r in range(ac[1]+1,R-1):
        A[r][0]=A[r+1][0]
    A[-1][:-1]=A[-1][1:]
    for r in range(R-1,ac[1],-1):
        A[r][-1]=A[r-1][-1]
    A[ac[1]][2:]=A[ac[1]][1:-1]
    A[ac[1]][1]=0
    A[ac[0]][0],A[ac[1]][0]=-1,-1

print(sum(chain(*A))+2) # 공기청정기 값 더하기