"""
https://www.acmicpc.net/problem/17281
"""
import sys
from itertools import permutations


def game(o):
    s = 0
    o.insert(3, 0)
    n = 0
    for res in inns.values():
        bs = 0
        out = 0
        while True:
            n %= 9
            player = o[n]
            if out == 3:
                break
            if res[player] == 0:
                out += 1
            else:
                bs = (bs << 1 | 1) << (res[player] - 1)
                s += bin(bs >> 3).count('1')
                bs = bs & 7
            n += 1
    return s


N = int(sys.stdin.readline())
inns = dict()
for i in range(1, N + 1):
    inns[i] = list(map(int, sys.stdin.readline().split()))
ppl = [p for p in range(1, 9)]
score = 0
for o in permutations(ppl, 8):
    score = max(game(list(o)), score)

print(score)
