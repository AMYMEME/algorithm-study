# https://www.acmicpc.net/problem/1644
# 소수의 연속합

import sys
import math

N = int(sys.stdin.readline())
if N == 1:
    print(0)
    exit(0)
prime_list = []
for i in range(2, N + 1):
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(i)

# initialize
left = 0
local_sum = prime_list[0]
right = 0
length = len(prime_list)
match_count = 0

while left < length:
    while right < length - 1:
        if local_sum + prime_list[right + 1] > N:
            break
        right += 1
        local_sum += prime_list[right]
    if local_sum == N:
        match_count += 1
    local_sum -= prime_list[left]
    left += 1
print(match_count)
