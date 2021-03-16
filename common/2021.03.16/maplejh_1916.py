'''
https://www.acmicpc.net/problem/1916
'''
import sys
import heapq
INF=1000000000 # 최대값 설정!

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

graph=[[0 if i==j else INF for j in range(N)] for i in range (N)]
for _ in range(M):
    s,d,c=map(int,sys.stdin.readline().split())
    if graph[s-1][d-1]<=c: # 최소값으로
        continue
    graph[s-1][d-1]=c
start,dest=map(int,sys.stdin.readline().split())
start=start-1
dest=dest-1

# 다익스트라
dist=[INF]*N
dist[start]=0
route=[]
heapq.heappush(route,(0,start))
while route:
    cost, source=heapq.heappop(route)    
    for j in range(N):
        if graph[source][j]!=INF and cost+graph[source][j]<dist[j]:
            dist[j]=cost+graph[source][j]
            heapq.heappush(route,(dist[j],j))

print(dist[dest])