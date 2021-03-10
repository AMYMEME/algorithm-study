'''
https://www.acmicpc.net/problem/2493
'''
import sys

N=int(sys.stdin.readline())
top=list(map(int,sys.stdin.readline().split()))

stack=[]
result=[0]*N
for n,t in enumerate(top):
    while stack:
        if stack[-1][1]>t:
            result[n]=stack[-1][0]
            break
        else:
            stack.pop()
    stack.append((n+1,t))

print(*result)