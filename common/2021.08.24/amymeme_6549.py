# https://www.acmicpc.net/problem/6549
# 히스토그램에서 가장 큰 직사각형

# 참고 : https://foramonth.tistory.com/13


import sys


def solution(l):
    N = l[0]
    stack = []  # (connect_start_idx, value)
    max_value = 0

    for cur_idx, cur_h in enumerate(l[1:]):
        min_idx = cur_idx
        while stack and stack[-1][1] >= cur_h:
            min_idx, before_h = stack.pop()
            max_value = max(max_value, before_h * (cur_idx - min_idx))
        stack.append((min_idx, cur_h))

    # square for start_idx ~
    for start_idx, value in stack:
        max_value = max(max_value, (N - start_idx) * value)
    return max_value


while True:
    row = list(map(int, sys.stdin.readline().split()))
    if row == [0]:
        break
    print(solution(row))
