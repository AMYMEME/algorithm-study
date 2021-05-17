# https://programmers.co.kr/learn/courses/30/lessons/43105

import copy


def solution(triangle):
    dp = copy.deepcopy(triangle)
    for row_idx, row in enumerate(triangle[:-1]):
        for col_idx, _ in enumerate(row):
            dp[row_idx + 1][col_idx] = max(dp[row_idx + 1][col_idx],
                                           dp[row_idx][col_idx] + triangle[row_idx + 1][col_idx])
            dp[row_idx + 1][col_idx + 1] = max(dp[row_idx + 1][col_idx + 1],
                                               dp[row_idx][col_idx] + triangle[row_idx + 1][col_idx + 1])
    answer = max(dp[-1])
    return answer
