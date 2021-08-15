# https://www.acmicpc.net/problem/1328
import sys
from math import comb, factorial

sys.setrecursionlimit(10 ** 9)


def solution(h, s):
    if h == s:
        return 1
    if s == 1:
        return factorial(h - 1)
    tmp = 0
    for j in range(h - s + 1):
        tmp += (solution(h - 1 - j, s - 1) * comb(h - 1, j) * factorial(j))
    return tmp


N, L, R = map(int, sys.stdin.readline().split())
answer = 0
for i in range(L - 1, N - R + 1):  # 가장 높은 빌딩의 위치
    print(i)
    # 가장 높은 빌딩이 양 끝에 존재해야하는 경우
    if (L == 1 and i) or (R == 1 and (N - 1 - i)):
        continue
    left = solution(i, L - 1) * comb(N - 1, i)
    right = solution(N - 1 - i, R - 1)
    answer += (left * right)

print(answer%1000000007)

'''
 시간초과; 가장 큰 빌딩을 먼저 배치하는 방법으로
 좌표: 0 ~ N-1
 가장 높은 빌딩 가능한 위치 i 
 -> 왼쪽에서 남은 빌딩 (n-1) 중 왼쪽에 가능한 개수(i개) 빌딩조합 (n-1)C(i)
 -> solution 함수: 총 h개의 빌딩 중에서 s개가 보이는 경우의 수 반환
    가장 높은 빌딩은 항상 보이니까 왼쪽에서 i개 중에서 L-1개가 보이도록
 -> 오른쪽도 같은 방법으로
'''