import heapq
import collections
v, e = map(int, input().split())
graph = collections.defaultdict(list)
check=[0]*(v+1)

for _ in range(e):
    start, end, weight = map(int, input().split())
    graph[start].append([weight, start, end])
    graph[end].append([weight, end, start])

def prim(start):
    check[start]=1
    candidate = graph[start]
    heapq.heapify(candidate)
    tree=[]
    res=0

    while candidate:
        weight, start, end = heapq.heappop(candidate)
        if check[end]==0:
            check[end]=1
            tree.append([start, end])
            res+=weight

            for next in graph[end]:
                if check[next[2]]==0:
                    heapq.heappush(candidate, next)
    return res

print(prim(1))
