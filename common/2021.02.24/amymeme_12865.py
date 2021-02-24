# https://www.acmicpc.net/problem/12865
# 백준 12865 - 평범한 배낭
# 참고 : https://dheldh77.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B0%EB%82%AD-%EB%AC%B8%EC%A0%9CKnapsack-Problem

import sys

N, K = map(int, sys.stdin.readline().split())
weights = [0]
values = [0]
boards = [[0] * (K + 1) for _ in range(N + 1)]

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    weights.append(W)
    values.append(V)

for i in range(N + 1):
    for j in range(K + 1):
        if i == 0 or j == 0:
            continue
        if j < weights[i]:
            boards[i][j] = boards[i - 1][j]
        else:
            boards[i][j] = max(boards[i - 1][j], values[i] + boards[i - 1][j - weights[i]])
print(boards[-1][-1])
