# https://www.acmicpc.net/problem/19238
# 백준 19238 - 스타트 택시

import sys
from collections import defaultdict, deque
import heapq


def bfs(si, sj):
    distances = [[0]*N for _ in range(N)]
    q = deque([(si, sj)])  # distance, i, j
    visited = {(si, sj)}
    while q:
        i, j = q.popleft()
        for diff_i, diff_j in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            ni = i + diff_i
            nj = j + diff_j
            if -1 < ni < N and -1 < nj < N and (ni, nj) not in visited:
                if board[ni][nj] == 0:  # 지나갈 수 있다면,
                    visited.add((ni, nj))
                    q.append((ni, nj))
                    distances[ni][nj] = distances[i][j] + 1
    return distances


N, M, fuel = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ci, cj = map(int, sys.stdin.readline().split())
ci -= 1
cj -= 1
customers = defaultdict(list)
for i in range(M):
    si, sj, di, dj = map(int, sys.stdin.readline().split())
    customers[i + 1].append((si - 1, sj - 1))
    customers[i + 1].append((di - 1, dj - 1))
exit_flag = False

while customers:
    distance_to_cus = []
    bfs_distances = bfs(ci, cj)
    for key in customers.keys():
        cus_i, cus_j = customers[key][0]
        heapq.heappush(distance_to_cus, (bfs_distances[cus_i][cus_j], cus_i, cus_j, key))
    cus_distance, cus_i, cus_j, key = heapq.heappop(distance_to_cus)
    di, dj = customers[key][1]
    if cus_i == di and cus_j == dj:  # 고객의 현재위치, 고객 목적지가 같을 경우
        ci = di
        cj = dj
        customers.pop(key)
        continue
    if cus_i != ci and cus_j != cj and cus_distance == 0:  # 벽에 막혀서 고객한테 갈 수 없는 경우
        # 그냥 cus_distance == 0으로 처리하면, 현재 택시위치와 고객 위치가 같은 경우를 잘못 처리함
        exit_flag = True
        break
    if fuel < cus_distance:  # 고객한테 가다가 연료가 모자른 경우
        exit_flag = True
        break
    fuel -= cus_distance
    des_distance = bfs(cus_i, cus_j)[di][dj]
    if fuel < des_distance or des_distance == 0:  # 목적지 가다가 연료 모자르거나, 목적지 못가는 경우
        exit_flag = True
        break
    fuel += des_distance
    ci = di
    cj = dj
    customers.pop(key)
if exit_flag:
    print(-1)
else:
    print(fuel)
