# 백준 #1874
# https://www.acmicpc.net/problem/1874

import sys

n = sys.stdin.readline().strip()
challenges = []
for challenge in sys.stdin:
    challenges.append(int(challenge.strip()))

inputs = []
for i in range(1, int(n)+1):
    inputs.append(i)

my_stack = []
operations = ""

while challenges:
    if my_stack:
        if my_stack[-1] != challenges[0]:
            if inputs :
                my_stack.append(inputs.pop(0))
                operations += "+"
            else:
                break
        else:
            my_stack.pop(-1)
            operations += "-"
            challenges.pop(0)
    else:
        if inputs :
            my_stack.append(inputs.pop(0))
            operations += "+"
        else:
            break
if my_stack:
    print("NO")
else:
    for op in operations:
        print(op)

# ------------ 이후 수정 ------------ #

import sys

n = int(sys.stdin.readline())
my_stack = []
operations = ""
i = 1

for _ in range(n):
    challenge = int(sys.stdin.readline())
    while i <= challenge:
        my_stack.append(i)
        operations += "+"
        i += 1
    if my_stack[-1] == challenge:
        my_stack.pop(-1)
        operations += "-"
    else:
        break

if my_stack:
    print("NO")
else:
    for op in operations:
        print(op)