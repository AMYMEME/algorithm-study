'''
https://www.acmicpc.net/problem/17822
'''
import sys
from collections import deque,defaultdict

def check():
    erase=set()
    for key,p in plate.items():
        for j in range(M):
            if p[j]==0: continue
            if p[j]==p[(j-1)%M] or p[j]==p[(j+1)%M]:
                erase.add((key,j))
            if key!=N and p[j]==plate[key+1][j]:
                erase.add((key, j))
                erase.add((key+1,j))
    if erase:
        for ki,loc in erase:
            plate[ki][loc]=0
    else:
        num=N*M
        total=0
        for p in plate.values():
            total+=sum(p)
            num-=p.count(0)
        if num==0: return
        avg=total/num
        for a in range(1,N+1):
            for b in range(M):
                if plate[a][b]!=0:
                    if plate[a][b]-avg>0:
                        plate[a][b]-=1
                    elif plate[a][b]-avg<0:
                        plate[a][b]+=1

N,M,T=map(int,sys.stdin.readline().split())

plate=defaultdict(deque)
for i in range(1,N+1):
    plate[i].extend(list(map(int,sys.stdin.readline().split())))

rotate=[]
for _ in range(T):
    rotate.append(list(map(int, sys.stdin.readline().split())))

for x,d,k in rotate:
    for i in plate.keys():
        if i%x==0:
            if d==0:
                plate[i].rotate(k)
                # for _ in range(k):
                #     temp=plate[i].pop()
                #     plate[i].appendleft(temp)
            else:
                plate[i].reverse()
                plate[i].rotate(k)
                plate[i].reverse()
                # for _ in range(k):
                #     temp=plate[i].popleft()
                #     plate[i].append(temp)
    check()

total=0
for p in plate.values():
    total+=sum(p)
print(total)