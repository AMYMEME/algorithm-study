def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.sort()
    rocks.append(distance)

    # mid 값 미만으로 제거하되, 그 중 거리 최솟값 따로 저장
    while left < right:
        mid = (left + right) // 2
        prev = 0
        remove_cnt = 0
        min_value = 1000000000

        for rock in rocks:
            # 제거 가능
            if rock - prev < mid:
                remove_cnt += 1
                if remove_cnt > n:
                    break
            else:
                min_value = min(min_value, rock - prev)
                prev = rock
        # 너무 많이 제거했으면 mid값을 줄여서 제거 rock을 줄여보기
        if remove_cnt > n:
            right = mid
        else:
            left = mid + 1
            answer = min_value
    return answer
