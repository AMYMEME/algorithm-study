#문제: https://www.acmicpc.net/problem/4179

불 bfs-> 불 bfs 돌린거 적용해서 지훈이 bfs 돌기

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    fqlen = len(fq)
    while fqlen:
        x, y = fq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if a[nx][ny] == '.':
                    a[nx][ny] = 'F'
                    fq.append([nx, ny])
        fqlen -= 1

    qlen = len(q)
    while qlen:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                print(check[x][y])
                return
            else:
                if a[nx][ny] == '.' and not check[nx][ny]:
                    check[nx][ny] = check[x][y] + 1
                    q.append([nx, ny])
        qlen -= 1
        
    if q:
        bfs()
    else:
        print("IMPOSSIBLE")

r, c = map(int, input().split())
check = [[0]*c for _ in range(r)]
a, q, fq = [], deque(), deque()

for i in range(r):
    row = list(input().strip())
    a.append(row)
    for j, key in enumerate(row):
        if key == 'J':
            q.append([i, j])
            check[i][j] = 1
            a[i][j] = '.'
        elif key == 'F':
            check[i][j] = 1
            fq.append([i, j])

bfs()