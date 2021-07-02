# https://programmers.co.kr/learn/courses/30/lessons/64062
# 징검다리 건너기
def solution(stones, k):
    answer = 0
    while True:
        cnt = 0
        for idx, stone in enumerate(stones):
            if stone:
                stones[idx] = stone - 1
                cnt = 0
            else:
                cnt += 1
                if cnt >= k:
                    return answer
        answer += 1
