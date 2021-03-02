'''
https://www.acmicpc.net/problem/11000
'''
import sys
import heapq

N=int(sys.stdin.readline().strip())
lecture=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
lecture.sort()

end_time=[0]
for s,t in lecture:
    if end_time[0]<=s:
        heapq.heappop(end_time)
    heapq.heappush(end_time,t)

print(len(end_time))