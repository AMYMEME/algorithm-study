# https://programmers.co.kr/learn/courses/30/lessons/64064

import re
from itertools import product


def solution(user_id, banned_id):
    filtered = []
    for bid in banned_id:
        filter_str = ''.join(filter(any, re.split(r"(\*)", bid))).replace('*', '.')
        filter_str = '^' + filter_str + '$'

        r = re.compile(filter_str)
        filtered.append(filter(r.match, user_id))

    results = []
    for result in map(set, product(*filtered)):
        if len(result) != len(filtered):
            continue
        if result in results:
            continue
        results.append(set(result))
    return len(results)
