from collections import deque
board=[list(input())for i in range(12)]

xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]

res=0

def puyo(i, j, color):
    chain.append([i, j])
    pqueue = deque()
    pqueue.append((i, j, color))
    while pqueue:
        x, y, color = pqueue.popleft()
        for d in range(4):
            nearx=x+xd[d]
            neary=y+yd[d]
            if 0<=nearx<12 and 0<=neary<6 and board[nearx][neary]==color and check[nearx][neary]==0:
                chain.append([nearx, neary])
                check[nearx][neary]=1
                pqueue.append((nearx, neary, color))
def down():
    #뿌요 밑에 빈칸 있으면 내리기
    #밑에 부터 생각해야함. 뿌요가 j번째 줄이면 11~j까지를 탐색해야 함
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11, j, -1):
                if board[j][i]!='.' and board[k][i]=='.':
                    board[k][i]=board[j][i]
                    board[j][i]='.'
                    break

# 뿌요 터트리기 -> 떨어져 쌓이기 반복
while True:
    isTrue=False
    check = [[0] * 6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j]!='.' and check[i][j]==0:
                check[i][j]=1
                chain=[]
                puyo(i, j, board[i][j])
                if len(chain)>3:
                    isTrue=True
                    for x, y in chain:
                        board[x][y]='.'
    #터트릴게 없는 경우
    if not isTrue:
        break
    down()
    res+=1
print(res)

