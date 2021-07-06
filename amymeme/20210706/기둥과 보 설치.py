# https://programmers.co.kr/learn/courses/30/lessons/60061
# 기둥과 보 설치
def add_check(result, i, j, struct):
    if struct == 0:  # 기둥
        if j == 0:  # 바닥
            return True
        if (i, j - 1, 0) in result:  # 기둥 위
            return True
        if (i, j, 1) in result or (i - 1, j, 1) in result:  # 보 양끝 위
            return True
    else:  # 보
        if (i, j - 1, 0) in result or (i + 1, j - 1, 0) in result:  # 한쪽이 기둥 위
            return True
        if (i - 1, j, 1) in result and (i + 1, j, 1) in result:
            return True
    return False


def remove_check(result, x, y, a):
    # 경우의 수가 너무 많아서 remove 했을 때 모두 만족하는지 전수 조사
    tmp = result - {(x, y, a)}
    for x, y, a in tmp:
        if not add_check(tmp, x, y, a):
            return False
    return True


def solution(n, build_frame):
    result = set()

    for work in build_frame:
        x, y, a, b = work
        if b == 0:  # 삭제
            if remove_check(result, x, y, a):
                result.remove((x, y, a))
        else:
            if add_check(result, x, y, a):
                result.add((x, y, a))

    answer = list(result)
    answer.sort()
    return answer
