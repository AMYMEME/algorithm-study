#문제 : https://www.acmicpc.net/problem/

import sys

def find(x):#x의 루트노드찾기
    if P[x]<0:
        return x
    else:
        y=find(P[x])
        P[x]=y
        return P[x]
 
def union(x,y):
    x_root=find(x)
    y_root=find(y)
    if x_root != y_root:#루트노드가 같지 않으면
        P[y_root]=x_root#루트노드를 다른 루트노드에 붙여준다.
 
 
#전체 도시수 
N=int(sys.stdin.readline())
#주어진 원소 갯수 만큼 사용하지 않을 값 -1 생성
P=[-1]*(N+1)  #도시가 1부터 시작해서 (N+1)로 통일
#여행 계획에 속한 도시 수
M=int(sys.stdin.readline())

for i in range(N):
    connection=list(map(int,sys.stdin.readline().split()))
    for j in range(i+1,N): #양방향
        if connection[j]: #짝
            union(i+1,j+1)
 
check=True
t_route=list(map(int,sys.stdin.readline().split())) #여행 경로
t_root=find(t_route[0])
for i in range(M):#루트 동일?
    if find(t_route[i])!=t_root:
        check=False
        break
 
if check:
    print("YES")
else:
    print("NO")