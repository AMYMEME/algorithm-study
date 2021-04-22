"""
https://www.acmicpc.net/problem/10830
"""

import sys
from copy import deepcopy


def multiplication(a, b):
    result = []
    for col in a:
        temp = []
        for row in zip(*b):
            temp.append(sum(x * y for x, y in zip(col, row)) % 1000)
        result.append(temp)

    return result


n, b = map(int, sys.stdin.readline().split())
b = list(map(int, (format(b, 'b'))))  # 이진수로

a = []
for _ in range(n):
    a.append([*map(lambda x: x % 1000, (map(int, sys.stdin.readline().split())))])

c = deepcopy(a)
for i in b[1:]:
    if i:
        c = multiplication(a, multiplication(c, c))
    else:
        c = multiplication(c, c)

for r in c:
    print(*r)
