# https://www.acmicpc.net/problem/2096
# BOJ 2096 - 내려가기

'''
3
1 2 3
4 5 6
4 9 0
'''

import sys

N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_dp = [board[0]]
max_dp = [board[0]]

for i in range(1, N):
    min_dp.append([])
    max_dp.append([])
    # [i][0]
    min_dp[i].append(min(min_dp[i-1][0], min_dp[i-1][1]) + board[i][0])
    max_dp[i].append(max(max_dp[i - 1][0], max_dp[i - 1][1]) + board[i][0])

    # [i][1]
    min_dp[i].append(min(min_dp[i - 1][0], min_dp[i - 1][1], min_dp[i - 1][2]) + board[i][1])
    max_dp[i].append(max(max_dp[i - 1][0], max_dp[i - 1][1], max_dp[i - 1][2]) + board[i][1])

    # [i][2]
    min_dp[i].append(min(min_dp[i - 1][1], min_dp[i - 1][2]) + board[i][2])
    max_dp[i].append(max(max_dp[i - 1][1], max_dp[i - 1][2]) + board[i][2])

print(max(max_dp[-1]), min(min_dp[-1]))
