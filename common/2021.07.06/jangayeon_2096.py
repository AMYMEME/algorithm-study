#문제 : https://www.acmicpc.net/problem/2096
/*구상 : 동적프로그래밍
2차원 배열로
점화식 : D[i][0] = max(D[i-1][0], D[i-1][1]) + arr[0] */
