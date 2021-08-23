# https://www.acmicpc.net/problem/6549
# 히스토그램에서 가장 큰 직사각형

import sys
from collections import defaultdict


def solution(l):
    N = l[0]
    connect = defaultdict(int)
    dp = [l[1]]
    connect[l[1]] += 1

    for idx, h in enumerate(l[2:], start=2):
        before = l[idx - 1]
        connect[h] += 1

        if before > h:  # 작아진 경우
            if connect[h] == 1:
                connect[h] += 1
            for k, _ in filter(lambda x: x[0] > h, connect.items()):
                connect[k] = 0
            dp.append(max(dp[-1], connect[h] * h))

        elif before <= h:  # 커진 경우
            before_max = 0
            for k, _ in filter(lambda x: x[1], connect.items()):
                if k != h:
                    connect[k] += 1
                before_max = max(before_max, connect[k] * k)
            dp.append(max(dp[-1], before_max))
    return dp[-1]


while True:
    row = list(map(int, sys.stdin.readline().split()))
    if row == [0]:
        break
    print(solution(row))
