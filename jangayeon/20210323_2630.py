import sys
input=sys.stdin.readline


def cut(n,x,y):
    global b,w
    color=array[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=array[i][j]:
                cut(n//2,x,y)
                cut(n//2,x,y+n//2)
                cut(n//2,x+n//2,y)
                cut(n//2,x+n//2,y+n//2)
                return
    
    if color==0:
        w+=1
        return
    else:
        b+=1
        return


N=int(input())
array=[list(map(int,input().split())) for _ in range(N)]
w=0
b=0
cut(N,0,0)
print(w)
print(b)

