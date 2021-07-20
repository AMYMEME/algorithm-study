# https://app.codility.com/programmers/trainings/4/polygon_concavity_index/
# PolygonConcavityIndex


from extratypes import Point2D


def direction(A, B, C):
    ex_product = (B.x - A.x) * (C.y - A.y) - (B.y - A.y) * (C.x - A.x)
    if ex_product > 0:
        return 1  # counter-clock
    elif ex_product < 0:
        return -1  # clock
    else:
        return 0  # flat


def solution(A):
    size = len(A)

    low_y = float('INF')
    low_ys = []
    for i in range(size):
        if A[i].y < low_y:
            low_y = A[i].y
            low_ys = [i]
        elif A[i].y == low_y:
            low_ys.append(i)

    start_point = low_ys[0]
    low_y_array = [False] * size
    for i in low_ys:
        low_y_array[i] = True

    while low_y_array[start_point]:
        start_point = (start_point + 1) % size
    start_point = (start_point - 1 + size) % size

    rotated_A = A[start_point:] + A[: start_point]
    d = direction(rotated_A[-1], rotated_A[0], rotated_A[1])
    extend_A = rotated_A + rotated_A[:2]
    for i in range(size):
        temp = direction(extend_A[i], extend_A[i + 1], extend_A[i + 2])
        if temp * d < 0:
            return (i + 1 + start_point) % len(A)
    return -1
