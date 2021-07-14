#문제 : https://www.acmicpc.net/problem/2096
#구상 : dp 배열의 슬라이딩 윈도우 
#2차원 배열로
#점화식 : D[i][0] = max(D[i-1][0], D[i-1][1]) + arr[0] */

n=int(input())
table=[list(map(int,input().split()))for _ in range(n)]
large=small=table[0]


for i in range(1,n):
    large=[max(large[0],large[1])+table[i][0],
        max(large[0],large[1],large[2])+table[i][1],
        max(large[1],large[2])+table[i][2]]
    small=[min(large[0],large[1])+table[i][0],
        min(large[0],large[1],large[2])+table[i][1],
        min(large[1],large[2])+table[i][2]]

print(max(large),min(small))