#문제 : https://www.acmicpc.net/problem/1520

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x == m-1 and y == n-1: #맨 오른쪽 하단인 경우
        return 1
    if dp[x][y] == -1: #방문하지 않은 경우
        dp[x][y] = 0 #0으로 만들고 dfs+dp 실행
        for i in range(4):
            nx = x + dx[i] #상하좌우 이동
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n: #이동해도 범위 내 존재함
                if arr[x][y] > arr[nx][ny]: #내리막길인 경우
                    dp[x][y] += dfs(nx, ny)  #경로 추가 (경우의 수 추가)
    return dp[x][y]
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[-1] * n for i in range(m)] #방문여부/경우의 수 확인
print(dfs(0, 0))