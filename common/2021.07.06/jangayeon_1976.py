#문제 : https://www.acmicpc.net/problem/

/*구상 
Union Find : 간선 잇는 두 정점 구하기
*/
def Find(x):#x의 루트노드찾기
    if p[x]<0:
        return x
    else:
        y=Find(p[x])
        p[x]=y
        return y
 
def Union(x,y):
    x_p=Find(x)
    y_p=Find(y)
    if x_p != y_p:#루트노드가 같지 않으면
        p[y_p]=x_p#루트노드를 다른 루트노드에 붙여준다.
 
 
 
N=int(sys.stdin.readline())
p=[-1]*(N+1)
M=int(sys.stdin.readline())
# [[] for _ in range(N+1)]
for i in range(N):
    connection=list(map(int,sys.stdin.readline().split()))
    for j in range(i+1,N): #양방향
        if connection[j]: #짝
            Union(i+1,j+1)
 
check=True
t_plan=list(map(int,sys.stdin.readline().split()))
tmp=Find(t_plan[0])
for i in range(M):#루트 동일?
    if Find(t_plan[i])!=tmp:
        check=False
        break
 
if check:
    print("YES")
else:
    print("NO")
 
 
