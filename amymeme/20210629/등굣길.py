# https://programmers.co.kr/learn/courses/30/lessons/42898
# 등굣길

def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]

    for x in range(1, n):
        if [1, x + 1] in puddles:
            break
        board[x][0] = 1

    for x in range(1, m):
        if [x + 1, 1] in puddles:
            break
        board[0][x] = 1

    for i in range(1, n):
        for j in range(1, m):
            if [j + 1, i + 1] in puddles:
                continue
            board[i][j] = (board[i - 1][j] + board[i][j - 1]) % 1000000007

    return board[-1][-1]