# https://www.acmicpc.net/problem/1976
import sys
from collections import defaultdict


def find(parent):
    if parent not in answer:
        answer.add(parent)
    for k in board[parent]:
        if k not in answer:
            answer.add(k)
            find(k)


N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
board=defaultdict(set)
for i in range(1,N+1):
    temp=map(int,sys.stdin.readline().split())
    for j,n in enumerate(temp):
        if n:
            board[i].add(j+1)
plan=list(map(int,sys.stdin.readline().split()))


answer = set()
find(plan[0])

s_plan=set(plan)
print("YES" if s_plan&answer==s_plan else "NO")