n = int(input())
board=[[0]*101 for _ in range(101)]
xd=[1,0,-1,0]
yd=[0,-1,0,1]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    direction_info=[d]
    #세대별 방향 규칙 찾기
    for _ in range(g):
        direction_info+=[(i+1)%4 for i in direction_info[::-1]]
    board[x][y]=1
    for i in direction_info:
        nx=xd[i]+x
        ny=yd[i]+y
        board[nx][ny]=1
        x, y = nx, ny

ans=0
for i in range(100):
    for j in range(100):
        if board[i][j]==1:
            if board[i+1][j]==1 and board[i+1][j+1]==1 and board[i][j+1]==1:
                ans+=1
print(ans)


