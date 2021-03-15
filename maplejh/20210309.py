'''
https://www.acmicpc.net/problem/3190
'''
import sys
from collections import deque

def play():
    snake=deque([(1,1)])
    dir={0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
    s_dir=1 # 뱀의 방향
    time=1
    while(True):
        # 뱀이 움직일 곳 (r,c)
        r=dir[s_dir][0]+snake[-1][0]
        c=dir[s_dir][1]+snake[-1][1]
        if r==0 or r==N+1 or c==0 or c==N+1 or (r,c) in snake:
            return time
        else:
            snake.append((r,c))
        if (r,c) in apple:
            apple.remove((r,c))
        else:
            snake.popleft()
        if time in c_dir.keys():
            if c_dir[time]=='L':
                s_dir=(s_dir-1)%4
            else:
                s_dir=(s_dir+1)%4
        time+=1

N=int(sys.stdin.readline())
K=int(sys.stdin.readline())
apple=[]
for _ in range(K):
    row,col=map(int,sys.stdin.readline().split())
    apple.append((row,col))
L=int(sys.stdin.readline())
c_dir=dict() # 방향 변환 정보
for _ in range(L):
    T,C=sys.stdin.readline().split()
    c_dir[int(T)]=C

print(play())