"""
https://www.acmicpc.net/problem/3055
"""
import sys
from collections import deque
from copy import deepcopy
from itertools import chain

direction=[(1,0),(0,1),(-1,0),(0,-1)]


def bfs(start):
    temp=deepcopy(board)
    distance=[]
    q=deque()
    q.append((start,0)) # 방문할 점,시작점에서 이동횟수
    while q:
        (vx,vy),count=q.popleft()
        for dx,dy in direction:
            nx=vx+dx
            ny=vy+dy
            if -1<nx<R and -1<ny<C and temp[nx][ny]!=-1:
                temp[nx][ny] = -1  # visit
                if board[nx][ny]=="D":
                    distance.append(count+1)
                elif board[nx][ny]=="X":
                    continue
                elif board[nx][ny]==".":
                    q.append(((nx, ny), count + 1))
                elif board[nx][ny]>count+1:
                    q.append(((nx,ny),count+1))
    return sorted(distance)[0] if len(distance) else "KAKTUS"


R,C= map(int,sys.stdin.readline().split(" "))
board=[]
for i in range(R):
    board.append(list(sys.stdin.readline().strip()))
    for n,j in enumerate(board[i]):
        if j=="S":
            board[i][n]="."
            S=(i,n)
        if j=="*":
            board[i][n]=0

num=0
while True:
    num+=1
    for i in range(R):
        for j in range(C):
            if board[i][j]==(num-1):
                for dx, dy in direction:
                    nx = i + dx
                    ny = j + dy
                    if -1 < nx < R and -1 < ny < C:
                        if board[nx][ny]==".":
                            board[nx][ny]=num

    if "." not in chain(*board) or num>R*C :
        break

print(bfs(S))
