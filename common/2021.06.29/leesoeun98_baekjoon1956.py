v, e = map(int, input().split())
INF=987654321
graph = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    start, end, distance = map(int, input().split())
    graph[start][end] = distance

#플로이드 와샬...
for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])
result=INF
for i in range(1, v+1):
    result=min(result, graph[i][i])
if result==INF:
    print(-1)
else:
    print(result)
