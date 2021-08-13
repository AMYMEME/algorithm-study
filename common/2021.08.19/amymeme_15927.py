# https://www.acmicpc.net/problem/15927
# 회문은 회문아니야!!

import sys


def solution(s):
    if s != s[::-1]:
        return len(s)
    if len(set(s)) == 1:
        return -1
    return len(s) - 1


print(solution(sys.stdin.readline().strip()))
