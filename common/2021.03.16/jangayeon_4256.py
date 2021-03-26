#https://www.acmicpc.net/problem/4256 -> 출력 형식 에러

import sys
global pre_
global in_

def post(s,n,e):
    for i in range(s,e):
        if(in_[i]==pre_[e]):
            post(s,i,r+1)
            post(i+1,e,r+1+i-s)
            print(pre_[r],end=" ")
        

case= int(sys.stdin.readline().strip())
for i in range(case):
    _ = int(sys.stdin.readline()) 
    pre_=list(map(int,sys.stdin.readline().strip().split()))
    in_=list(map(int,sys.stdin.readline().strip().split()))

    post(0,case,0)



#https://www.acmicpc.net/problem/4256

import sys

def post(pre_,in_):
    if len(pre_)==0:
        return
    elif len(pre_)==1:
        print(pre_[0],end=" ")
    elif len(pre_)==2:
        print(pre_[1],pre_[0],end=" ")


    idx=in_.index(pre_[0])
    in_left=in_[0:idx]
    pre_left=pre_[1:1+len(in_left)]
    post(pre_left,in_left)

    in_right=in_[idx+1:]
    pre_right=pre_[1+len(pre_left):]
    post(pre_right,in_right)
    print(pre_[0],end=" ")

case= int(sys.stdin.readline().strip())
for i in range(case):
    pre_=list(map(int,sys.stdin.readline().strip().split()))
    in_=list(map(int,sys.stdin.readline().strip().split()))
    post(pre_,in_)
    print()     