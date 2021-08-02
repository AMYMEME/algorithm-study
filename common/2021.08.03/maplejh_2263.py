# https://www.acmicpc.net/problem/2263
import sys


def preorder(postorder, inorder):
    root = postorder[-1]
    loc = inorder.index(root)  # root 위치 - 트리 나누기
    left = inorder[:loc]
    right = inorder[loc + 1:]
    answer.append(root)
    if postorder[:loc]:
        preorder(postorder[:loc], left)
    if postorder[loc:-1]:
        preorder(postorder[loc:-1], right)


n = int(sys.stdin.readline())
i = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))
answer = []
preorder(p, i)
print(*answer)
