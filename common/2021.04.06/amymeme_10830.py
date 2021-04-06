# https://www.acmicpc.net/problem/10830
# 백준 10830 - 행렬 제곱

import sys


def get_elem(sub_list1, sub_list2):
    return sum([a * b for a, b in zip(sub_list1, sub_list2)]) % 1000


def matrix_multiply(_A, _B):
    temp = [[] for _ in range(N)]
    T_B = list(zip(*_B))
    for i in range(N):
        for j in range(N):
            temp[i].append(get_elem(_A[i], T_B[j]))
    return temp


def get_square(matrix):
    return matrix_multiply(matrix, matrix)


def solve_dq(A, B):
    if B == 1:
        return A

    square = get_square(A)
    if B % 2 == 0:
        return solve_dq(square, B // 2)
    else:
        return matrix_multiply(solve_dq(square, B // 2), A)


N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = solve_dq(A, B)
for i in range(N):
    for j in range(N):
        print(result[i][j] % 1000, end=' ')
    print()
