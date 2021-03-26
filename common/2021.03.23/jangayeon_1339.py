
# 문제 : https://www.acmicpc.net/problem/1339
# import sys; sys.stdin.readline 사용 X

N=int(input())
words=[input() for _ in range(N)]


letter_digits={}

for word in words:
    cnt=len(word)-1
    for letter in word:
        if letter in letter_digits:
            letter_digits[letter]+=pow(10,cnt)
        else:
            letter_digits[letter]=pow(10,cnt)
        cnt-=1


digits=sorted(list(letter_digits.values()),reverse=True)
result=0
for i in range(len(digits)):
    result+=digits[i]*(9-i)
print(result)

