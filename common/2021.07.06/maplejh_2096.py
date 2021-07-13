# https://www.acmicpc.net/problem/2096
import sys

N = int(sys.stdin.readline())
board = list(map(int, sys.stdin.readline().split()))
s_max = board + [0, 0, 0]
s_min = board + [0, 0, 0]

for i in range(1, N):
    loc = (i % 2) * 3
    ploc = (i - 1) % 2 * 3
    board = list(map(int, sys.stdin.readline().split()))

    s_max[loc] = board[0] + max(s_max[ploc], s_max[ploc + 1])
    s_max[loc + 1] = board[1] + max(s_max[ploc], s_max[ploc + 1], s_max[ploc + 2])
    s_max[loc + 2] = board[2] + max(s_max[ploc + 1], s_max[ploc + 2])

    s_min[loc] = board[0] + min(s_min[ploc], s_min[ploc + 1])
    s_min[loc + 1] = board[1] + min(s_min[ploc], s_min[ploc + 1], s_min[ploc + 2])
    s_min[loc + 2] = board[2] + min(s_min[ploc + 1], s_min[ploc + 2])

last = (N - 1) % 2 * 3
print(max(s_max[last:last + 3]), end=' ')
print(min(s_min[last:last + 3]))
