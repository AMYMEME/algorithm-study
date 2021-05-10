n = int(input())
res = [0 for i in range(n)]


def check(res, depth):
    for k in range(depth):
        temp = res[k:]
        for i in range(1, (depth // 2) + 1):
            if temp[:i] == temp[i:2 * i]:
                return False
    return True


def DFS(depth):
    # 나쁜 수열 종료
    if not check(res, depth):
        return -1
    # return 0 으로 하나만 출력하도록 함
    if depth == n:
        print(''.join(res))
        return 0
    else:
        for i in range(1, 4):
            res[depth] = str(i)
            if DFS(depth + 1) == 0:
                return 0


DFS(0)
