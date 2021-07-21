#문제:https://www.acmicpc.net/problem/1504
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize


def djstra(start, end):
    dist = [INF] * (N + 1)

    Q = []
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        now_dist, now_node = heapq.heappop(Q)

        for next_dist, next_node in graph[now_node]:
            next_dist = next_dist + now_dist

            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(Q, [next_dist, next_node])

    return dist[end]


N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    start, end, cost = map(int, input().split())

    graph[start].append([cost,end])
    graph[end].append([cost,start])

must1, must2 = map(int, input().split())

tmp1 = djstra(1, must1) +djstra(must1, must2) + djstra(must2, N)
tmp2 = djstra(1, must2) + djstra(must2, must1) + djstra(must1, N)

if tmp1 >= INF and tmp2 >= INF:
    print(-1)
else:
    print(min(tmp1, tmp2))
