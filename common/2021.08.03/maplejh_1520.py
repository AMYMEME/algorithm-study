# https://www.acmicpc.net/problem/1520
import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    if x == M - 1 and y == N - 1:  # 맨끝까지 간 경우
        return 1
    if dp[x][y] != -1:  # 값이 이미 있는 경우 (탐색한 경우)
        return dp[x][y]
    dp[x][y] = 0  # 탐색한다고 표시
    for dx, dy in d:  # 상하좌우 탐색
        nx = x + dx
        ny = y + dy
        if -1 < nx < M and -1 < ny < N:
            if board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
M, N = map(int, sys.stdin.readline().split())
board = []
dp = [[-1] * N for _ in range(M)]

for _ in range(M):
    board.append(list(map(int, sys.stdin.readline().split())))

h = dfs(0, 0)
print(h)
