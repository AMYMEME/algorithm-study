import sys

N, S = map(int, sys.stdin.readline().split())
series = list(map(int, sys.stdin.readline().split()))
answer = N


left = 0
while left < N:
    right = left
    #TODO : sum 대신 앞 더하고 뒤 빼기
    while S >= sum(series[left:right+1]) and right < N:
        right += 1
    if S > sum(series[left:right+1]):
        break
    if answer > right - left + 1:
        answer = right - left + 1
    left += 1
print(answer)