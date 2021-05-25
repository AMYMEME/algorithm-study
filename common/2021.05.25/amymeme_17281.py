# https://www.acmicpc.net/problem/17281
# ⚾

import sys
from itertools import permutations


def game_start(predictions, hitter_order):
    score = 0
    turn = 0

    for cur_inning in predictions:
        out = 0
        base1 = 0
        base2 = 0
        base3 = 0

        while out < 3:
            hitter_score = cur_inning[hitter_order[turn]]
            if hitter_score == 0:
                out += 1
            elif hitter_score == 1:
                score += base3
                base3 = base2
                base2 = base1
                base1 = 1
            elif hitter_score == 2:
                score += base3 + base2
                base3 = base1
                base2 = 1
                base1 = 0
            elif hitter_score == 3:
                score += base3 + base2 + base1
                base3 = 1
                base2 = 0
                base1 = 0
            elif hitter_score == 4:
                score += 1 + base1 + base2 + base3
                base3 = 0
                base2 = 0
                base1 = 0
            turn = (turn + 1) % 9
    return score


N = int(sys.stdin.readline())
predictions = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
total_score = 0

for per in set(permutations(range(1, 9), 8)):
    per = list(per)
    per.insert(3, 0)
    total_score = max(total_score, game_start(predictions, per))

print(total_score)
