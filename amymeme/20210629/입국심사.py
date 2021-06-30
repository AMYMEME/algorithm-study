# https://programmers.co.kr/learn/courses/30/lessons/43238
# 입국심사

def solution(n, times):
    left = 1
    # max wait time
    right = max(times) * n

    while left < right:
        mid = (left + right) // 2
        possible_n = 0

        for time in times:
            possible_n += mid // time

        if possible_n >= n:
            right = mid
        else:
            left = mid + 1
    return left
