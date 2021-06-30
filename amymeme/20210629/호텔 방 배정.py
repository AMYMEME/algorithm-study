# https://programmers.co.kr/learn/courses/30/lessons/64063
# https://m.blog.naver.com/js568/221957852279 참고
# 호텔 방 배정

import sys

sys.setrecursionlimit(10000)  # 재귀 허용깊이 임의로 지정

rooms = dict()


def solution(k, room_number):
    for num in room_number:
        find_empty(num)
    return list(rooms.keys())


def find_empty(chk):  # 재귀함수
    global rooms
    if chk not in rooms.keys():  # 빈 방이면
        rooms[chk] = chk + 1  # rooms에 새 노드 추가
        return chk  # 요청한 방
    empty = find_empty(rooms[chk])  # 재귀함수 호출
    rooms[chk] = empty + 1  # (배정된 방+1)을 부모노드로 변경
    return empty  # 새로 찾은 빈 방
