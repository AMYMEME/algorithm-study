'''
https://www.acmicpc.net/problem/11047
'''
import sys

def coin(K,A):
    result=0
    for a in reversed(A):
        result+=K//a
        K%=a
    print(result)

if __name__=="__main__":
    N,K=map(int,sys.stdin.readline().split())
    A=[]
    for i in range(N):
        A.append(int(sys.stdin.readline().strip()))
    coin(K,A)