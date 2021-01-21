from sys import stdin
from itertools import combinations

lab = {}
cand = []
cand_combi = []
safe_area = []


def spread_virus(key, test_lab):
    if ((key[0]-1, key[1]) in test_lab and test_lab[(key[0]-1, key[1])] == 0):
        test_lab[(key[0]-1, key[1])] = 2
        spread_virus((key[0]-1, key[1]), test_lab)
    if ((key[0], key[1]+1) in test_lab and test_lab[(key[0], key[1]+1)] == 0):
        test_lab[(key[0], key[1]+1)] = 2
        spread_virus((key[0], key[1]+1), test_lab)
    if ((key[0]+1, key[1]) in test_lab and test_lab[(key[0]+1, key[1])] == 0):
        test_lab[(key[0]+1, key[1])] = 2
        spread_virus((key[0]+1, key[1]), test_lab)
    if ((key[0], key[1]-1) in test_lab and test_lab[(key[0], key[1]-1)] == 0):
        test_lab[(key[0], key[1]-1)] = 2
        spread_virus((key[0], key[1]-1), test_lab)
    return test_lab


def get_safe_area(walls):
    count = 0
    test_lab = lab.copy()
    for i in walls:
        test_lab[i] = 1
    for key, value in test_lab.items():
        if (value == 2):
            test_lab = spread_virus(key, test_lab)
    for _, value in test_lab.items():
        if (value == 0):
            count += 1
    return count


if __name__ == "__main__":

    N, M = map(int, stdin.readline().split())

    for i in range(N):
        line = map(int, stdin.readline().split())
        for k, v in enumerate(line):
            lab[(i, k)] = v

    for key, value in lab.items():
        if (value == 0):
            cand.append(key)

    cand_combi = combinations(cand, 3)

    for i in cand_combi:
        safe_area.append(get_safe_area(i))

    print(max(safe_area))
