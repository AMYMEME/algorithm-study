import sys
sys.setrecursionlimit(100000) #최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다
def DFS(start, cycle):
    global answer
    check[start]=1
    cycle.append(start)
    next = matrix[start]
    # 더이상 방문 불가, 마지막 학생이면
    # 마지막 학생이 가리키는 학생부터 사이클이 형성됨
    if check[next]==1:
        if next in cycle:
            answer+=cycle[cycle.index(next):]
            return
    else:
        DFS(next, cycle)

for _ in range(int(input())):
    n = int(input())
    matrix = [0] + list(map(int, sys.stdin.readline().split()))
    check=[0]*(n+1)
    answer=[]
    for i in range(1, n + 1):
        if check[i]==0:
            DFS(i, [])
    print(n - len(answer))
