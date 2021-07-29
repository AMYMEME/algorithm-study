#문제: https://www.acmicpc.net/problem/4179

"""
큐 : 불 좌표 -> 사람 좌표
BFS 탐색  : 미로 나가기까지 최소 탐색 횟수
사람은 빈칸으로만 이동 가능
"""

from sys import stdin
from collections import deque
input = stdin.readline

R, C = map(int, input().split())
a = [list(input().strip()) for _ in range(R)]
dist = [[0]*C for _ in range(R)]
q = deque()

for i in range(R):
    for j in range(C):
        if a[i][j] == 'J': #사람 위치
            sx, sy = i, j 
        elif a[i][j] == 'F': #불 위치
            q.append((i, j, 1)) #불부터 enque
            dist[i][j] = 1 #불이 1초만에 갈 수 있는 거리

def bfs():
    q.append((sx, sy, 0)) #사람 원래 위치 (사람 가장 마지막에 enque)
    dist[sx][sy] = 1 #사람이 1초만에 갈 수 있는 거리
    while q: #더이상 탐색할 불과 사람이 없을 때 까지
        x, y, f = q.popleft()
        for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1): #4 방향 탐색
            nx, ny = x+dx, y+dy #이동
            if nx < 0 or nx >= R or ny < 0 or ny >= C: #더이상 이동 불가능한 곳인 경우
                if f: #다른 방향으로 이동
                    continue
                print(dist[x][y])
                return
            if not dist[nx][ny] and a[nx][ny] != '#': #전에 방문한 적 없거나 빈 곳인 경우 도달 가능
                #현재 시간이 정점의 시간보다 빠른 경우 -> 이동가능 
                q.append((nx, ny, f)) #새롭게 도달한 곳 추가
                dist[nx][ny] = dist[x][y]+1 #도달 시간 추가
    print("IMPOSSIBLE")

bfs()

