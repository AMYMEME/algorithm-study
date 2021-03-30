#https://www.acmicpc.net/problem/11399

N = int(input())
lists = list(map(int, input().split()))
total = 0
lists.sort()
for i in range(N):
    for j in range(i + 1):
        total += lists[j]
print(total)