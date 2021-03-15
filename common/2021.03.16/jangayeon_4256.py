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



     