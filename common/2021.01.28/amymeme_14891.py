# https://www.acmicpc.net/problem/14891
# 백준 14891 - 톱니바퀴

import sys
from collections import deque

gears = [deque(map(int, sys.stdin.readline().strip())) for _ in range(4)]


def dfs_right(current_gear_num, before_rotate_gear, original_direction):
    if current_gear_num < 3 and before_rotate_gear[2] != gears[current_gear_num + 1][-2]:
        dfs_right(current_gear_num + 1, gears[current_gear_num + 1], -original_direction)
        gears[current_gear_num + 1].rotate(-original_direction)


def dfs_left(current_gear_num, before_rotate_gear, original_direction):
    if current_gear_num > 0 and before_rotate_gear[-2] != gears[current_gear_num - 1][2]:
        dfs_left(current_gear_num - 1, gears[current_gear_num - 1], -original_direction)
        gears[current_gear_num - 1].rotate(-original_direction)


K = int(sys.stdin.readline().strip())
for _ in range(K):
    gear_num, direction = map(int, sys.stdin.readline().split())
    gear_num -= 1  # for list index
    dfs_right(gear_num, gears[gear_num], direction)
    dfs_left(gear_num, gears[gear_num], direction)
    gears[gear_num].rotate(direction)

score = 0
if gears[0][0] == 1: score += 1
if gears[1][0] == 1: score += 2
if gears[2][0] == 1: score += 4
if gears[3][0] == 1: score += 8
print(score)