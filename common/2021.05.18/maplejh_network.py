'''
https://programmers.co.kr/learn/courses/30/lessons/43162
'''
from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            q = deque()
            q.append(i)
            visited[i] = 1
            while q:
                nx = q.popleft()
                for b in range(n):
                    if computers[nx][b] == 1 and visited[b] == 0:
                        visited[b] = 1
                        q.append(b)
            answer += 1
    return answer
