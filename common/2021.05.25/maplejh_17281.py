"""
https://www.acmicpc.net/problem/17281
"""
import sys
from itertools import permutations


def game(o):
    s = 0
    o.insert(3, 0)  # 타순
    n = 0
    for res in inns.values():  # 각 이닝
        bs1 = 0
        bs2 = 0
        bs3 = 0
        out = 0
        while True:
            n %= 9
            player = o[n]
            if out == 3:
                break  # 이닝 종료
            if res[player] == 0:  # 아웃
                out += 1
            elif res[player]==1:
                s+= bs3
                bs3=bs2
                bs2=bs1
                bs1=1
            elif res[player]==2:
                s+=bs3+bs2
                bs3=bs1
                bs2=1
                bs1=0
            elif res[player]==3:
                s += (bs1 + bs2 + bs3)
                bs3=1
                bs2=0
                bs1=0
            elif res[player]==4:
                s+=(bs1+bs2+bs3+1)
                bs1=0
                bs2=0
                bs3=0
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
