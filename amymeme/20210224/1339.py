# https://www.acmicpc.net/problem/1339
# 백준 1339 - 단어 수학
# 참고 : https://suri78.tistory.com/183

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]
dic = defaultdict(int)
max_number = 9
result = 0

for word in words:
    for idx, char in enumerate(word):
        dic[char] += pow(10, (len(word) - idx - 1))

digits = list(dic.values())
digits.sort(reverse=True)

for digit in digits:
    digit *= max_number
    max_number -= 1
    result += digit
print(result)