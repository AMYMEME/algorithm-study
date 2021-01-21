import heapq
from sys import stdin

result = []
abs_heap = []
num = int(stdin.readline())

for _ in range(num):
    x = int(stdin.readline())
    if (x != 0):
        heapq.heappush(abs_heap, (abs(x), x))
    else:
        if abs_heap:
            result.append(str(heapq.heappop(abs_heap)[1]))
        else:
            result.append("0")

print("\n".join(result))
