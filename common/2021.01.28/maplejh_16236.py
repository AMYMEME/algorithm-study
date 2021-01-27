'''
https://www.acmicpc.net/problem/16236
'''

import sys
from collections import deque
from copy import deepcopy

def bfs(board,baby_shark):
    temp_board=deepcopy(board)
    direction=[(1,0),(-1,0),(0,1),(0,-1)]
    q=deque()
    q.append((baby_shark[1],0)) # (거쳐서 갈 수 있는 곳, 상어에서 거리)
    distance=[] # 잡아먹을 수 있는 물고기 거리->시간,(좌표)
    while(q):
        (vx,vy),count=q.popleft()
        for dx,dy in direction:
            nx,ny=vx+dx,vy+dy
            if -1<nx<len(board) and -1<ny<len(board):
                if temp_board[nx][ny]==0 or temp_board[nx][ny]==baby_shark[0]:
                    q.append(((nx,ny),count+1))
                elif temp_board[nx][ny]>0 and temp_board[nx][ny]<baby_shark[0]:
                    distance.append((count+1,(nx,ny)))
                temp_board[nx][ny]=-1 # visit
    return sorted(distance)[0] if len(distance)!=0 else (0,(0,0))

if __name__=="__main__":
    N=int(sys.stdin.readline())
    board=[]
    for x in range(N):
        board.append(list(map(int,sys.stdin.readline().split())))
        for y, a in enumerate(board[x]):
            if a==9: 
                baby_shark=(2,(x,y)) # 사이즈, 아기상어위치
                board[x][y]=0
    time,cnt=0,0
    while(True): 
        t,(rx,ry)=bfs(board,baby_shark) # t: 물고기 한마리 잡아먹을때 걸리는 시간
        if t==0: # 더 이상 못 잡아 먹음
            break
        board[rx][ry]=0
        time+=t
        cnt+=1
        if cnt==baby_shark[0]:
            baby_shark=(baby_shark[0]+1,(rx,ry))
            cnt=0
        else:
            baby_shark=(baby_shark[0],(rx,ry))
    print(time)