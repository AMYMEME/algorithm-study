# https://www.acmicpc.net/problem/9663
# 백준 9663 - N-Queen

import sys


def start(ci):
    global result
    if ci == N:
        result += 1
        return
    for j in range(N):
        if j in cols or (ci-j) in right_dia or (ci+j) in left_dia:
            continue
        rows.add(ci)
        cols.add(j)
        right_dia.add(ci-j)
        left_dia.add(ci+j)
        start(ci+1)
        rows.remove(ci)
        cols.remove(j)
        right_dia.remove(ci-j)
        left_dia.remove(ci+j)


N = int(sys.stdin.readline())
rows = set()
cols = set()
left_dia = set()  # \
right_dia = set()  # /
result = 0
start(0)
print(result)
