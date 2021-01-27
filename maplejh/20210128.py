'''
https://www.acmicpc.net/problem/10026
'''

import sys
from collections import deque

def bfs(board,location,color):
    direction=[(1,0),(-1,0),(0,1),(0,-1)]
    q=deque()
    q.append(location)
    while q:
        vx,vy=q.popleft()
        for dx, dy in direction:
            nx,ny=vx+dx,vy+dy
            if -1<nx<len(board) and -1<ny<len(board):
                if board[nx][ny]==color: # 같은 색인 경우
                    q.append((nx,ny))
                    board[nx][ny]=0 # visit

if __name__ == "__main__":
    N=int(sys.stdin.readline())
    board1=[]
    board2=[]
    for n in range(N): # 적록색약 x
        board1.append(list(sys.stdin.readline().strip()))
        temp=[]
        for element in board1[n]: # 적록색약 o
            if element=="R":
                temp.append("G")
            else:
                temp.append(element)
        board2.append(temp)
  
    region1, region2=0, 0
    for x in range (N):
        for y in range(N):
            if board1[x][y]!=0:
                bfs(board1,(x,y),board1[x][y])
                region1+=1
            if board2[x][y]!=0:
                bfs(board2,(x,y),board2[x][y])
                region2+=1
    print(region1,region2)