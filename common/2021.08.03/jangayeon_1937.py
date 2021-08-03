#문제 : https://www.acmicpc.net/problem/1937

from sys import setrecursionlimit 
setrecursionlimit(10**9)

def dfs(i, j): 
    if visit[i][j] < 0: #해당 지점 한 번도 방문 X
        visit[i][j] = 0 #지금 방문함
        for d in range(4): #상하좌우 참색
            x = i+dx[d]
            y = j+dy[d] 
            if 0<=x<n and 0<=y<n and bamboo[i][j] < bamboo[x][y]: 
                # 범위 내 & 현재보다 더 많은 대나무 있는 경우
                visit[i][j] = max(visit[i][j], dfs(x, y)) 
                #상하좌우 중 가장 긴 생존 일 갱신
        visit[i][j] += 1 
    return visit[i][j] 
    
n = int(input()) 
bamboo = [list(map(int, input().split())) for _ in range(n)] 
visit = [[-1] * n for _ in range(n)] 
dx= [-1, 1, 0, 0]
dy=[0, 0, -1, 1]
ans = 0 
for i in range(n): 
    for j in range(n): 
        ans = max(ans, dfs(i, j)) 
print(ans)

