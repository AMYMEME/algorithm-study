#문제:  https://www.acmicpc.net/problem/1005

from collections import defaultdict, deque

def top():
    dP_ = [0] * (N+1) #결과 저장
    q = deque() #큐 

    for i in range(1, N+1):
        if in_degree[i] == 0: #진입 차수 0인 것 enque
            q.append(i)
            dP_[i] += time_[i]

    while q: #empty까지 deque
        now = q.popleft() #que에서 원소 꺼내기

        for i in graph[now]:
            in_degree[i] -= 1 #꺼낸 노드와 연결된 모든 노드의 진입 차수 -1
            dP_[i] = max(dP_[i], dP_[now] + time_[i]) 
            #현재 값 vs 새로 꺼낸 노드 기준 시간 갱신

            if in_degree[i] == 0: #새롭게 진입차수 0 된 노드 enque
                q.append(i)


    return dP_[target]
    
    
T = int(input()) #테스트 케이스 갯수

for test_case in range(T):

    N, K = map(int, input().split()) #건물 개수, 건물 건설 순서 규칙 갯수
    time_ = [0] + list(map(int, input().split())) #건물 당 걸리는 시간
    graph = [[] for _ in range(N+1)] #건물 순서 저장 배열
    in_degree = [0] * (N+1) #진입 차수 저장 배열

    for _ in range(K):
        start, end = map(int, input().split()) #건물 순서 저장 입력 받기
        graph[start].append(end) #건물 선후 관계 각각 연결
        in_degree[end] += 1 #진입 차수 +1

    target = int(input()) #건설 해야 할 건물 번호

    print(top())
