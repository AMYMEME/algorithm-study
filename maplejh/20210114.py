'''
https://www.acmicpc.net/problem/1107
'''
import sys

def check(num, broken_numbers):
    num=list(str(num))
    for i in num:
        if i in broken_numbers: return False
    return True

if __name__ == "__main__":
    N=sys.stdin.readline().strip()
    broken_numbers=[]
    if(sys.stdin.readline().strip()!='0'):
        broken_numbers=list(sys.stdin.readline().split())
    push_count=abs(int(N)-100) # +/-만
    for i in range(1000001):
        if check(i,broken_numbers): push_count=min(push_count,abs(i-int(N))+len(str(i)))
    
    print(push_count)