# https://www.acmicpc.net/problem/1030
# 백준 1030 - 프렉탈 평면

import sys


def is_middle(board_len, i, j):
    n_times = board_len // N
    if n_times * middle_start <= i < n_times * middle_end:
        return n_times * middle_start <= j < n_times * middle_end
    return False


def check(board_len, i, j):
    if board_len == 1:
        print(0, end='')
        return
    if is_middle(board_len, i, j):
        print(1, end='')
    else:
        if board_len == N:
            print(0, end='')
        else:
            next_len = board_len // N
            check(next_len, i % next_len, j % next_len)


s, N, K, R1, R2, C1, C2 = map(int, sys.stdin.readline().split())
middle_start = (N - K) // 2
middle_end = middle_start + K
final_len = pow(N, s)

for i in range(R1, R2 + 1):
    for j in range(C1, C2 + 1):
        check(final_len, i, j)
    print()
