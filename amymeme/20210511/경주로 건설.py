answer = 1000000000


def dfs(ci, cj, board, N, cur_direct, straight_cnt, corner_cnt):
    global answer
    if ci == N - 1 and cj == N - 1:
        cur_cost = straight_cnt * 100 + corner_cnt * 500
        if cur_cost < answer:
            answer = cur_cost
        return
    for di, dj, n_direct in [(0, -1, 'left'), (0, 1, 'right'), (-1, 0, 'up'), (1, 0, 'down')]:
        ni = ci + di
        nj = cj + dj
        if -1 < ni < N and -1 < nj < N:
            if board[ni][nj] != 0:
                continue
            board[ni][nj] = 2
            if ci == 0 and cj == 0:
                dfs(ni, nj, board, N, n_direct, 1, 0)
                board[ni][nj] = 0
                continue
            if n_direct != cur_direct:
                dfs(ni, nj, board, N, n_direct, straight_cnt + 1, corner_cnt + 1)
            else:
                dfs(ni, nj, board, N, n_direct, straight_cnt + 1, corner_cnt)
            # back tracking
            board[ni][nj] = 0


def solution(board):
    global answer
    N = len(board)
    board[0][0] = 2
    dfs(0, 0, board, N, None, 0, 0)
    return answer