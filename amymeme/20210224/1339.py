# https://www.acmicpc.net/problem/1339
# 백준 1339 - 단어 수학


import sys
from itertools import chain

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(N)]
_words = words.copy()
word_number_dic = dict()
digits = []
max_number = 9
result = 0

while list(chain(*_words)):
    digit = []
    for idx, word in enumerate(_words):
        if not word:
            continue
        digit.append(word[-1])
        _words[idx] = word[:-1]
    digits.append(digit)

for digit in digits[::-1]:
    for char in digit:
        if char not in word_number_dic.keys():
            word_number_dic[char] = max_number
            max_number -= 1
print(word_number_dic)
for word in words:
    number = 0
    for idx, char in enumerate(word):
        number += word_number_dic[char] * pow(10, (len(word) - idx - 1))
    result += number
print(result)
