# https://www.acmicpc.net/problem/2263
# 트리의 순회

import sys
from collections import defaultdict


def start(in_left, in_right, post_left, post_right):
    global pre_order
    root_value = post_order[post_right]
    pre_order.append(root_value)
    index = in_order_dict[root_value]

    if in_left < index:
        left_cnt = index - 1 - in_left
        start(in_left, in_left + left_cnt, post_left, post_left + left_cnt)

    if index < in_right:
        right_cnt = in_right - index - 1
        start(index + 1, index + 1 + right_cnt, post_right - 1 - right_cnt, post_right - 1)


sys.setrecursionlimit(10 ** 5)
n = int(sys.stdin.readline())
in_order_dict = defaultdict(int)
in_order = list(map(int, sys.stdin.readline().split()))
for idx, value in enumerate(in_order):
    in_order_dict[value] = idx
post_order = list(map(int, sys.stdin.readline().split()))
pre_order = []
start(0, n - 1, 0, n - 1)
print(*pre_order, sep=' ')
