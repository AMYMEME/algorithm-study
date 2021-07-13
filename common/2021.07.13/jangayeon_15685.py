#문제: https://www.acmicpc.net/problem/15685


import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1] #위아래 좌우 이동
dy = [1, 0, -1, 0]
n = int(input()) #드래곤 커브 갯수
plane = [[0] * 101 for i in range(101)] #드래곤 커브 그릴/담을 부분
for i in range(n): #시작점(x), 시작점(y), 방향, 세대 입력 받음
    y, x, d, g = map(int, input().split())
    plane[x][y] = 1
    temp = [d] #(이전 세대 숫자 표현 넣을 거임)
    q = [d] #초기 방향
    for _ in range(g + 1): #0세대~>g세대까지 만들기 
        for k in q:
            x += dx[k]
            y += dy[k]
            plane[x][y] = 1
        #이전 세대의 뒤에서부터 꺼내면서 +1 해주기
        q = [(i + 1) % 4 for i in temp] 
        q.reverse()
        temp += q
#사각형 갯수 구하기        
cnt = 0
for i in range(100): #100*100 돌며 단순 탐색
        for j in range(100):
            #인접한 4칸의 정사각형이 모두 드래곤에 속함
            if plane[i][j] and plane[i][j + 1] and plane[i + 1][j] and plane[i + 1][j + 1]:
                cnt += 1 #갯수 증가
print(cnt)