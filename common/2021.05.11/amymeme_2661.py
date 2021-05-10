import sys


def check(l):
    for window_size in range(2, len(l) // 2 + 1):
        window_end = len(l)
        window_start = window_end - window_size
        window = l[window_start:window_end]
        past = l[window_start - window_size:window_end - window_size]
        if window == past:
            return False
    return True


def dfs(l):
    global answer
    if len(l) == N:
        value = int(l)
        if value < answer:
            answer = value
        return
    for i in range(1, 4):
        if l[-1] == str(i):
            continue
        if check(l + str(i)):
            dfs(l + str(i))


N = int(sys.stdin.readline())
line = '1'
answer = int('3' * N)

dfs(line)
print(answer)
