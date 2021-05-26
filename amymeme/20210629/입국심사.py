# https://programmers.co.kr/learn/courses/30/lessons/43238
# 입국심사
import heapq


def solution(n, times):
    times = list(map(lambda x: (x, x), times))
    heapq.heapify(times)
    while n:
        shortest_wait_time, original_time = heapq.heappop(times)
        n -= 1
        heapq.heappush(times, (shortest_wait_time + original_time, original_time))
    return shortest_wait_time