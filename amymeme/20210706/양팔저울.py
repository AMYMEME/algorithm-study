# https://www.acmicpc.net/problem/2629
# BOJ 2629 - 양팔저울

'''
2
1 4
2
3 2
Y N

4
2 3 3 3
3
1 4 10
Y Y N
'''

import sys

def solution(goal):



_ = int(sys.stdin.readline())
sinkers = list(map(int, sys.stdin.readline().split()))
_ = int(sys.stdin.readline())
goals = list(map(int, sys.stdin.readline().split()))

for x in goals:
    print(solution(x))
