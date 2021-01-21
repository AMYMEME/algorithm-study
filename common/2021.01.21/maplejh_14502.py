'''
https://www.acmicpc.net/problem/14502
'''

import sys
from copy import deepcopy
from itertools import combinations, chain
from collections import deque

def bfs(virus, copy_board):
    direction=[(1,0),(-1,0),(0,1),(0,-1)]
    q=deque()
    q.extend(virus)
    while q:
        vx,vy=q.popleft()
        for dx, dy in direction:
            nx,ny=vx+dx,vy+dy
            if -1<nx<len(copy_board[0]) and -1<ny<len(copy_board):
                if copy_board[ny][nx]==0:
                    copy_board[ny][nx]=2
                    q.append((nx,ny))
    return list(chain.from_iterable(copy_board)).count(0) # flatten

if __name__ == "__main__":
    N,M=map(int,sys.stdin.readline().split())
    board, empty, virus=[],[],[]
    for y in range(N):
        board.append(list(map(int,sys.stdin.readline().split())))
        for x, a in enumerate(board[y]):
            if a==0: # 빈공간 좌표
                empty.append((x,y))
            elif a==2: # virus 좌표
                virus.append((x,y))
    result=0
    for candidates in list(combinations(empty, 3)): # 빈공간에 기둥 조합
        copy_board=deepcopy(board)
        for x,y in candidates:
            copy_board[y][x]=1
        result=max(result,bfs(virus,copy_board))
    print(result)