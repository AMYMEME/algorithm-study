from collections import deque

def solution(n, edge):
    #1번노드에서 각 노드까지의 거리 저장할 배열 distance
    distance=[-1]*(n+1)
    
    #간선 그래프 만들고
    graph={}
    for start, end in edge:
        graph[start]=graph.get(start, [])+[end]
        graph[end]=graph.get(end, [])+[start]

    queue=deque()
    queue.append((1,0))
    
    #1번 노드에서 각 노드까지의 최단거리를 구함 (bfs) 
    while queue:
        node, depth = queue.popleft()
        distance[node]=depth
        for adj in graph[node]:
            if distance[adj]==-1:
                distance[adj]=0
                queue.append((adj, depth+1))
    
    #거기서 최댓값이 같은게 몇개인지 세기 
    return distance.count(max(distance))
