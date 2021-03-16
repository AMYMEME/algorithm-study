# https://www.acmicpc.net/problem/4256
# 백준 4256 - 트리

import sys


def postorder(_preorder, _inorder):
    root_value = _preorder[0]
    root_next_idx = _inorder.index(root_value) + 1

    if root_next_idx > 1:
        postorder(_preorder[1:root_next_idx], _inorder[:root_next_idx-1])
    if root_next_idx < len(_preorder):
        postorder(_preorder[root_next_idx:], _inorder[root_next_idx:])
    print(root_value, end=' ')


T = int(sys.stdin.readline())
for _ in range(T):
    print()
    _ = int(sys.stdin.readline())
    preorder = list(sys.stdin.readline().split())
    inorder = list(sys.stdin.readline().split())
    postorder(preorder, inorder)