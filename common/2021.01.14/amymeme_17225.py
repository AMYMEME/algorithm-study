import sys

A, B, N = map(int, sys.stdin.readline().split())
blue_end_time = 0
blue_result = []
red_end_time = 0
red_result = []
total_present_num = 0
# (start_time, color)
todo_list = []

for _ in range(N):
    time, color, num = sys.stdin.readline().split()
    if color == 'B':
        # 아직 하고 있는 중이라면, 작업 끝나는 시각을 다음 시작각 시으로, 아니라면 현재 시각을 시작 시각으로
        next_start_time = blue_end_time if blue_end_time > int(time) else int(time)
        blue_end_time = next_start_time + A * int(num)
        for i in range(int(num)):
            todo_list.append((next_start_time + A * i, color))
    elif color == 'R':
        next_start_time = red_end_time if red_end_time > int(time) else int(time)
        red_end_time = next_start_time + B * int(num)
        for i in range(int(num)):
            todo_list.append((next_start_time + B * i, color))
todo_list.sort()
for (start_time, color) in todo_list:
    total_present_num += 1
    if color == 'B':
        blue_result.append(total_present_num)
    else:
        red_result.append(total_present_num)

print(len(blue_result))
print(" ".join(str(b) for b in blue_result))
print(len(red_result))
print(" ".join(str(r) for r in red_result))
