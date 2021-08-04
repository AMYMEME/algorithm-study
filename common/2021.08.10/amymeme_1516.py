# https://www.acmicpc.net/problem/1516
# 게임 개발

import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline())
cost = defaultdict(int)
advance_count = defaultdict(int)
in_adj = defaultdict(list)
out_adj = defaultdict(list)
answer = defaultdict(int)

for building_number in range(1, N + 1):
    row = list(map(int, sys.stdin.readline().split()))
    cost[building_number] = row[0]
    in_advances = row[1:-1]
    in_adj[building_number] = in_advances
    advance_count[building_number] += len(in_advances)
    for advance in in_advances:
        out_adj[advance].append(building_number)

leaves = deque(map(lambda x: x[0], filter(lambda x: not x[1], advance_count.items())))

while leaves:
    leaf = leaves.popleft()
    answer[leaf] = cost[leaf]
    need_times = [answer[advance] for advance in in_adj[leaf]]
    answer[leaf] += max(need_times) if need_times else 0

    for after in out_adj[leaf]:
        advance_count[after] -= 1
        if not advance_count[after]:
            leaves.append(after)

for key in range(1, N + 1):
    print(answer[key])
