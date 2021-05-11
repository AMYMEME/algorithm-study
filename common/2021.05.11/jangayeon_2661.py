#https://www.acmicpc.net/problem/2661


def back_tracking(idx): 
    for i in range(1, (idx//2) + 1): 
        if s[-i:] == s[-2*i:-i]: #나쁜 순열인 경우
            return -1 
    if idx == n: #백트래킹의 깊이 = n 
        for i in range(n): #출력
            print(s[i], end = '') 
        return 0 
    for i in range(1, 4): #후보가 되는 문자열 만들기
        s.append(i) 
        if back_tracking(idx + 1) == 0: 
            return 0 
        s.pop() 

n = int(input()) 
s = [] 
back_tracking(0)

