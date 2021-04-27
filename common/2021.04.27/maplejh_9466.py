"""
https://www.acmicpc.net/problem/9466
"""
import sys

sys.setrecursionlimit(1000001)


def dfs(start):
    global final
    visit[start] = 1
    loop.append(start)

    if visit[students[start]]:
        if students[start] in loop:
            final += loop[loop.index(students[start]):]
            return
    else:
        dfs(students[start])


T = int(sys.stdin.readline())
student = []
for _ in range(T):
    n = int(sys.stdin.readline())
    temp = list(map(int, sys.stdin.readline().split()))
    students = dict()
    for i in range(1, n + 1):
        students[i] = temp[i - 1]

    visit = [1] + [0] * n
    final = []
    for s in students.keys():
        if not visit[s]:
            loop = []
            dfs(s)

    print(n - len(final))
