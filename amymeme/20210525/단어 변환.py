from collections import deque


def compare(s1, s2):
    differ = 0
    for idx, char in enumerate(s1):
        if char != s2[idx]:
            differ += 1
        if differ > 1:
            break
    if differ > 1:
        return False
    return True


def solution(begin, target, words):
    q = deque([(begin, 0)])  # word, time
    visited = set()
    while q:
        cur_word, cnt = q.popleft()
        if cur_word == target:
            return cnt
        for word in words:
            if word in visited:
                continue
            if compare(word, cur_word):
                q.append((word, cnt + 1))
                visited.add(word)
    return 0
