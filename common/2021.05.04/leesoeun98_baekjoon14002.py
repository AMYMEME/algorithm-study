from collections import deque
n = int(input())
num = list(map(int, input().split()))

dp = [1 for i in range(n)]
arr = [[x] for x in num]

for i in range(n):
    for j in range(i):
        if num[i] > num[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
idx=dp.index(max(dp))
now=dp[idx]
queue=deque()
queue.append(num[idx])
for i in range(idx, -1, -1):
    if now==dp[i]+1:
        now=dp[i]
        queue.appendleft(num[i])

print(max(dp))
print(*queue)
