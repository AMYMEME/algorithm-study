v, e = map(int, input().split())
tree=[[0]*(v+1) for _ in range(v+1)]
check=[0]*(v+1)
res=[]
for _ in range(e):
    a, b, c = map(int, input().split())
    tree[a][b]=c
    tree[b][a]=c

def dfs(i, visited, cnt):
    for next in range(len(tree[i])):
        if next not in visited and tree[i][next]!=0 :
            visited+=[next]
            cnt+=tree[i][next]
    return cnt

for i in range(1, v+1):
    res.append(dfs(i, [i], 0))
print(min(res))
