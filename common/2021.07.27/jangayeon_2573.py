#문제:https://www.acmicpc.net/problem/2573

1년 지남 -> 높이는 상하좌우에 있는 0 갯수만큼 줄어듬
 2개 이상으로 분리 될 때 찾기

 => 연결 요소 2개 이상 될때 시점 찾기
#풀이 참고 : https://kangmin1012.tistory.com/7


"""
아직 방문 X인 것에 대한 bfs 탐색 진행
bfs 탐색 횟수 = 빙하 갯수
큐에 넣는 순간 방문했다고 표시해서 중복으로 탐색 진행되는 것 방지
빙하가 녹는 작업은 입력되었을 때 상하좌우 기준으로 진행
"""


import sys
from collections import deque
def bfs(i,j,visit) :
    que = deque([[i,j]])
    melting_que = deque() # 빙하가 녹는 위치와 녹는 정도를 저장하는 큐
    visit[i][j] = 1
    while que :
        i,j = que.popleft()
        melt_cnt = 0
        for d_x, d_y in direction :
            next_x = i + d_x
            next_y = j + d_y
            if 0 <= next_x <= x-1 and 0 <= next_y <= y-1 and visit[next_x][next_y] == 0:
            # 빙산의 높이가 있고 방문을 안했을 경우 que에 값 넣어주기
                if glacier[next_x][next_y] != 0:
                    visit[next_x][next_y] = 1  # 방문 체크
                    que.append([next_x,next_y])
            # 사방향 탐색 시 0일 경우 melt_cnt 증가
                else :
                    melt_cnt += 1
        if melt_cnt : #녹은 것이 있으면 갱신
            melting_que.append([i,j,melt_cnt])
    return melting_que

input=sys.stdin.readline
year = 0 # 몇 년이 지났는지 판단하는 변수
x, y = map(int,input().split())
glacier = [[int(n) for n in input().split()] for _ in range(x)]
direction = ((1,0),(-1,0),(0,-1),(0,1)) #동서남북
#반복문 종료 조건 -> 빙산의 갯수가 0이거나 2일 경우
while True :
    cnt = 0 # 빙산의 갯수를 담는 cnt 변수
    visit = [[0 for _ in range(y)] for _ in range(x)]  # bfs를 위한 탐색 확인 리스트
    for i in range(x-1) :
        for j in range(y-1) :
            if glacier[i][j] != 0 and visit[i][j] == 0 : #빙하의 높이가 남아있고 방문하지 않을 경우
                cnt += 1 # 빙산의 갯수 추가
                melt = bfs(i,j,visit) # bfs 시작을 하고 각 좌표별로 녹는 정도 반환
                while melt :
                    m_x, m_y, m = melt.popleft()
                    glacier[m_x][m_y] = max(glacier[m_x][m_y]-m, 0)
    if cnt == 0 :
        year = 0
        break
    if cnt >= 2 : #2년 이상으로 분리됨!!
        break
    year += 1  # 일 년 증가
    # 빙산의 갯수가 0이거나 2일 경우 반복문 종료
print(year)