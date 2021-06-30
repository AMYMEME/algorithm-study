def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    foods = []
    for idx, value in enumerate(food_times):
        foods.append((value, idx + 1))
    foods.sort()

    bottom = 0
    n = len(foods)

    for idx, (value, number) in enumerate(foods):
        if k < (value - bottom) * n:
            numbers = list(map(lambda x: x[1], foods[idx:]))
            numbers.sort()
            order = k % len(numbers)
            return numbers[order]
        k -= (value - bottom) * n
        bottom = value
        n -= 1
