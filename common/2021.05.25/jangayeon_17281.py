#https://www.acmicpc.net/problem/17281


import sys
from itertools import permutations
read = sys.stdin.readline
    
N = int(read())
results = [list(map(int, read().split())) for _ in range(N) ]
 
# (index+1)타순에 value번 선수가 친다.
# 4번타자는 0번 선수로 고정
# 8!개의 경우의 수
 
maxScore = -1
 
for order in permutations((range(1, 9)), 8):
    order = list(order[:3]) + [0] + list(order[3:])
    hitter = 0
    score = 0
    for i in range(N):
        # 한 이닝에서 유지되는것들
        outcount = 0
        first, second, third = 0, 0, 0
 
        while outcount < 3:                 #3아웃이 될때까지 반복
            # 같은 타석에서 유지되는 것들
            result = results[i][order[hitter]]
            
            if result == 0:     #아웃
                outcount +=1
            elif result == 1:
                score += third
                first, second, third = 1, first, second
            elif result == 2:
                score += (second + third)
                first, second, third = 0, 1, first
            elif result == 3:
                score += (first + second + third)
                first, second, third = 0, 0, 1
            elif result == 4:
                score += (first + second + third + 1)
                first, second, third = 0, 0, 0
      
            hitter = (hitter + 1) % 9                     #다음타자
    if maxScore < score:
        maxScore = score
 
print(maxScore)