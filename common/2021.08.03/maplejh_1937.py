# https://www.acmicpc.net/problem/1937
import sys

sys.setrecursionlimit(10 ** 6)
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1  # 첫칸 1
    for dx, dy in d:
        nx = dx + x
        ny = dy + y
        if -1 < nx < n and -1 < ny < n:
            if forest[nx][ny] > forest[x][y]:  # 조건만족
                dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]


n = int(sys.stdin.readline())
forest = []
for _ in range(n):
    forest.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)
