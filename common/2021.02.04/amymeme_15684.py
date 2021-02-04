# https://www.acmicpc.net/problem/15684
# 백준 15684 - 사다리 조작
import sys


def ladder_down(start):
    ci = 0
    cj = start
    while ci < H:
        if original_ladders[ci][cj]:
            cj += 1
        elif cj > 0 and original_ladders[ci][cj - 1]:
            cj -= 1
        ci += 1
    return cj


def game_start():
    for idx in range(N):
        if idx != ladder_down(idx):
            return False
    return True


def dfs(temp_ladder_cnt, ci, cj):
    global result
    global original_ladders
    if result != -1:
        return
    if temp_ladder_cnt == 0:
        if game_start():
            result = count
        return
    for i in range(ci, H):
        for j in range(N - 1):
            if i == ci and j <= cj:
                continue
            if j > 0 and original_ladders[i][j - 1]:
                continue
            if original_ladders[i][j] or original_ladders[i][j + 1]:
                continue
            original_ladders[i][j] = 1
            dfs(temp_ladder_cnt - 1, i, j)
            original_ladders[i][j] = 0


N, M, H = map(int, sys.stdin.readline().split())
original_ladders = [[0] * N for _ in range(H)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    original_ladders[a - 1][b - 1] = 1
result = -1

for count in range(4):
    dfs(count, 0, -1)  # dfs(count, 0, 0)은 왜 틀리는지...
    if result != -1:
        break

print(result)
