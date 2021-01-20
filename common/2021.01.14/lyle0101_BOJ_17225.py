from sys import stdin

g_time = 1
gift_num = 1
g_gift_queue = []
A_gift_queue = []
B_gift_queue = []
is_A_active, is_B_active = False, False
is_A_working, is_B_working = 0, 0

A_speed, B_speed, num = map(int, stdin.readline().split())

for _ in range(num):
    c_time, c_color, c_num = stdin.readline().split()

    while(g_time != int(c_time)):
        if (is_A_working):
            is_A_working -= 1
        if (not is_A_working and is_A_active and g_gift_queue):
            A_gift_queue.append(g_gift_queue.pop(0))
            is_A_working += A_speed
        if (is_B_working):
            is_B_working -= 1
        if (not is_B_working and is_B_active and g_gift_queue):
            B_gift_queue.append(g_gift_queue.pop(0))
            is_B_working += B_speed
        g_time += 1

    for _ in range(int(c_num)):
        g_gift_queue.append(gift_num)
        gift_num += 1

    if (c_color == "B"):
        is_A_active = True
        if (not is_A_working):
            if (A_speed == 0):
                for _ in range(int(c_num)):
                    A_gift_queue.append(g_gift_queue.pop(0))
            else:
                A_gift_queue.append(g_gift_queue.pop(0))
                is_A_working += A_speed

    else:
        is_B_active = True
        if (not is_B_working):
            if (B_speed == 0):
                for _ in range(int(c_num)):
                    B_gift_queue.append(g_gift_queue.pop(0))
            else:
                B_gift_queue.append(g_gift_queue.pop(0))
                is_B_working += B_speed

print(len(A_gift_queue))
print(*A_gift_queue)
print(len(B_gift_queue))
print(*B_gift_queue)
