from collections import defaultdict, deque

answer = []
graph = defaultdict(list)


def dfs(use_tickets, total_tickets, ticket_cnt, path, cur):
    global answer
    if ticket_cnt == total_tickets:
        if not answer or answer > path:
            answer = path
            return
    for nxt in graph[cur]:
        if use_tickets[(cur, nxt)] == 0:
            continue
        use_tickets[(cur, nxt)] -= 1
        dfs(use_tickets, total_tickets, ticket_cnt+1, path+[nxt], nxt)
        use_tickets[(cur, nxt)] += 1


def solution(tickets):
    global graph
    use_tickets = defaultdict(int)
    for depart, dest in tickets:
        graph[depart].append(dest)
        use_tickets[(depart, dest)] += 1
    dfs(use_tickets, len(tickets), 0, ["ICN"], "ICN")
    return answer
