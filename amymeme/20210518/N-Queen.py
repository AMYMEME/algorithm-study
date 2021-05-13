cnt = 0


def dfs(row, n, cols, left_dias, right_dias):
    global cnt
    if row == n:
        cnt += 1
        return
    for col in range(n):
        if col in cols:
            continue
        if row + col in left_dias:
            continue
        if row - col in right_dias:
            continue
        cols.append(col)
        left_dias.append(row + col)
        right_dias.append(row - col)
        dfs(row + 1, n, cols, left_dias, right_dias)
        cols.pop()
        left_dias.pop()
        right_dias.pop()


def solution(n):
    dfs(0, n, [], [], [])
    return cnt
