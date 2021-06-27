# https://programmers.co.kr/learn/courses/30/lessons/60059
# 자물쇠와 열쇠

def rotate_right(matrix):
    return list(map(list, map(reversed, zip(*matrix))))


def check(key, key_i, key_j, lock):
    N = len(lock)
    M = len(key)

    i = 0
    while i < N:
        j = 0
        while j < N:
            if -1 < i + key_i < M and -1 < j + key_j < M:
                bit = key[i + key_i][j + key_j] ^ lock[i][j]  # 둘다 튀어나온 부분이어도 안됨
            else:
                bit = lock[i][j]
            if not bit:
                return False
            j += 1
        i += 1
    return True


def solution(key, lock):
    if sum(row.count(1) for row in key) < sum(row.count(0) for row in lock):
        return False
    N = len(lock)
    M = len(key)

    for _ in range(5):
        key = rotate_right(key)
        # key는 오른쪽, 밑으로는 N만큼 갈 수 있고, 위, 왼쪽으로는 M만큼 갈 수 있음
        for key_i in range(-N, M):
            for key_j in range(-N, M):
                if check(key, key_i, key_j, lock):
                    return True
    return False
