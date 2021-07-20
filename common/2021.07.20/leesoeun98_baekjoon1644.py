prime = [True] * 4000001

for i in range(2, int(4000001**0.5)):
    if prime[i]:
        for j in range(i + i, 4000001, i):
            prime[j] = False

prime_num = [i for i, j in enumerate(prime) if (j == True) and i >=2 ]

sum_prime=[0]*(len(prime_num)+1)
for i in range(len(prime_num)):
    sum_prime[i+1]=sum_prime[i]+prime_num[i]

n = int(input())
cnt = 0
left = 0
right = 1
while left < len(sum_prime) and prime_num[right-1] <= n:
    if sum_prime[right]-sum_prime[left] == n:
        cnt += 1
        left+=1
    elif sum_prime[right]-sum_prime[left] > n:
        left += 1
    else:
        if right<len(sum_prime)-1:
            right += 1
        else:
            left+=1
print(cnt)
