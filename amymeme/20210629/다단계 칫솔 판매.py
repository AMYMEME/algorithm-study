# https://programmers.co.kr/learn/courses/30/lessons/77486
# 다단계 칫솔 판매

from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []
    graph = defaultdict(str)  # 굳이 defaultdict 아니어도 됨
    bill = defaultdict(int)

    for idx, refer in enumerate(referral):
        graph[enroll[idx]] = refer

    persons = graph.keys()
    for idx, person in enumerate(seller):
        value = amount[idx] * 100
        while person in persons and value > 0:
            bill[person] += (value - value // 10)
            person = graph[person]
            value //= 10

    for p in enroll:
        answer.append(bill[p])
    return answer
