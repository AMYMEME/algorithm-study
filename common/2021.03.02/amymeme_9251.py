# https://www.acmicpc.net/problem/9251
# 백준 9251 - LCS(Longest Common Subsequence, 최장 공통 부분 수열)
# 참고 - https://ko.wikipedia.org/wiki/%EC%B5%9C%EC%9E%A5_%EA%B3%B5%ED%86%B5_%EB%B6%80%EB%B6%84_%EC%88%98%EC%97%B4

import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
N = len(second)
M = len(first)

matrix = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if second[i-1] == first[j-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
print(matrix[-1][-1])