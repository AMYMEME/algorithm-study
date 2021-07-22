#문제:https://www.acmicpc.net/problem/1644

"""
소수를 위한 에라토스체
https://mygumi.tistory.com/66
"""

import sys
input = sys.stdin.readline
 
N = int(input())
isPrime = [False, False] + [True] * (N - 1)
Seqprime = []
 
for i in range(2, N + 1):
    if isPrime[i]:
        Seqprime.append(i)
        for j in range(2 * i, N + 1, i):
            isPrime[j] = False
 
start = 0
end = 0
sum = 0
ans = 0
 
while(True):
    if sum >= N:
        sum -= Seqprime[start]
        start += 1
    elif end == len(Seqprime):
        break
    else:
        sum += Seqprime[end]
        end += 1
 
    if sum == N:
        ans += 1
 
print(ans)