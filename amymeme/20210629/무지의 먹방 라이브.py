def next_turn(food_times, cur_turn):
    length = len(food_times)
    diff = 1
    while food_times[(cur_turn + diff) % length] == 0:
        diff += 1
    return (cur_turn + diff) % length


def solution(food_times, k):
    turn = 0
    while k:
        food_times[turn] -= 1
        if not any(food_times):
            break
        turn = next_turn(food_times, turn)
        k -= 1
    if not any(food_times):
        return -1
    else:
        return turn + 1
