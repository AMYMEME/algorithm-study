# https://programmers.co.kr/learn/courses/30/lessons/17678
# [1차] 셔틀버스

import heapq


def from_hhmm(hhmm):
    h, m = hhmm.split(':')
    return int(h) * 60 + int(m)


def to_hhmm(time):
    h, m = divmod(time, 60)
    return '{0:02}:{1:02}'.format(h, m)


def solution(n, t, m, timetable):
    answer = ''
    # sort
    timetable = list(map(from_hhmm, timetable))
    heapq.heapify(timetable)

    logs = []
    clock = 9 * 60
    while n > 0:
        cnt = 0
        persons = []
        if not timetable:
            break
        while timetable and timetable[0] <= clock and cnt < m:
            cnt += 1
            persons.append(heapq.heappop(timetable))
        logs.append((to_hhmm(clock), cnt, persons))
        n -= 1
        clock += t

    for time, cnt, arrives in logs[::-1]:
        if cnt < m:
            return time
        else:
            return to_hhmm(max(arrives) - 1)
    return answer
