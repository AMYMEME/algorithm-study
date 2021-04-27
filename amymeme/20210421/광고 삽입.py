# https://programmers.co.kr/learn/courses/30/lessons/72414
# 2021 KAKAO BLIND RECRUITMENT - 광고 삽입

def time_to_int(h, m, s):
    return h * 3600 + m * 60 + s


def solution(play_time, adv_time, logs):
    a_h, a_m, a_s = map(int, adv_time.split(":"))
    adv_int = time_to_int(a_h, a_m, a_s)
    p_h, p_m, p_s = map(int, play_time.split(":"))
    play_int = time_to_int(p_h, p_m, p_s)
    if play_int <= adv_int:
        return "00:00:00"
    dp = [0 for _ in range(play_int + 1)]
    for log in logs:
        start, end = log.split("-")
        s_h, s_m, s_s = map(int, start.split(":"))
        e_h, e_m, e_s = map(int, end.split(":"))
        start_int = time_to_int(s_h, s_m, s_s)
        end_int = time_to_int(e_h, e_m, e_s)
        dp[start_int] += 1
        dp[end_int] -= 1
    for i in range(1, len(dp)):
        dp[i] = dp[i - 1] + dp[i]

    max_time = 0
    answer = adv_int
    now = sum(dp[:adv_int])
    for i in range(adv_int - 1, play_int + 1):
        now -= dp[i - adv_int]
        now += dp[i]
        if now > max_time:
            max_time = now
            answer = i

    answer = answer - adv_int + 1

    H, answer = divmod(answer, 3600)
    M, S = divmod(answer, 60)

    return "{0:02}:{1:02}:{2:02}".format(H, M, S)