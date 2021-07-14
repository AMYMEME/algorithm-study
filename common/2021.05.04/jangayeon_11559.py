#문제 https://www.acmicpc.net/problem/11559


from collections import deque



def BFS(x, y,color): #터질 뿌요 탐색
    colors=set()
    que=deque()
    que.append((x,y))

    while que:
        node = que.popleft()
        if node in colors: continue
        colors.add(node)
        for i in range(4):
            nx, ny = node[0]+dx[i], node[1]+dy[i]
            if not(0<=nx<n and 0<=ny<m): continue
            if board[nx][ny] == color:
                que.append((nx, ny))
    return colors


def down():
    for y in range(m):
        for x in range(n-1, -1, -1):
            if board[x][y] == '.': continue
            for k in range(n-1, x, -1):
                if board[k][y] == '.':
                    board[k][y] = board[x][y]
                    board[x][y] = '.'



anv = 0
n, m = 12, 6
board = [list(input().strip()) for _ in range(n)]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

while(1):
    check = 0
    for i in range(n-1, -1, -1):
        for j in range(m):
            if board[i][j] == '.': continue
            array = BFS(i, j, board[i][j])
            if len(array) >= 4:
                if check == 0: check = 1
                for x, y in array:
                    board[x][y] = '.'
    down()
    if check == 1: anv = anv + 1
    elif check == 0: break
print(anv)


