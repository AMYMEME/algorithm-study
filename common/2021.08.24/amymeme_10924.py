# https://www.acmicpc.net/problem/10924
# 팰린드롬?

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
palindromes = defaultdict(set)
M = int(sys.stdin.readline())
questions = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

for start in set(map(lambda x: x[0], questions)):
    palindromes[start].add(start)

    start -= 1  # for idx
    for end in range(N - 1, start, -1):
        flag = True
        for diff in range((end - start) // 2 + 1):
            if numbers[start + diff] != numbers[end - diff]:
                flag = False
                break
        if flag:
            palindromes[start + 1].add(end + 1)

for i, j in questions:
    if j in palindromes[i]:
        print(1)
    else:
        print(0)
