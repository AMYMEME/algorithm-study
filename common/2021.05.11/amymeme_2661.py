import sys


def dfs(idx):
    global answer
    for window_size in range(2, idx // 2 + 1):
        if answer[-2 * window_size:-window_size] == answer[-window_size:]:
            return False
    if idx == N:
        return True
    for i in range(1, 4):
        if answer[idx - 1] == i:
            continue
        answer.append(i)
        if dfs(idx + 1):
            return True
        answer.pop()


N = int(sys.stdin.readline())
answer = [1]

dfs(1)
print(*answer, sep="")
