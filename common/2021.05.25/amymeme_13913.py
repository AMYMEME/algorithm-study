# https://www.acmicpc.net/problem/13913
# 숨바꼭질 4

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX_LENGTH = 100001
locations = [(0, 0)] * MAX_LENGTH  # time, the past location
diff = [-1, 1]

q = deque([(N, 0)])  # cur_location, cur_time
locations[N] = (0, -1)  # if not, fail when N == K

while locations[K] == (0, 0):
    cur_location, cur_time = q.popleft()

    for di in diff:
        nxt_location = di + cur_location
        if -1 < nxt_location < MAX_LENGTH:
            if locations[nxt_location] != (0, 0):
                continue
            locations[nxt_location] = (cur_time + 1, cur_location)
            q.append((nxt_location, cur_time + 1))

    nxt_location = cur_location * 2
    if -1 < nxt_location < MAX_LENGTH:
        if locations[nxt_location] != (0, 0):
            continue
        locations[nxt_location] = (cur_time + 1, cur_location)
        q.append((nxt_location, cur_time + 1))

print(locations[K][0])
stack = [K]
past_path = K
while past_path != N:
    past_path = locations[past_path][1]
    stack.append(past_path)
while stack:
    print(stack.pop(), end=' ')
