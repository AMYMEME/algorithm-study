import sys
import heapq

N = int(sys.stdin.readline())
my_min_heap_queue = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if my_min_heap_queue:
            print(heapq.heappop(my_min_heap_queue)[1])
        else:
            print(0)
    else:
        heapq.heappush(my_min_heap_queue, (abs(x), x))
