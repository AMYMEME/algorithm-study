# https://programmers.co.kr/learn/courses/30/lessons/42628
import bisect


def solution(operations):
    q = []

    for operation in operations:
        operation = operation.split()
        if operation[0] == 'I':
            expect_loc = bisect.bisect(q, int(operation[1]))
            left = q[:expect_loc]
            left.append(int(operation[1]))
            q = left + q[expect_loc:]
            continue
        if not q:
            continue
        if operation[1] == '-1':
            q = q[1:]
        else:
            q.pop()
    return [q[-1], q[0]] if q else [0, 0]
