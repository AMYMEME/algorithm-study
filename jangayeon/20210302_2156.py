#https://www.acmicpc.net/problem/2156

n=int(input())

result=[ 0 for j in range(n+1)]

wine=[0]

for j in range(n):
  wine.append(int(input()))

for i in range(1,n+1):
  if i==1:
    result[1]=wine[1]
  elif i ==2:
    result[2]=wine[1]+wine[2]
  else:
    result[i]=max(result[i-1],result[i-2]+wine[i],result[i-3]+wine[i-1]+wine[i])
  

print(result[-1])