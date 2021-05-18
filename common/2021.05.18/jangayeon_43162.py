def solution(n, computers):
    net_cnt = 0 #네트워크 갯수 확인
    visited = [0]*n #방문여부 Check
    bfs = [] #큐
    

    while 0 in visited: #아직 방문 X인 노드에 대해 (=연결여부 확인 안 한 노드에 대해)
        bfs.append(visited.index(0)) #지금까지 방문 안 한 노드에 싹 다 큐에 넣어서 진행 
        while bfs: #연결여부 확인할 노드가 없을 때까지
            node = bfs.pop(0) #맨 앞에 있는 큐 값 pop
            visited[node] = 1 #방문 했으니 check
            for i in range(n): #전체 노드 돌면서 연결 여부 check
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i) #이전에 방문한 적 없고 지금 검사하는 노드랑 연결되어 있음
        net_cnt += 1
    return net_cnt