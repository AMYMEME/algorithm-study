def greedy(string):
    stack = []
    cnt = 0
    while string:
        stack.append(string.pop())
        if len(stack) >= 3 and stack[-1] == '1' and stack[-2] == '1' and stack[-3] == '0':
            stack.pop()
            stack.pop()
            stack.pop()
            cnt += 1
    stack = ''.join(reversed(stack))
    loc = stack.find('111')
    if loc != -1:
        return stack[:loc] + '110' * cnt + stack[loc:]
    loc = stack.rfind('11')
    if loc != -1:
        return stack[:loc] + '110' * cnt + stack[loc:]
    loc = stack.rfind('0')
    return stack[:loc] + '110' * cnt + stack[loc:]


def solution(s):
    answer = []
    for string in s:
        answer.append(greedy(list(string)))
    return answer
