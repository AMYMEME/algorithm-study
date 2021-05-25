# https://www.acmicpc.net/problem/13913

from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(dist_time[x]+1):\
        temp = route[temp]
        arr.append(temp)
        #담아논 이전까지의 경로
    print(' '.join(map(str,  arr[::-1])))

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K: #동생 위치 도달
            print(dist_time[x]) #걸린 시간 출력
            path(x)
            return x
        for i in (x+1, x-1, 2*x): #이동하는 경우의 수 : 전진, 후진, 순간이동
            if 0<=i<=100000 and dist_time[i]==0:
                q.append(i)
                dist_time[i] = dist_time[x] + 1
                route[i] = x

N, K = map(int, input().split())
dist_time = [0]*100001
route = [0]*100001
bfs()
