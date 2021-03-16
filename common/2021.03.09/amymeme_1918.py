# https://www.acmicpc.net/problem/1918
# 백준 1918 - 후위표기식
# 참고 : 자료구조 강의자료
"""
연산자 스택을 이용 !

피연산자(알파벳)를 만나면 그대로 출력
연산자 등장 시 스택(맨 마지막 pop) 연산자 우선순위보다 현재 연산자 우선순위가 높을 경우 그냥 넣음
그렇지 않을 경우엔 스택에서 빼서 출력(현재 연산자 우선순위 높아질때까지)
왼쪽 괄호는 우선순위 가장 낮은 취급 및 등장 시 연산자 스택에 넣음
오른쪽 괄호는 연산자는 아니지만, 등장시 스택에서 왼쪽 괄호 나오기 전까지 모두 출력
"""

import sys


def print_stack():
    global my_stack
    while my_stack:
        if my_stack[-1] == '(':
            my_stack.pop()
            return
        print(my_stack.pop(), end='')


infix_expression = sys.stdin.readline().strip()
operators_order = {'*': 0, '/': 0, '+': 1, '-': 1, '(': 2}
operators = operators_order.keys()
my_stack = []

for char in infix_expression:
    if char == ')':
        print_stack()
        continue
    if char == '(':
        my_stack.append(char)
        continue
    if char not in operators:  # operand
        print(char, end='')
        continue
    if my_stack and operators_order[my_stack[-1]] <= operators_order[char]:  # 현재 연산자 우선순위 낮으면 먼저 출력
        while my_stack and operators_order[my_stack[-1]] <= operators_order[char]:
            print(my_stack.pop(), end='')
    my_stack.append(char)
if my_stack:
    print_stack()
