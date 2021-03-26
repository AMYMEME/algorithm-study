# 문제 : https://www.acmicpc.net/problem/17829

import sys

input=sys.stdin.readline

def pooling(array,n):
    if n==1:
        return array[0][0]
    else:
        new_=[[] for _ in range(n//2)]
        for i in range(0,n,2):
            for j in range(0,n,2):
                new_[i//2].append(sorted([array[i][j],array[i+1][j],array[i][j+1],array[i+1][j+1]])[2])
        return pooling(new_,n//2)




N=int(input())
array=[list(map(int,input().split())) for _ in range(N)]
print(pooling(array,N))