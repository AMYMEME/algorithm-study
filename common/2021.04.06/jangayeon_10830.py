#문제: https://www.acmicpc.net/problem/10830


def multi_mat(n,m1,m2): 
    result=[[0 for _ in range(n)] for _ in range(n)] #계산 결과 담는 행렬

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+=m1[i][k]*m2[k][j] #행렬 계산 값을 결과 담는 행렬에 넣어줌
            result[i][j]%=1000 #1000으로 나눈 나머지
    
    return result

def dev(n,x,mat):
    if x==1: #종료 : x // 2 = n = 0
        return mat 
    else:
        tmp=dev(n,x//2,mat)
        if x%2==0: #짝수 제곱
            return multi_mat(n,tmp,tmp)
        else: #홀수 제곱
            return multi_mat(n,multi_mat(n,tmp,tmp),mat)

n,x=map(int, input().split())
a=[list(map(int,input().split())) for _ in range(n)]

result=dev(n,x,a)
for i in result:
    for j in i:
        print(j%1000,end=' ') #종료 시 행렬이 그대로 반환 됨으로 %1000연산 필요함
    print()
