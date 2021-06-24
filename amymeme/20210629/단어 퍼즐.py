import heapq


def solution(strs, t):
    pq = []
    satis_length_set = {0}
    heapq.heappush(pq, (0, 0))
    while pq:
        str_cnt, satis_length = heapq.heappop(pq)
        if satis_length == len(t):
            return str_cnt
        if satis_length > len(t):
            break
        goal_str = t[satis_length:]
        for word in strs:
            if goal_str.find(word) == 0:
                if satis_length + len(word) in satis_length_set:
                    continue
                heapq.heappush(pq, (str_cnt + 1, satis_length + len(word)))
    return -1
