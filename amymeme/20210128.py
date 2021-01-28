# https://www.acmicpc.net/problem/16235
# 백준 16235 - 나무 재태크

import sys

diff = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
N, M, K = map(int, sys.stdin.readline().split())
land = [[5] * N for _ in range(N)]
fertilizers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
tree_infos = [[{} for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, sys.stdin.readline().split())
    tree_infos[x - 1][y - 1][z] = 1  # 개수

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if tree_infos[i][j]:
                temp = {}
                dead = 0
                for age in sorted(tree_infos[i][j].keys()):
                    if age * tree_infos[i][j][age] <= land[i][j]:
                        land[i][j] -= age * tree_infos[i][j][age]
                        temp[age + 1] = tree_infos[i][j][age]
                    else:
                        survive = land[i][j] // age
                        if not survive:
                            dead += (age // 2) * tree_infos[i][j][age]
                            continue
                        land[i][j] -= age * survive
                        temp[age + 1] = survive
                        dead += (age // 2) * (tree_infos[i][j][age] - survive)
                tree_infos[i][j] = temp
                land[i][j] += dead
            land[i][j] += fertilizers[i][j]
    for i in range(N):
        for j in range(N):
            if tree_infos[i][j]:
                count = 0
                for age in tree_infos[i][j].keys():
                    if age % 5 == 0:
                        count += tree_infos[i][j][age]
                if count:
                    for dx, dy in diff:
                        nx, ny = i + dx, j + dy
                        if -1 < nx < N and -1 < ny < N:
                            if 1 not in tree_infos[nx][ny].keys():
                                tree_infos[nx][ny][1] = count
                            else:
                                tree_infos[nx][ny][1] += count

count = 0
for i in range(N):
    for j in range(N):
        count += sum(tree_infos[i][j].values())
print(count)
