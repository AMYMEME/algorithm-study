#https://www.acmicpc.net/problem/11729

import sys



def hanoi(n,start,help,end):
    if n==1:
        print(start,end)
    else:
        hanoi(n-1,start,end,help)
        print(start,end)
        hanoi(n-1,help,start,end)

n=int(input())
total=1
for _ in range(n-1):
    total=total*2+1
print(total)
hanoi(n,1,2,3)

