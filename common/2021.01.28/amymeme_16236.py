# https://www.acmicpc.net/problem/16236
# 백준 16236 - 아기 상어
import heapq
import sys
from collections import deque


def bfs(ci, cj):
    q = deque([(ci, cj, 0)])  # 지나갈 수 있는 경로와 현재위치까지의 거리
    visited = {(ci, cj)}
    # 현재 위치 제외하고 다음부터 (거리, i, j) heapq 에 넣음 -> 작은순으로 자동 정렬(min heap)
    distances = []  # 먹을 수 있는 물고기 거리들
    while q:
        i, j, distance = q.popleft()
        for di, dj in diff:
            ni, nj = i + di, j + dj
            if -1 < ni < N and -1 < nj < N and (ni, nj) not in visited:
                if space[ni][nj] <= age:
                    q.append((ni, nj, distance + 1))
                    visited.add((ni, nj))
                if 0 < space[ni][nj] < age:
                    heapq.heappush(distances, (distance + 1, ni, nj))
    return distances


N = int(sys.stdin.readline())
age = 2
time = 0
count = 0
space = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
diff = [(-1, 0), (0, -1), (0, 1), (1, 0)]
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            ci, cj = i, j
            space[i][j] = 0
while True:
    distances = bfs(ci, cj)
    if len(distances) == 0:
        break
    shortest_distance, ci, cj = distances[0]
    space[ci][cj] = 0
    time += shortest_distance
    count += 1
    if count == age:
        age += 1
        count = 0
print(time)
