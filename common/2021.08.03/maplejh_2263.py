# https://www.acmicpc.net/problem/2263
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 9)


def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = postorder[post_end]
    loc = idx[root]  # root 위치 - 트리 나누기
    left_len = loc - in_start  # root를 기준으로 inorder에서 왼쪽
    right_len = in_end - loc  # root를 기준으로 inorder에서 오른쪽
    answer.append(root)
    preorder(in_start, loc - 1, post_start, post_start + left_len - 1)
    preorder(loc + 1, in_end, post_end - right_len, post_end - 1)


n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
idx = defaultdict(int)
for k in range(n):
    idx[inorder[k]] = k

answer = []
preorder(0, n - 1, 0, n - 1)
print(*answer)
