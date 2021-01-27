'''
https://www.acmicpc.net/problem/14891
'''

import sys
from collections import deque
from copy import deepcopy

def left(onegear): # 반시계방향
    return (255&onegear<<1)|((onegear&(1<<7))>>7)

def right(onegear): # 시계방향
    return (255&onegear>>1)|((onegear&1)<<7)

def turn(gear,state): 
    temp=deepcopy(gear)
    q=deque()
    temp[state[0]]=(left(gear[state[0]]) if state[1]==-1 else right(gear[state[0]])) # 주어진 톱니바퀴회전
    visit=[state[0]] # 처리한 톱니바퀴
    q.append(state)
    while(q):
        num, direction=q.popleft()
        for d in [1,-1]:
            if num+d>-1 and num+d<4 and num+d not in visit: 
                (big, small)=(num+d,num) if d==1 else (num,num+d)
                if ((gear[small]&(1<<5))>>5)^((gear[big]&(1<<1))>>1): # ^연산 -> 같으면 0 다르면 1 
                    temp[num+d]=(left(gear[num+d]) if direction==1 else right(gear[num+d]))
                    q.append((num+d,-direction))
                    visit.append(num+d)
    return temp

if __name__=="__main__":
    gear=[]
    for n in range(4):
        gear.append(int(sys.stdin.readline().strip(),2)) # 이진수-> 십진수 형태로
    k=int(sys.stdin.readline())
    for i in range(k):
        num, direction=map(int,sys.stdin.readline().split())
        gear=turn(gear,(num-1,direction))
    sum=0
    for n,i in enumerate(gear): # 비트연산(1,2,4,8)
        sum|=(i&(1<<7))>>(7-n)
    print(sum)