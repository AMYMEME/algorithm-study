#https://www.acmicpc.net/problem/14002

n = int(input())
arr = list(map(int, input().split()))
max_len = [1]*n

for i in range(1, n):
    for j in range(i):
        if arr[i]>arr[j]:
            max_len[i] = max(max_len[i], max_len[j]+1)

print(max(max_len))
curr_max = max(max_len)
lst = []
for i in range(n-1, -1, -1):
    if max_len[i]==curr_max:
        lst.append(arr[i])
        curr_max-=1
lst.reverse()
for i in lst:
    print(i, end=' ')