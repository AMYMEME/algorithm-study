# https://programmers.co.kr/learn/courses/30/lessons/42888
# 오픈채팅방

def solution(record):
    answer = []
    users = dict()
    logs = []

    for row in record:
        row = row.split(' ')
        if row[0] == 'Leave':
            logs.append((row[1], '님이 나갔습니다.'))
            continue
        users[row[1]] = row[2]
        if row[0] == 'Enter':
            logs.append((row[1], '님이 들어왔습니다.'))

    print(logs)
    for uid, event in logs:
        answer.append("{0}{1}".format(users[uid], event))
    return answer
