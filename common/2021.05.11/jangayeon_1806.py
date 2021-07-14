#문제 : https://www.acmicpc.net/problem/1806

import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start, end, sum = 0, 0, 0 #시작 부분, 끝 부분, 시작 ~ 끝 부분 함
min_ = 100001

while True:
    # 현재 부분 합 > = s 
    if sum >= S:
        sum -= arr[start]   # 앞에서 원소 한 개 삭제 : start의 위치 1 증가
        start += 1
        min_ = min(min_, end - start + 1)   # 가장 작은 길이의 부분 합 : start~end까지가 현재 최소값보다 작으면 최소값 갱신
  
    elif end == N:    # end=N되면 탐색 종료
        break
    else: # 현재 부분 합 < s 
        sum += arr[end]     # 뒤로 원소 1개 추가 : end 위치 1 증가
        end += 1

if min_ == 100001:  # 초기 min값과 같다면 sum이 S를 넘지 못한 것
    min_ = 0
print(min_)