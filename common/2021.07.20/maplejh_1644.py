# https://www.acmicpc.net/problem/1644
import sys

N = int(sys.stdin.readline())

# 소수 찾기
prime = []
arr = [0, 0] + [1] * (N - 1)
for i in range(2, int(N ** 0.5) + 1):
    if not arr[i]:
        continue
    for j in range(2, N // i + 1):
        arr[i * j] = 0
prime=[k for k in range(N+1) if arr[k]]

# 연속합 찾기
answer = 0
left, right = 0, 0
temp = 0
while right <= len(prime):
    if temp >= N:
        if temp == N:
            answer += 1
        temp -= prime[left]
        left += 1
    else:
        if right < len(prime):
            temp += prime[right]
        right += 1
print(answer)
