# https://programmers.co.kr/learn/courses/30/lessons/81303
# 표 편집

def solution(n, k, cmd):
    answer = ['O'] * n
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    stack = []
    cur_idx = k

    for c in cmd:
        if c[0] == 'D':
            for _ in range(int(c.split(' ')[1])):
                cur_idx = linked_list[cur_idx][1]
        elif c[0] == 'U':
            for _ in range(int(c.split(' ')[1])):
                cur_idx = linked_list[cur_idx][0]
        elif c[0] == 'C':
            prev, nxt = linked_list[cur_idx]
            answer[cur_idx] = 'X'
            stack.append((cur_idx, prev, nxt))

            if prev == -1:
                linked_list[nxt][0] = prev
            elif nxt == n:
                linked_list[prev][1] = nxt
            else:
                linked_list[prev][1] = nxt
                linked_list[nxt][0] = prev
            cur_idx = prev if nxt == n else nxt
        else:  # Z
            removed, removed_prev, removed_nxt = stack.pop()
            answer[removed] = 'O'
            if removed_prev == -1:
                linked_list[removed_nxt][0] = removed
            elif removed_nxt == n:
                linked_list[removed_prev][1] = removed
            else:
                linked_list[removed_prev][1] = removed
                linked_list[removed_nxt][0] = removed
    return ''.join(answer)
