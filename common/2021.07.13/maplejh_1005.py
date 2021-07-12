# https://www.acmicpc.net/problem/1005
import sys
from collections import defaultdict, deque

T = int(sys.stdin.readline())
for x in range(T):
    N, K = map(int, sys.stdin.readline().split())
    building = [-1] + list(map(int, sys.stdin.readline().split()))  # 각 건물 건설시간
    rule = defaultdict(list)  # 건설 규칙
    indegree = [0] * (N + 1)  # 진입 차수
    for y in range(K):
        pre, post = map(int, sys.stdin.readline().split())
        rule[pre].append(post)
        indegree[post] += 1
    W = int(sys.stdin.readline().strip())
    q = deque()
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if not indegree[i]:
            q.append(i)
            dp[i] = building[i]

    answer = 0
    while q:
        pre_node = q.popleft()
        if not indegree[W]:
            break
        for post_node in rule[pre_node]:
            indegree[post_node] -= 1
            dp[post_node] = max(dp[post_node], dp[pre_node] + building[post_node])
            if not indegree[post_node]:
                q.append(post_node)
    print(dp[W])
