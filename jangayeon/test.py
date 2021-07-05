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