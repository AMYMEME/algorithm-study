'''
https://www.acmicpc.net/problem/1753
'''
import sys
from collections import defaultdict
import heapq
INF=200001 # sys.maxsize

V,E=map(int,sys.stdin.readline().split())
K=int(sys.stdin.readline())
graph=defaultdict(list)
for _ in range(E):
    u,v,w=map(int,sys.stdin.readline().split())
    graph[u].append((v,w)) # 여러 개 간선 고려 필요 x

# 다익스트라
dist=[INF]*(V+1)
dist[K]=0
heap=[(0,K)]
while heap:
    cost,node=heapq.heappop(heap)
    for v,w in graph[node]:
        if w+cost<dist[v]:
            dist[v]=w+cost
            heapq.heappush(heap,(w+cost,v))

for i in dist[1:]:
    print(i if i!=INF else "INF")