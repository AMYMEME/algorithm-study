# https://programmers.co.kr/learn/courses/30/lessons/64063
# 호텔 방 배정

def solution(k, room_number):
    answer = [0] * len(room_number)
    empty_rooms = [True] * (k + 1)
    for idx, want in enumerate(room_number):
        while not empty_rooms[want]:
            want += 1
        empty_rooms[want] = False
        answer[idx] = want

    return answer
