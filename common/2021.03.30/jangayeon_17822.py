#https://www.acmicpc.net/problem/17822

from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0] #오른쪽 왼쪽 위 아래
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    xcnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4): #인접한 영역 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            #원으로 구현
            if ny < 0: 
                ny = m-1 #앞으로 범위 넘어가면 맨 뒤로 이어줌
            elif ny > m-1: #뒤로 범위 넘어가면 맨 앞으로 이어줌
                ny = 0

            if 0 <= nx < n and 0 <= ny < m and not c[nx][ny]: #모두 범위 내에 있고 방문X
                if a[x][y] == a[nx][ny]: #수가 같음
                    c[nx][ny] = 1 #방문 표시 
                    q.append([nx, ny]) #지우는 것들에 넣음
                    xcnt += 1 #지우는 숫자 갯수 증가

    return xcnt #지운 갯수 반환

n, m, t = map(int, input().split()) #원판 갯수, 한 판의 정수 갯수, 회전수

a, nsum, nm = [], 0, n*m #원판 숫자 배열, 원판 숫자 합, 원판 숫자 개수
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    nsum += sum(row)

q = deque() #원판 회전 구현 위해 depue 사용 - 
c = [[0]*m for _ in range(n)] #방문 체크 배열

for _ in range(t): #원판 회전 실시
    x, d, k = map(int, input().split()) #_번째 회전할 때 x배수 원판, d방향, k칸 이동

    k %= m #원이니까 원판 한 개의 숫자 갯수 만큼 나누기 
    for i in range(x-1, n, x):
        if d == 0: #시계방향
            a[i] = a[i][-k:] + a[i][:-k]
            c[i] = c[i][-k:] + c[i][:-k]
        else: #반시계 방향
            a[i] = a[i][k:] + a[i][:k]
            c[i] = c[i][k:] + c[i][:k]

    flag = 0
    for i in range(n):
        for j in range(m):
            if not c[i][j]: #아직 방문 안한 경우
                cnt = bfs(i, j)
                if cnt: #지운 숫자가 있으니
                    nsum -= a[i][j] * cnt #전체 원판 숫자의 합에서 빼기
                    nm -= cnt #전체 원판 숫자의 갯수에서 빼기
                    flag = 1 #인접하면서 같은 숫자 있어서 해당 처리 작업 했음

    if nm == 0: #원판에 남은 숫자가 한개도 없는 경우 
        #-> 평균 계산 시 0으로 나누는 경우 처리
        print(0)
        sys.exit()

    if not flag: #지운 숫자가 없는 경우
        avg = nsum / nm #평균 구해서
        for i in range(n):
            for j in range(m):
                if not c[i][j]:
                    if a[i][j] > avg: #평균 보다 큰 수에 -1
                        a[i][j] -= 1
                        nsum -= 1
                    elif a[i][j] < avg: #평균 보다 작은 수에 +1
                        a[i][j] += 1
                        nsum += 1
print(nsum)