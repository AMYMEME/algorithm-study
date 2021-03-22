#https://www.acmicpc.net/problem/1916


import heapq
import sys
r = sys.stdin.readline
INF = 1e9


def dijkstra(n, s, e, edg):
    q = []
    dist = [INF] * n #각 도시 사이 거리 무한대
    dist[s-1] = 0 #시작 지점 0
    heapq.heappush(q, [s-1, 0]) #힙에 시작 지점 추가

    while q:
        pos, cost = heapq.heappop(q)

        for p, c in edg[pos]:
            c += cost #현재 노드+연결된 다른 노드
            if c < dist[p]: #현재 노드를 거쳐서 다른 노드로 이동이 더 짧은 경우
                dist[p] = c
                heapq.heappush(q, [p, c]) #최소연결값 갱신
    return dist[e-1]


N = int(r()) #도시갯수
M = int(r()) #버스 갯수
edges = [[] for _ in range(N)] #도시와 버스 - 출발점에 따른 도착점과 비용
for i in range(M):
    u, v, w = list(map(int, r().split())) #출발, 도착, 비용
    edges[u-1].append([v-1, w])

st, end = map(int, r().split()) #출발점, 도착점

print(dijkstra(N,st, end, edges))