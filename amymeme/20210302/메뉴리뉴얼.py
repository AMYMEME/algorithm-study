# https://programmers.co.kr/learn/courses/30/lessons/72411
# 프로그래머스 메뉴리뉴얼(2021 KAKAO BLIND RECRUITMENT)

from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    for course_len in course:
        result = result_per_course(orders, course_len)
        result = list(map(sorted, result))
        answer += result_per_course(orders, course_len)
    answer.sort()
    return answer


def result_per_course(orders, course_len):
    my_dict = defaultdict(int)
    for order in orders:
        combis = combinations(order, course_len)
        for combi in combis:
            my_dict[tuple(sorted(combi))] += 1
    if not my_dict:
        return []
    max_value = max(my_dict.values())
    if max_value < 2:
        return []
    return [''.join(key) for key in my_dict.keys() if my_dict[key] == max_value]
