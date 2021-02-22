# https://www.acmicpc.net/problem/11000
# 백준 11000 - 강의실 배정

import sys
import heapq

N = int(sys.stdin.readline())
timetables = []
rooms_end_time = []

for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    heapq.heappush(timetables, (S, T))

while timetables:
    lecture = heapq.heappop(timetables)
    if not rooms_end_time:
        heapq.heappush(rooms_end_time, lecture[1])
    else:
        if rooms_end_time[0] > lecture[0]:
            heapq.heappush(rooms_end_time, lecture[1])
        else:
            heapq.heappop(rooms_end_time)
            heapq.heappush(rooms_end_time, lecture[1])
print(len(rooms_end_time))
