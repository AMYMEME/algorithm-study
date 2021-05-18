"""
https://www.acmicpc.net/problem/11559
"""
import sys
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(start):
    color = board[start[0]][start[1]]
    visit = set()
    visit.add(start)
    q = deque()
    q.append(start)
    while q:
        cx, cy = q.popleft()
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < 12 and 0 <= ny < 6 and (nx, ny) not in visit:
                if board[nx][ny] == color:
                    visit.add((nx, ny))
                    q.append((nx, ny))
    if len(visit) >= 4:
        for vx, vy in visit:
            board[vx][vy] = "."
        return True
    else:
        return False


def play():
    count = 0
    while True:
        flag=False
        for x in range(12):
            for y in range(6):
                if board[x][y] != ".":
                    if bfs((x, y)):
                        flag=True
        if not flag:
            break

        count += 1
        for j in range(6):
            for i in range(10, -1, -1):
                if board[i][j]==".": continue
                for k in range(11,i,-1):
                    if board[k][j] == ".":
                        board[k][j] = board[i][j]
                        board[i][j] = "."

    return count


board = []
for _ in range(12):
    board.append(list(sys.stdin.readline().strip()))

print(play())
