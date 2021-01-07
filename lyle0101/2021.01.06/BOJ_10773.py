'''
https://www.acmicpc.net/problem/10773

'''

from sys import stdin

stack = []
item_num = int(stdin.readline())

for _ in range(item_num):
    item = int(stdin.readline())
    if (item == 0):
        stack.pop()
    else:
        stack.append(item)

print(sum(stack))
