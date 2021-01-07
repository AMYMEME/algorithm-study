'''
https://www.acmicpc.net/problem/10828

'''

from sys import stdin

stack, result = [], []


def push(item):
    return stack.append(item)


def pop():
    result.append(stack.pop()) if stack else result.append(-1)


def size():
    result.append(len(stack))


def empty():
    result.append(0) if stack else result.append(1)


def top():
    result.append(stack[-1]) if stack else result.append(-1)


if __name__ == "__main__":

    command_num = int(stdin.readline())

    for _ in range(command_num):
        command = stdin.readline().split()

        if (command[0] == "push"):
            push(command[1])
        else:
            globals()[command[0]]()

    for item in result:
        print(item)
