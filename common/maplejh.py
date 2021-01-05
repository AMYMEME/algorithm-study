'''
https://www.acmicpc.net/problem/9012
'''

def check_vps(a):
    sum=0 #스택역할
    for i in a:
        if sum<0:
            return "NO"
        if i=="(":
            sum+=1 #push
        elif i==")":
            sum-=1 #pop
    return "YES" if sum==0 else "NO" 

if __name__ == "__main__":
    n=int(input())
    for i in range(n):
        a=input()
        print(check_vps(a))





    

