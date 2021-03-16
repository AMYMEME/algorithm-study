'''
https://www.acmicpc.net/problem/1927
'''
import sys
import heapq

N=int(sys.stdin.readline())
heap=[]

for _ in range(N):
    x=int(sys.stdin.readline())
    if x:
        heapq.heappush(heap,x)
    else:
        print(heapq.heappop(heap)) if len(heap) else print(0)