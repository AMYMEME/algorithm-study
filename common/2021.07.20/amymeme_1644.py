# https://www.acmicpc.net/problem/1644
# 소수의 연속합

import sys


def get_prime_list(n):
    # https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
    sieve = [True] * (n + 1)
    for i in range(2, int(n ** .5) + 1):
        if sieve[i]:  # i가 소수인 경우
            for j in range(i + i, n + 1, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return [x for x in range(2, n + 1) if sieve[x]]


N = int(sys.stdin.readline())
prime_list = get_prime_list(N)
if not prime_list:
    print(0)
    exit(0)

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
