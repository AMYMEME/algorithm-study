#문제 : https://www.acmicpc.net/problem/1967

from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, mode):
    q = deque()
    q.append(x) #시작점 enque
    visit = [-1 for _ in range(n)] #방문 여부 배열
    visit[x] = 0
    while q:
        x = q.popleft()
        for w, nx in tree[x]:#경로가 연결 되어 있고
            if visit[nx] == -1: #아직 방문 전
                visit[nx] = visit[x] + w #가중치 더해서 갱신
                q.append(nx)
    if mode == 1:
        return visit.index(max(visit)) #최대 경로 값 가진 노드 인덱스 반환
    else:
        return max(visit) #최대 경로 값

n = int(input()) #노드 갯수
tree = [[] for _ in range(n)] 

for i in range(n-1):
    x, y, w = map(int, input().split()) #간선에 대한 정보 입력
    tree[x-1].append([w, y-1]) #양방향 연결 (index 0부터 시작해서 노드 번호-1)
    tree[y-1].append([w, x-1])
print(bfs(bfs(0, 1), 2))