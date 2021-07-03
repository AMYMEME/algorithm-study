# https://programmers.co.kr/learn/courses/30/lessons/42884
# 단속카메라

duplicates = []


def check(route):
    if not duplicates:
        duplicates.append(route)
        return
    if duplicates[-1][1] >= route[0]:
        duplicates[-1] = (route[0], min(duplicates[-1][1], route[1]))
    else:
        duplicates.append(route)


def solution(routes):
    # duplicates.clear()
    routes.sort()

    for route in routes:
        check(route)

    return len(duplicates)
