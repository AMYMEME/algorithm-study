# 백준 #19640
# https://www.acmicpc.net/problem/19640

import heapq
import sys
from itertools import repeat

N, M, K = map(int, sys.stdin.readline().split())
lines = [[] for i in repeat(None, M)]
count = 0

for original_turn in range(N):
    D, H = map(int, sys.stdin.readline().split())
    lines[original_turn % M].append((D, H, original_turn % M, original_turn))

head = []

for line in lines:
    if line:
        heapq.heappush(head, ((-line[0][0], -line[0][1], line[0][2]), line[0][3]))

while head:
    now_turn = heapq.heappop(head)
    lines[now_turn[0][2]].pop(0)
    if now_turn[1] == K:
        break
    if lines[now_turn[0][2]]:
        next_turn = lines[now_turn[0][2]][0]
        heapq.heappush(head, ((-next_turn[0], -next_turn[1], next_turn[2]), next_turn[3]))
    count += 1
print(count)
