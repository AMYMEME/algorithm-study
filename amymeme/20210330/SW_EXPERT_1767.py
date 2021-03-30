# 1767. [SW Test 샘플문제] 프로세서 연결하기


def check(ci, cj, di, dj):
    ni = ci + di
    nj = cj + dj
    while -1 < ni < N and -1 < nj < N:
        if board[ni][nj] != 0:
            return False
        ni += di
        nj += dj
    return True


def set_coil(ci, cj, di, dj):
    global board
    ni = ci + di
    nj = cj + dj
    coil_cnt = 0

    if not check(ci, cj, di, dj):
        return False, 0

    while -1 < ni < N and -1 < nj < N:
        board[ni][nj] = 2  # flag for coil
        coil_cnt += 1
        ni += di
        nj += dj
    return True, coil_cnt


def clear_coil(ci, cj, di, dj):
    global board
    ni = ci + di
    nj = cj + dj
    while -1 < ni < N and -1 < nj < N:
        board[ni][nj] = 0
        ni += di
        nj += dj


def dfs(turn, cnt, coil):
    global max_cnt, min_coil
    if turn == len(cores):
        if cnt > max_cnt:
            max_cnt = cnt
            min_coil = coil
        elif cnt == max_cnt:
            if min_coil > coil:
                min_coil = coil
        return
    if len(cores) - turn + cnt < max_cnt:
        return
    ci, cj = cores[turn]
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        possible, coil_cnt = set_coil(ci, cj, di, dj)
        if possible:
            dfs(turn + 1, cnt + 1, coil + coil_cnt)
            clear_coil(ci, cj, di, dj)
    dfs(turn + 1, cnt, coil)


T = int(input())
for i in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    # 가장자리 제외
    for j in range(1, N):
        for k in range(1, N):
            if board[j][k] == 1:
                cores.append((j, k))
    max_cnt = 0
    min_coil = 0
    dfs(0, 0, 0)
    print('#{0} {1}'.format(i+1, min_coil))
