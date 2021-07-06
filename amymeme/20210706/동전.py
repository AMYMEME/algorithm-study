# https://www.acmicpc.net/problem/9084
# BOJ 9084 - 동전
import sys


def solution(coins, goal):
    dp = [0] * (goal + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, goal + 1):
            dp[j] += dp[j - coin]
    return dp[-1]


T = int(sys.stdin.readline())
for i in range(T):
    _ = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    goal = int(sys.stdin.readline())
    print(solution(coins, goal))
