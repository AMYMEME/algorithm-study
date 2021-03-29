# https://www.acmicpc.net/problem/17822
# 백준 17822 - 원판 돌리기

import sys
from collections import deque


def turn(x, d, k):
    global turn_plates
    plate_idx = x
    direction = -1 if d else 1
    while plate_idx <= N:
        turn_plates[plate_idx - 1].rotate(direction * k)
        plate_idx += x


def bfs(i, j):
    global check
    q = deque([(i, j)])
    visited = {(i, j)}
    check[i][j] = True
    while q:
        ci, cj = q.popleft()
        value = turn_plates[ci][cj]
        for di, dj in diff:
            ni = ci + di
            nj = cj + dj
            if -1 < ni < N and -2 < nj < M + 1:
                if nj == -1:
                    nj = M - 1
                if nj == M:
                    nj = 0
                if (ni, nj) in visited:
                    continue
                if turn_plates[ni][nj] == value:
                    q.append((ni, nj))
                    visited.add((ni, nj))
                    check[ni][nj] = True
    return visited


def sum_number():
    total_sum = 0
    number_count = 0
    for plate in turn_plates:
        for number in plate:
            if number > 0:
                total_sum += number
                number_count += 1
    return total_sum, number_count


def fix_number():
    global turn_plates
    total_sum, number_count = sum_number()
    avg = total_sum / number_count
    for _i in range(N):
        for _j in range(M):
            if turn_plates[_i][_j] < 0:
                continue
            if turn_plates[_i][_j] > avg:
                turn_plates[_i][_j] -= 1
            elif turn_plates[_i][_j] < avg:
                turn_plates[_i][_j] += 1


def remove_number(idx_set):
    global turn_plates
    for _i, _j in idx_set:
        turn_plates[_i][_j] = -1  # remove flag


diff = [(0, 1), (1, 0), (-1, 0), (0, -1)]
N, M, T = map(int, sys.stdin.readline().split())
turn_plates = [deque(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [[False] * M for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, sys.stdin.readline().split())
    turn(x, d, k)
    _, number_count = sum_number()
    if not number_count:
        break
    check = [[False] * M for _ in range(N)]
    adj_exist = False
    for i in range(N):
        for j in range(M):
            if not check[i][j] and turn_plates[i][j] > 0:
                result = bfs(i, j)
                if len(result) == 1:
                    continue
                adj_exist = True
                remove_number(result)
    if not adj_exist:
        fix_number()
print(sum_number()[0])
