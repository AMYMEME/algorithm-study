# https://www.acmicpc.net/problem/11047
# 백준 11047 - 동전 0
import sys

N, K = map(int, sys.stdin.readline().split())
values = [int(sys.stdin.readline().strip()) for _ in range(N)]
total_count = 0

for value in values[::-1]:
    if K == 0:
        break
    if value > K:
        continue
    count = K // value
    K -= count * value
    total_count += count

print(total_count)