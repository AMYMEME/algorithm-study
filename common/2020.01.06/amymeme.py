import sys

sys.stdin.readline(); # dismiss first loop count

for line in sys.stdin:
    stack_count = 0
    end_flag = False

    for char in line:
        if char == '(':
            stack_count += 1
        if char == ')':
            if stack_count < 1:
                end_flag = True
                break
            else:
                stack_count -= 1
    if end_flag:
        print("NO")
    else:
        if stack_count == 0:
            print("YES")
        else:
            print("NO")
