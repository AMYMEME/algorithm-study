from collections import deque

n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p].append([w, c])
    tree[c].append([w, p])

def bfs(root, mode):
    queue=deque()
    queue.append(root)
    distance=[-1]*(n+1)
    distance[root]=0
    
    while queue:
        node = queue.popleft()
        for w, adj in tree[node]:
            if distance[adj]==-1:
                distance[adj]=distance[node]+w
                queue.append(adj)
    if mode==1:
        return distance.index(max(distance))
    else:
        return max(distance)

print(bfs(bfs(1, 1), 0))
        
