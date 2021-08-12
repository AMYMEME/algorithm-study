
#문제 : https://www.acmicpc.net/problem/4485

import sys
import heapq
input = sys.stdin.readline
max_num=sys.maxsize

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

test = 1 #풀어낸 테스트 케이스 수
while True:
    N = int(input()) #동굴 크기
    if N == 0: #없음
        break
    map_ = [] #맵 입력 받기
    for _ in range(N):
        map_.append(list(map(int, input().split())))
    mon = [[max_num]*N for _ in range(N)] #각 칸의 동굴에 대한 잃은 루피갯수
    visited = [[False]*N for _ in range(N)] #방문 배열
    queue = [[map_[0][0], 0,0]] #시작 상태 enque
 
    while queue:
        w, x, y = heapq.heappop(queue) #현재 잃은 루피, x좌표, y좌표
        for i in range(4):#상하좌우 돌기
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and mon[nx][ny] > w + map_[nx][ny]:
                #범위 내 & 아직 방문 X & 잃는 루피가 더 적은 경우
                mon[nx][ny] = w + map_[nx][ny] #잃은 루피 정보 갱신
                visited[nx][ny] = True #방문으로 바꿔주기
                heapq.heappush(queue, [mon[nx][ny], nx, ny]) #방문한 곳 위치 enque
                
                
    print("test {0}: {1}".format(test, mon[N-1][N-1])) #갱신을 모두 거쳐 계산한 최소의 잃은 루피 수
    test += 1 #풀은 테스트 케이스 +1