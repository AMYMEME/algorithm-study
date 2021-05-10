import sys


def check(l):
    for window_size in range(2, len(l) // 2 + 1):
        i = 0
        while i <= len(l) - window_size * 2:
            window = l[i:i + window_size]
            next_window = l[i + window_size:i + window_size * 2]
            if window == next_window:
                return False
            i += 1
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
