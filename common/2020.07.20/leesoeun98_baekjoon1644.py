prime = [True] * 4000001
prime_num = []
prime[1] = False
for i in range(2, int(4000001**0.5)):
    if prime[i]:
        for j in range(i + i, 4000001, i):
            prime[j] = False
for i in range(2, 4000001):
    if prime[i]:
        prime_num.append(i)

sum_prime=[0]*(len(prime_num)+1)
for i in range(len(prime_num)):
    sum_prime[i+1]=sum_prime[i]+prime_num[i]

n = int(input())
cnt = 0
left = 0
right = 1
while left <=len(sum_prime) and prime_num[right-1] <= n:
    sumnum = sum(prime_num[left:right + 1])
    if sumnum == n:
        cnt += 1
        right+=1
    elif sumnum > n:
        left += 1
    else:
        if right<len(sum_prime)-1:
            right += 1
        else:
            left+=1
print(cnt)
