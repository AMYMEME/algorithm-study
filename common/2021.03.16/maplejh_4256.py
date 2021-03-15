'''
https://www.acmicpc.net/problem/4256
'''
import sys

def postorder(preorder,inorder):
    root=preorder[0]
    root_i=inorder.index(root)
    left=inorder[:root_i]
    if preorder[1:root_i+1]:
        postorder(preorder[1:root_i+1],left)
    right=inorder[root_i+1:]
    if preorder[root_i+1:]:
        postorder(preorder[root_i+1:],right)
    answer.append(root)

T=int(sys.stdin.readline())

for _ in range(T):
    answer=[]
    n=int(sys.stdin.readline())
    preorder=list(map(int,sys.stdin.readline().split()))
    inorder=list(map(int,sys.stdin.readline().split()))
    postorder(preorder,inorder)
    print(*answer)