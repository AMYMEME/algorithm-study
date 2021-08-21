# https://www.acmicpc.net/problem/6549
import sys

while True:
    n, *case = map(int, sys.stdin.readline().split())
    if not n:
        break
    case.append(0)  # 맨 끝값까지 비교하기 위해
    ans = 0
    s = []  # stack- 오름차순
    for i, h in enumerate(case):
        while s and case[s[-1]] >= h:  # stack에 h보다 크거나 같은 높이 pop
            ch = case[s.pop()]
            # 높이가 커버할 수 있는 구간 w
            if s:
                w = i - 1 - s[-1]
            else:
                w = i
            ans = max(ans, w * ch)
        s.append(i)
    print(ans)
