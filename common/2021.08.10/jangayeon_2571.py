#문제  : https://www.acmicpc.net/problem/2571

import sys

arr = [[0] * 100 for _ in range(100)] #색종이 도화지에 붙인 상태 변수 선언
N = int(sys.stdin.readline()) #색종이 갯수
for _ in range(N):
    width, height = map(int, sys.stdin.readline().split()) #왼쪽 변 거리, 아래쪽 변 거리
    for i in range(10): #도화지 붙이기
        for j in range(10):
            arr[width+i][height+j] = 1

for x in range(100): #전체 돌며 
    for y in range(100):
        if arr[x][y]: #해당 부분인 1이면
            arr[x][y] += arr[x - 1][y] #각 줄의 높이 구하기


ans = 0
for x in range(100):
    for y in range(100):
        height = 100 #최대 높이로 임시로 설정
        for z in range(y, 100): #시작 위치부터 체크해서 가장 낮은 높이 구하기
            height = min(height, arr[x][z]) #가장 작은 값으로 갱신
            ans = max(ans, height * (z - y + 1))
print(ans)