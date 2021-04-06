#https://www.acmicpc.net/problem/16234


import sys
sys.setrecursionlimit(100000) 
'''
#Maximum recursion depth exceed
이 코드에서 재귀의 깊이는 약 2500이 될 수 있습니다. 
하지만 파이썬3에는 기본 재귀 제한이 있고 이게 약 1000회 정도입니다. 
파이파이3는 이보다 재귀 제한이 더 높아서 통과되는 것으로 보입니다. 
파이썬3로 통과하려면 아래와 같은 코드를 상단에 추가하면 됩니다.
'''

N, L, R = map(int, input().split())
lists = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnt = 0


def go(x, y):
    for i in range(4):
        _x = x + dx[i]
        _y = y + dy[i]

        if 0 <= _x < N and 0 <= _y < N and visited[_x][_y]:
            tmp = abs(lists[x][y] - lists[_x][_y])
            if L <= tmp <= R:
                visited[_x][_y] = False
                combine.append([_x, _y])
                go(_x, _y)


while True:
    visited = [[True] *N for _ in range(N)]
    flag = True
    for i in range(N):
        for j in range(N):
            combine = []

            if visited[i][j]:
                combine.append([i, j])
                visited[i][j] = False
                go(i, j)

                if len(combine) > 1:
                    flag = False
                    avg = int(sum([lists[x][y] for x, y in combine]) // len(combine))
                    for x, y in combine:
                        lists[x][y] = avg

    if flag:
        break

    cnt += 1

print(cnt)
