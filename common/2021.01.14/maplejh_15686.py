'''
https://www.acmicpc.net/problem/15686
'''
from itertools import combinations

def cal_per_chicken_distance(house,chicken):
    return abs(house[0]-chicken[0])+abs(house[1]-chicken[1])

def total_chicken_distance(candiate,house):
    total=0
    for per_house in house:
        distance=200
        for chicken in candiate:
            distance=min(distance,cal_per_chicken_distance(per_house,chicken))
        total+=distance    
    return total

if __name__ == "__main__":
    chicken=[]
    house=[]
    N, M = map(int,input().split())
    for i in range(N):
        row=list(map(int,input().split()))
        for j in range(N):
            if row[j]==1:
                house.append((i,j))
            elif row[j]==2:
                chicken.append((i,j))
            else:
                continue
    chicken_distance=1000000000
    for candidate in list(combinations(chicken, M)):
        chicken_distance=min(chicken_distance,total_chicken_distance(candidate, house))
    print(chicken_distance)