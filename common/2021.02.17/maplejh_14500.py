'''
https://www.acmicpc.net/problem/14500
'''
import sys

def dfs(depth,x,y,total):
    global result
    if depth==3:
        result=max(result,total)
        return
    else:
        for dx,dy in direction:
            vx=x+dx
            vy=y+dy
            if -1<vx<N and -1<vy<M and visit[vx][vy]==0:
                visit[vx][vy]=1
                dfs(depth+1,vx,vy,total+board[vx][vy])
                visit[vx][vy]=0 # 회전

def middle(x,y):
    global result
    if x+2<N and y+1<M:
        value=board[x][y]+board[x+1][y]+board[x+2][y]+board[x+1][y+1]
        result=max(result,value)
    if -1<x-1 and y+2<M:
        value=board[x][y]+board[x][y+1]+board[x][y+2]+board[x-1][y+1]
        result=max(result,value)
    if x+2<N and -1<y-1:
        value=board[x][y]+board[x+1][y]+board[x+2][y]+board[x+1][y-1]
        result=max(result,value)
    if x+1<N and y+2<M:
        value=board[x][y]+board[x][y+1]+board[x][y+2]+board[x+1][y+1]
        result=max(result,value)

direction=[(1,0),(-1,0),(0,1),(0,-1)]
N, M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result=0
visit=[[0]*M for _ in range(N)]
for x in range(N):
    for y in range(M):
        visit[x][y]=1
        dfs(0,x,y,board[x][y])
        visit[x][y]=0
        middle(x,y)

print(result)