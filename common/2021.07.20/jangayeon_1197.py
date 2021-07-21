#문제: https://www.acmicpc.net/problem/1197

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


def union(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


V, E = map(int, input().split())
graph = []

p = [0] * (V + 1)
for i in range(V + 1):
    p[i] = i

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append([C, A, B])


graph.sort()
count = 0
ans = 0

while graph:
    if count == (V-1):
        break

    C,A,B = graph.pop(0)

    if find_parent(p, A) == find_parent(p, B):
        continue
    else:
        union(p, A, B)
        count += 1
        ans += C
print(ans)