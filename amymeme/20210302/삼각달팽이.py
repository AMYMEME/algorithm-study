# https://programmers.co.kr/learn/courses/30/lessons/68645
# 프로그래머스 메뉴리뉴얼(월간 코드 챌린지 시즌1)

from itertools import chain


def solution(n):
    answer = triangles(n)
    return list(chain(*answer))


def triangles(n):
    answer = [[0] * i for i in range(1, n + 1)]
    start = 1
    side_len = n
    seq = 0

    while side_len > 0:
        if side_len == 1:
            answer[seq * 2][seq] = start
            return answer
        count = 3 * (side_len - 1)
        elems = range(start, start + count)
        left_start = seq * 2
        for elem in elems[:side_len - 1]:
            answer[left_start][seq] = elem
            left_start += 1
        bottom = n - 1 - seq
        bottom_idx = seq
        for elem in elems[side_len - 1:side_len * 2 - 2]:
            answer[bottom][bottom_idx] = elem
            bottom_idx += 1
        right_start = -1 - seq
        right = n - 1 - seq
        for elem in elems[side_len * 2 - 2:]:
            answer[right][right_start] = elem
            right -= 1
        start += count
        side_len -= 3
        seq += 1
    return answer
