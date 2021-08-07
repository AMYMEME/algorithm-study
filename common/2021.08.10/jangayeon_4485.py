
#문제 : https://www.acmicpc.net/problem/4485

import sys
import heapq
read = sys.stdin.readline

def problem():
    N = int(read())
    if N == 0:
        return -1
    cave = [list(map(int, read().split()))for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [[False for _ in range(N)] for _ in range(N)]
    hq = []
    heapq.heappush(hq, [cave[0][0], [0, 0]])
    answer = -1
    while hq:
        cw, cn = heapq.heappop(hq)

        if cn[0] == N-1 and cn[1] == N-1:
            answer = cw
            break

        if visit[cn[1]][cn[0]]:
            continue
            
        visit[cn[1]][cn[0]] = True
        
        for i in range(4):
            nx = cn[0] + dx[i]
            ny = cn[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[ny][nx]:
                heapq.heappush(hq, [cw + cave[ny][nx], [nx, ny]])
    return answer
    
i = 1
while True:
    answer = problem()
    if answer == -1:
        break
    else:
        print("Problem {}: {}".format(i, answer))

    i += 1