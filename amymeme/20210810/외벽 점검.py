# https://programmers.co.kr/learn/courses/30/lessons/60062
# 외벽 점검

def solution(n, weak, dist):
    dist.sort(reverse=True)
    weak_len = len(weak)
    for i in range(weak_len):
        weak.append(weak[i] + n)

    can_fix = {()}

    for count, d in enumerate(dist, start=1):
        possible_sets = []
        for i in range(weak_len):
            w = weak[i]
            possible_sets.append(set(map(lambda x: x % n, filter(lambda x: w <= x <= w + d, weak))))

        temp = set()
        for possible_set in possible_sets:
            for c in can_fix:
                new = possible_set | set(c)
                if len(new) == weak_len:
                    return count
                temp.add(tuple(new))
        can_fix = temp
    return -1
