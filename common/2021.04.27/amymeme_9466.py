# https://www.acmicpc.net/problem/9466
# 백준 9466 - 텀 프로젝트

import sys
from collections import defaultdict, deque


def solution(students, size):
    graph = defaultdict(int)
    for idx, student in enumerate(students, start=1):
        graph[idx] = student

    visited = set()
    total_cnt = size

    for i in range(1, size + 1):
        if i in visited:
            continue
        save = [i]
        q = deque(save)
        visited.add(i)
        while q:
            selector = q.popleft()
            selectee = graph[selector]
            if selectee not in visited:
                q.append(selectee)
                save.append(selectee)
                visited.add(selectee)
            else:
                cnt = 0
                while True:
                    if not save:
                        cnt = 0
                        break
                    cnt += 1
                    if save.pop() == selectee:
                        break
                total_cnt -= cnt
    return total_cnt


N = int(sys.stdin.readline())
for _ in range(N):
    size = int(sys.stdin.readline())
    students = list(map(int, sys.stdin.readline().split()))
    print(solution(students, size))
