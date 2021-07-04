# https://programmers.co.kr/learn/courses/30/lessons/12979
# 기지국 설치

def solution(n, stations, w):
    answer = 0
    apts = [False] * n

    for station in stations:
        l = station - 1 - w if station - w > 1 else 0
        r = station - 1 + w if station + w < n else n - 1
        apts[l:r+1] = [True] * (r-l+1)

    cnt = 0
    for flag in apts:
        if flag:
            answer = answer + (cnt - 1) // (2 * w + 1) + 1
            cnt = 0
        else:
            cnt += 1
    if cnt:
        answer = answer + (cnt - 1) // (2 * w + 1) + 1

    return answer
