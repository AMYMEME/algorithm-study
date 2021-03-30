package BOJ;

import java.util.Scanner;

public class baekjoon17822 {
    static int n, m, t;
    static int board[][];
    static int copy[][];
    static int same_count;
    static int answer;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        t = sc.nextInt();
        board = new int[n + 1][m];
        copy = new int[n + 1][m];
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < m; j++) {
                board[i][j] = sc.nextInt();
            }
        }
        for (int i = 0; i < t; i++) {
            int x = sc.nextInt();
            int idx = 1;
            int d = sc.nextInt();
            int k = sc.nextInt();
            if (d == 0) {
                //배수 회전
                while (idx * x <= n) {
                    for (int rotate = 0; rotate < k; rotate++) {
                        rightRotate(idx * x);
                    }
                    idx++;
                }
            } else {
                while (idx * x <= n) {
                    for (int rotate = 0; rotate < k; rotate++) {
                        leftRotate(idx * x);
                    }
                    idx++;
                }
            }
            //copy
            for (int row = 1; row <= n; row++) {
                for (int col = 0; col < m; col++) {
                    copy[row][col] = board[row][col];
                }
            }
            // 인접 수 지우기
            remove();
        }

        // 결과 출력
        for (int[] temp : copy) {
            for (int t : temp) {
                answer += t;
                System.out.print(t);
            }
            System.out.println();
        }
        System.out.println(answer);
    }

    public static void leftRotate(int x) {
        int temp = board[x][0];
        for (int i = 1; i <= board[x].length - 1; i++) {
            board[x][i - 1] = board[x][i];
        }
        board[x][board[x].length - 1] = temp;
    }

    public static void rightRotate(int x) {
        int temp = board[x][board[x].length - 1];
        for (int i = board[x].length - 1; i >= 1; i--) {
            board[x][i] = board[x][i - 1];
        }
        board[x][0] = temp;
    }

    public static void remove() {
        for (int row = 1; row <= n - 1; row++) {
            for (int col = 0; col < m - 1; col++) {
                if (board[row][col] == board[row + 1][col]) {
                    copy[row][col] = 0;
                    copy[row + 1][col] = 0;
                    same_count++;
                } else if (board[row][col] == board[row][col + 1]) {
                    copy[row][col] = 0;
                    copy[row][col + 1] = 0;
                    same_count++;
                }
            }
        }
        // 인접 수 없으면 평균 +-1
        if (same_count == 0) {
            int sum = 0;
            int count = 0;
            double avg = 0;
            for (int[] arr : copy) {
                for (int a : arr) {
                    sum += a;
                    count++;
                }
            }
            avg = sum / (double) count;
            for (int i = 1; i <= n; i++) {
                for (int j = 0; j < m; j++) {
                    if (copy[i][j] > avg) copy[i][j] -= 1;
                    else if (copy[i][j] < avg) copy[i][j] += 1;
                }
            }
        }
    }
}
