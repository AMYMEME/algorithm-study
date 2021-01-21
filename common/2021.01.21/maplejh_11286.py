'''
https://www.acmicpc.net/problem/11286
'''

import sys, heapq

N=int(sys.stdin.readline())
abs_heap=[]
for i in range(N):
    x=int(sys.stdin.readline())
    if x!=0:
        heapq.heappush(abs_heap,(abs(x),x))
    else:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)