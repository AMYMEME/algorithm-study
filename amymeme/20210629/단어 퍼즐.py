def solution(strs, t):
    length = len(t)
    dp = [0] * (length + 1)

    for t_idx in range(1, length + 1):
        dp[t_idx] = float('inf')

        for word_len in range(1, 6):
            if word_len > t_idx:
                start = 0
            else:
                start = t_idx - word_len
            if t[start:t_idx] in strs:
                dp[t_idx] = min(dp[t_idx - word_len] + 1, dp[t_idx])

    return dp[-1] if dp[-1] != float('inf') else -1
