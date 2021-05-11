"""
https://www.acmicpc.net/problem/1806
"""
import sys

N, S = map(int, sys.stdin.readline().split())
sequences = list(map(int, sys.stdin.readline().split()))

start = 0
end = 1
answer = sys.maxsize  # 길이
temp = sequences[0]  # 부분합을 저장 (리스트슬라이싱으로하면 시간초과)

# 투포인터
'''
start=0에서 조건만족하는 최소길이 찾고
start=1로 이동 이때 temp값에서 sequ[0]을 뺌=a값 그리고 다시 end 증가하면서 탐색
=> 이중 for문으로 돌리면 end가 a값이 될 때까지 탐색하는 시간소요
...계속 같은 방법으로
'''
while end <= N:  # end값이 범위 이내일 경우
    if temp >= S:
        answer = min(answer, end - start)  # 최소길이찾기
        temp -= sequences[start]
        start += 1
    else:
        if end < N:
            temp += sequences[end]
        end += 1

if answer == sys.maxsize:
    answer = 0

print(answer)
