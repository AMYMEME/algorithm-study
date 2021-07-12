# https://www.acmicpc.net/problem/1005
# ACM Craft

from collections import defaultdict
import sys

T = int(sys.stdin.readline())
graph = defaultdict(set)
max_time = 0


def dfs(cur, cur_time):
    global max_time
    if not graph[cur]:
        max_time = max(max_time, cur_time)
        return
    for nxt in graph[cur]:
        dfs(nxt, cur_time + times[nxt - 1])


for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    times = list(map(int, sys.stdin.readline().split()))

    for _ in range(K):
        before, after = map(int, sys.stdin.readline().split())
        graph[after].add(before)
    goal_building = int(sys.stdin.readline())
    dfs(goal_building, times[goal_building - 1])
    print(max_time)
    max_time = 0
    graph.clear()
