# https://programmers.co.kr/learn/courses/30/lessons/64062
# 징검다리 건너기
def check(stones, less_than):
    cnt = 0
    max_cnt = 0
    for idx, stone in enumerate(stones):
        if stone <= less_than:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0
    return max_cnt


def solution(stones, k):
    left = 0
    right = max(stones)
    while left < right:
        mid = (left + right) // 2
        if check(stones, mid) < k:
            left = mid + 1
        else:
            right = mid
    return left
