import sys

N, S = map(int, sys.stdin.readline().split())
series = list(map(int, sys.stdin.readline().split()))
answer = N + 1

left = 0
right = 0
_sum = 0

while right <= N:
    if _sum < S:
        if right == N:
            break
        _sum += series[right]
        right += 1
        continue
    _sum -= series[left]
    left += 1
    answer = min(answer, right - left + 1)

if answer == N + 1:
    print(0)
else:
    print(answer)
