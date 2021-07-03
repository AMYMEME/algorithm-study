# https://programmers.co.kr/learn/courses/30/lessons/12904
# 가장 긴 팰린드롬

def solution(s):
    l = len(s)
    dp = [1] * l
    for i in range(1, l):
        dp[i] = dp[i - 1]
        for j in range(i):
            if s[j:i + 1] == s[i::-1][0:i - j + 1]:
                dp[i] = max(dp[i], i - j + 1)

    return dp[-1]
