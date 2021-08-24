# https://www.acmicpc.net/problem/10942
import sys

N = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
questions = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = [[0] * (N + 1) for _ in range(N + 1)]

for d in range(N): # 문자열 길이: d+1
    for start in range(1,N+1): # 시작점
        end=start+d
        if end>N:
            break
        if num[start]!=num[end]: # 맨끝이 서로 다른 경우
            continue
        if start==end: # 길이가 1인 경우
            dp[start][end]=1
            continue
        if start+1==end: # 길이가 2인 경우
            dp[start][end]=1
            continue
        dp[start][end]=dp[start+1][end-1]

for s,e in questions:
    print(dp[s][e])


