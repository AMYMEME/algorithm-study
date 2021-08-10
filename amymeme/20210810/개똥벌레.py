# https://www.acmicpc.net/problem/3020
# 개똥벌레

from collections import defaultdict
import sys

N, H = map(int, sys.stdin.readline().split())
bottom = defaultdict(int)
top = defaultdict(int)
hurdle = 0

for i in range(N):
    if i % 2 == 0:
        bottom[int(sys.stdin.readline())] += 1
        hurdle += 1
    else:
        top[H - int(sys.stdin.readline())] += 1
min_value = hurdle
count = 1
for h in range(1, H):
    hurdle -= bottom[h]
    hurdle += top[h]
    if hurdle == min_value:
        count += 1
    elif hurdle < min_value:
        min_value = hurdle
        count = 1
print(min_value, count)
