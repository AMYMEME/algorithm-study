# https://www.acmicpc.net/problem/15686
# 백준 15686

import sys
from itertools import combinations


def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


if __name__ == "__main__":
    chicken_shops = []
    houses = []
    chicken_distances_per_shop = []

    N, M = map(int, sys.stdin.readline().split())

    for row_idx in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        for (col_idx, value) in enumerate(row):
            if value == 1:
                houses.append((row_idx, col_idx))
            if value == 2:
                chicken_shops.append((row_idx, col_idx))

    chicken_distances_per_shop = [[distance(chicken_shop, house) for house in houses] for chicken_shop in chicken_shops]
    combis = list(combinations(chicken_distances_per_shop, M))
    city_distances = []
    for combi in combis:
        city_distance = 0
        t_matrix = zip(*combi)
        for row in t_matrix:
            city_distance += min(row)
        city_distances.append(city_distance)
    print(min(city_distances))
