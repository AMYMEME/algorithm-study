'''
https://www.acmicpc.net/problem/1939
'''
import sys
from collections import deque,defaultdict
      
def bfs(mid):
    visit=set()
    visit.add(one)
    dq=deque()
    dq.append(one)
    while dq:
        c=dq.popleft()
        for end,cost in bridge[c]:
            if end not in visit and cost>=mid:
                dq.append(end)
                visit.add(end)
    return True if two in visit else False

N,M=map(int,sys.stdin.readline().split())
bridge=defaultdict(list)
costs=set()
for _ in range(M):
    A,B,C=map(int,sys.stdin.readline().split())
    bridge[A].append((B,C))
    bridge[B].append((A,C))
    costs.add(C)
one,two=map(int,sys.stdin.readline().split())

costs=sorted(list(costs))

# 이분탐색
result=0
left=0
right=len(costs)-1
while(left<=right):
    mid=(left+right)//2
    if bfs(costs[mid]):        
        result=max(result,costs[mid])
        left=mid+1
    else:
        right=mid-1

print(result)