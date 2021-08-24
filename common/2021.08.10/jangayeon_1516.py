#문제 : https://www.acmicpc.net/problem/1516

import sys
from collections import defaultdict, deque
input = sys.stdin.readline
 
N = int(input()) #건물 몇 개
que = deque() #큐
indeg_ = [0]*(N+1)
arr = [[0]*(N+1) for _ in range(N+1)] #건물과 재료 건물 관계 배열
time = [0]*(N+1) #가장 오래 걸리는 시간 저장 배열
 
for i in range(1, N+1): #건물과 재료 건물 관계 입력 받음
    _input = list(map(int, input().split()))
    time[i] = _input[0]
    for x in _input[1:-1]:
        arr[i][x] = 1 
        indeg_ [i] += 1
 
for i in range(1, N+1): 
    if indeg_ [i] == 0: #진입차수가 0인 경우 enque
        que.append(i)
 
while que:
    x = que.popleft() #진입차수가 0인 빌딜을 빼내며
    t = 0
    for i in range(1, N+1):
        if arr[i][x] == 1: #이 빌딜이 서로 위상 관계에 있음(관계)
            indeg_ [i] -= 1 #지어진 것이니 진입차수 -1
            if indeg_ [i] == 0: #진입차수 -1 하고 0 되면 재료가 되는 것들이 이미 만들어 진 것
                que.append(i)
        if arr[x][i] == 1:#(시간)
            t = max(time[i], t)#같은 차수에 있는 것들 중에 가장 오래 걸리는 시간 구하고
    time[x] += t #갱신
 
for i in time[1:]:
    print(i)

