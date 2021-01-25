import heapq
import sys


def spring_and_summer():
    next_tree_infos = []
    dead_trees = []
    while tree_infos:
        x, y, z = heapq.heappop(tree_infos)
        if land[x][y] >= z:
            land[x][y] -= z
            heapq.heappush(next_tree_infos, (x, y, z + 1))
        else:
            dead_trees.append((x, y, z))

    for x, y, z in dead_trees:
        land[x][y] += (z // 2)
    return next_tree_infos


def autumn():
    tmp = []
    while tree_infos:
        x, y, z = heapq.heappop(tree_infos)
        heapq.heappush(tmp, (x, y, z))
        if z % 5 != 0:
            continue
        for i in range(8):
            near_x, near_y = x + dx[i], y + dy[i]
            if -1 < near_x < N and -1 < near_y < N:
                heapq.heappush(tmp, (near_x, near_y, 1))
    return tmp


def winter():
    return [[land[i][j] + fertilizers[i][j] for j in range(N)] for i in range(N)]


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
N, M, K = map(int, sys.stdin.readline().split())
land = [[5] * N for _ in range(N)]
fertilizers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tree_infos = []
for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    heapq.heappush(tree_infos, (x - 1, y - 1, z))

for _ in range(K):
    tree_infos = spring_and_summer()
    tree_infos = autumn()
    land = winter()
print(len(tree_infos))
