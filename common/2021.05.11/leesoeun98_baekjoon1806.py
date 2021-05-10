n, s = map(int, input().split())
num = list(map(int, input().split()))
# sum 사용시 시간 초과남
sum_each_num = [0] * (n + 1)
for i in range(1, n + 1):
    sum_each_num[i] = sum_each_num[i - 1] + num[i - 1]
left = 0
right = 1
res = 1000001
while left != n:
    sumnum = sum_each_num[right] - sum_each_num[left]
    length = right - left
    #여기도 마지막인 경우를 예외처리해야함
    if sumnum < s:
        if right == n:
            left += 1
        else:
            right += 1
    elif sumnum >= s:
        if res > length:
            res = length
        left += 1

if res == 1000001:
    print(0)
else:
    print(res)
