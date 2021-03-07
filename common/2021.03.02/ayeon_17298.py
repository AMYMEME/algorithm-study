#문제 : https://www.acmicpc.net/problem/17298

n=int(input())
num=list(map(int,input().split()))

stack=[]
stack.append(0)

result=[-1 for _ in range(n)]

index=1

while stack and index<n:
    while stack and (num[stack[-1]]<num[index]):
        result[stack[-1]]=num[index]
        stack.pop()
    stack.append(index)
    index+=1

for i in range(len(result)):
    print(result[i],end=" ")