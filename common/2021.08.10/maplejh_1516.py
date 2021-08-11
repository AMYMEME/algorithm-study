# https://www.acmicpc.net/problem/1516
import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline())
buildings = defaultdict(int)  # 건물 짓는데 걸리는 시간
order = defaultdict(list)  # 먼저: 나중
indegree = [0] * (N + 1)  # 진입차수
q = deque()  # 진입차수가 0인 노드
dp = [0] * (N + 1)  # 먼저 지어져야 하는 건물들이 완성되는데 걸리는 시간

for i in range(1, N + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    buildings[i] = temp[0]
    for t in temp[1:-1]:
        order[t].append(i)
    indegree[i] = len(temp[1:-1])
    if not indegree[i]:
        q.append(i)
        dp[i] = buildings[i]

while q:
    pre_node = q.popleft()
    for post_node in order[pre_node]:
        indegree[post_node] -= 1
        dp[post_node] = max(dp[post_node], buildings[pre_node])
        if not indegree[post_node]:
            buildings[post_node] += dp[post_node]
            q.append(post_node)

for k in range (1, N + 1):
    print(buildings[k])
