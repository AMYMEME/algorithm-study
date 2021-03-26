# 쿼드압축 후 개수 세기
# 프로그래머스 월간 코드 챌린지 시즌1
# https://programmers.co.kr/learn/courses/30/lessons/68936

from itertools import chain


def solution(arr):
    valid, value = check(arr)
    if valid:
        if value:
            return [0, 1]
        else:
            return [1, 0]
    return split(arr)


def check(sub_arr):
    space = list(chain(*sub_arr))
    if max(space) == min(space):
        return True, min(space)
    return False, -1


def split(arr):
    result = [0, 0]
    size = len(arr)
    half = size // 2
    sub_arrs = [[[] for _ in range(half)] for _ in range(4)]
    for i in range(size):
        for j in range(size):
            if i < half and j < half:
                sub_arrs[0][i].append(arr[i][j])
            elif i < half and j >= half:
                sub_arrs[1][i].append(arr[i][j])
            elif i >= half and j < half:
                sub_arrs[2][i - half].append(arr[i][j])
            elif i >= half and j >= half:
                sub_arrs[3][i - half].append(arr[i][j])

    for sub_arr in sub_arrs:
        valid, value = check(sub_arr)
        if valid:
            result[value] += 1
        else:
            sub_result = split(sub_arr)
            result[0] += sub_result[0]
            result[1] += sub_result[1]
    return result
