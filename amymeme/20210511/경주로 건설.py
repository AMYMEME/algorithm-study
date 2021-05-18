from collections import deque

diff = [(0, -1, 'left'), (0, 1, 'right'), (-1, 0, 'up'), (1, 0, 'down')]


def bfs(board):
    N = len(board)
    q = deque([(0, 0, 0, None)])
    board[0][0] = 1
    while q:
        ci, cj, cur_cost, cur_direct = q.popleft()
        for di, dj, direct in diff:
            ni = ci + di
            nj = cj + dj
            if -1 < ni < N and -1 < nj < N and board[ni][nj] != 1:
                cost = cur_cost + 100
                if cur_direct is not None and cur_direct != direct:
                    cost += 500
                if board[ni][nj] == 0 or board[ni][nj] >= cost:
                    q.append((ni, nj, cost, direct))
                    board[ni][nj] = cost
    return board[N - 1][N - 1]


def solution(board):
    return bfs(board)
