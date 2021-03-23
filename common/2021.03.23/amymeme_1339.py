# https://www.acmicpc.net/problem/1339
# 백준 1339 - 단어 수학

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
alphabet = defaultdict(int)

for _ in range(N):
    word = sys.stdin.readline().strip()
    for idx, w in enumerate(word[::-1]):
        alphabet[w] += pow(10, idx)

values = sorted(alphabet.values(), reverse=True)

digit = 9  # max
result = 0
for value in values:
    result += value * digit
    digit -= 1
print(result)
