#문제 :  https://www.acmicpc.net/problem/2263

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def divide(in_start,in_end,post_start,post_end):
    if (post_start>post_end) or (in_start>in_end): #재귀 종료 : 수렴
        return
    
    root=post_[post_end] #후위 순회 마지막은 루트
    print(root,end=' ')

    lt=idx[root]-in_start #중위 순회 루트 기준 왼쪽 : left
    rt=in_end-idx[root] #중위 순회 루트 기준 오른쪽 : rigth

    divide(in_start,in_start+lt-1,post_start,post_start+lt-1) #왼쪽 서브트리
    divide(in_end-rt+1, in_end, post_end-rt, post_end-1) #오른쪽 서브트리


n=int(input())
in_=list(map(int,input().split()))
post_=list(map(int,input().split()))
idx=[0]*(n+1)
for i in range(n): #in-order 값의 index 저장
    idx[in_[i]]=i

divide(0,n-1,0,n-1)