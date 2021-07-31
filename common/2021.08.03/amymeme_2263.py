# https://www.acmicpc.net/problem/2263
# 트리의 순회

import sys


def start(inorder, postorder):
    global pre_order
    root_value = postorder.pop()
    pre_order.append(root_value)
    left_count = 0

    for idx, value in enumerate(inorder):
        if value == root_value:
            left_count = idx
            break

    if left_count > 0:  # left exist
        start(inorder[:left_count], postorder[:left_count])

    if left_count < len(inorder) - 1:
        start(inorder[left_count + 1:], postorder[left_count:])


sys.setrecursionlimit(10 ** 5)
n = int(sys.stdin.readline())
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))
pre_order = []
start(in_order, post_order)
print(*pre_order, sep=' ')
