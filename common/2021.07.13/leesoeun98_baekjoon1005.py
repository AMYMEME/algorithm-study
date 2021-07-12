from collections import deque
import sys
for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    delay=[0]+list(map(int, sys.stdin.readline().split()))
    buildings=[[] for _ in range(n+1)]
    indegree=[0]*(n+1)
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        buildings[x].append(y)
        indegree[y]+=1
    must=int(sys.stdin.readline())

    dp=[0]*(n+1)
    queue=deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            queue.append(i)
            dp[i]=delay[i]

    while queue:
        cur = queue.popleft()
        for next in buildings[cur]:
            indegree[next]-=1
            dp[next]=max(dp[next], dp[cur]+delay[next])
            if indegree[next]==0:
                queue.append(next)
    print(dp[must])

