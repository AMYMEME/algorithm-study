# https://programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러

import heapq


def solution(jobs):
    answer = 0
    job_cnt = len(jobs)
    time = 0
    heapq.heapify(jobs)
    pq = []

    while jobs or pq:
        while jobs and jobs[0][0] <= time:
            start, duration = heapq.heappop(jobs)
            heapq.heappush(pq, (duration, start))
        if pq:
            duration, start = heapq.heappop(pq)
            answer += (time + duration - start)
            time += duration
            continue
        time += 1
    return answer // job_cnt
