# https://www.acmicpc.net/problem/15927
import sys


def sol():
    l = len(word)
    ans = l  # 부분 문자열 길이
    while True:
        for i in range(l - ans + 1):
            temp = word[i:i + ans]  # 부분 문자열
            if temp != temp[::-1]:  # 회문이 아닌 경우
                return ans
        ans -= 1
    return ans


word = sys.stdin.readline().strip()
if len(set(word)) == 1:  # 맨끝까지 탐색이 오래 걸리는거 같아서 나눠서 구하기
    print(-1)
else:
    print(sol())

'''
간단한 방법: 경우의 수를 3개로 나눠서 풀면됨
1. 회문인 경우  
    -> 모든 문자가 같은 경우에는 -1 
    -> 다른 경우에는 문자열길이-1
2. 회문이 아닌 경우 -> 문자열길이 그대로 출력
'''