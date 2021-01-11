import itertools
n, m=map(int, input().split())

city=[]
chickens=[]
homes=[]
distance_per_chickenshop=[]

for i in range(n):
    city.append(list(list(input().split())))
    for j in range(n):
        if city[i][j]=='2':
            chickens.append((i+1,j+1))
        elif city[i][j]=='1':
            homes.append((i+1, j+1))

distance_per_chickenshop=[[(abs(h[0]-c[0])+abs(h[1]-c[1])) for h in homes] for c in chickens]

city_chicken_distances=[]
for i in range(1, m+1):
    # 치킨집을 조합으로 나타내어, m보다 작은 치킨집 조합을 모두 구하기
    nCr_chicken = list(itertools.combinations(distance_per_chickenshop, i))
    for combi in nCr_chicken:
        city_chicken_distance=0
        for j in range(len(homes)):
            distance_per_home=[]
            for k in range(len(combi)):
                distance_per_home.append(combi[k][j])
            #1번 치킨집에서 1번집까지의 거리 vs 2번 치킨집에서 1번집까지의 거리 => 그 중 최값들끼리 더함
            #즉, 각 집에서 치킨집까지의 거리를 비교하고 그 중 최솟값을 찾는것이다.
            city_chicken_distance+=min(distance_per_home)
        city_chicken_distances.append(city_chicken_distance)
"""
근데...for문을 4번이나 중첩해 써서 효율성은 떨어지는 코드이다. 
"""
print(min(city_chicken_distances))
