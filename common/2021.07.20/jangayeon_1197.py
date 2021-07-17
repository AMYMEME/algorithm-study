#문제: https://www.acmicpc.net/problem/1197

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def make_union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
graph = []

parent = [0] * (V + 1)
for i in range(V + 1):
    parent[i] = i

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append([C, A, B])


graph.sort()
count = 0
answer = 0

while graph:
    if count == (V-1):
        break

    C,A,B = graph.pop(0)

    if find_parent(parent, A) == find_parent(parent, B):
        continue
    else:
        make_union(parent, A, B)
        count += 1
        answer += C
print(answer)