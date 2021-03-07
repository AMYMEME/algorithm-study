#https://www.acmicpc.net/problem/19598 -> 못 풀음...

n=int(input())
cnt=0
res=0
time={}
for i in range(n):
    a,b=map(int,input().split())
    time[a]=1
    time[b]=-1
time=sorted(time.items())

for i in range(len(time)):
    cnt+=time[i][-1]
    res=max(res,cnt)
print(res)




