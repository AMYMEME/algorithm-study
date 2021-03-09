'''
https://www.acmicpc.net/problem/10828
'''
import sys

N=int(sys.stdin.readline())
stack=[]
for _ in range(N):
    temp=sys.stdin.readline().split()
    cmd=temp[0]
    if cmd == "push":
        stack.append(temp[1])
    elif cmd == "pop":
        print(stack.pop()) if stack else print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(0) if stack else print(1)
    elif cmd == "top":
        print(stack[-1]) if stack else print(-1)