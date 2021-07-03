#문제 : https://www.acmicpc.net/problem/7596
/* 구상
익은 날짜 저장
3차원 BFS
*/
def solution():
    cnt = 1
    while True:
        N = int(input())
        if not N:
            break
        array = []

        for i in range(N):
            array.append(str(input()))

        array.sort()
        print(cnt)
        cnt += 1

        for i in array:
            print(i)