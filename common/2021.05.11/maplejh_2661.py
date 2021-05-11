"""
https://www.acmicpc.net/problem/2661
"""
import sys


def backtracking(idx):
    for k in range(1, idx // 2 + 1):
        if answer[-2 * k:-k] == answer[-k:]:
            return False
    if idx == N:
        return True
    for i in range(1, 4):
        answer.append(i)
        if backtracking(idx + 1):
            return True
        answer.pop()


answer = []
N = int(sys.stdin.readline())
backtracking(0)
for n in answer:
    print(n,end='')
