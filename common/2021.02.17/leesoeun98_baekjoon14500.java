package BOJ;

import java.util.Scanner;

public class baekjoon14500 {
    static int n;
    static int m;
    static int board[][];
    static boolean check[][];
    static int result = 0;
    static int directionx[] = {-1, 1, 0, 0};
    static int directiony[] = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        board = new int[n][m];
        check = new boolean[n][m];
        for (int col = 0; col < n; col++) {
            for (int row = 0; row < m; row++) {
                board[col][row] = sc.nextInt();
                check[col][row] = false;
            }
        }
        for (int col = 0; col < n; col++) {
            for (int row = 0; row < m; row++) {
                check[col][row] = true;
                dfs(1, board[col][row], col, row);
                check[col][row] = false;
            }
        }
        // ㅜ
        for (int col = 0; col < n - 1; col++) {
            for (int row = 0; row < m - 2; row++) {
                int sum_result = board[col][row] + board[col][row + 1] + board[col][row + 2] + board[col + 1][row + 1];
                result = Math.max(sum_result, result);
            }
        }
        // ㅏ
        for (int col = 0; col < n - 2; col++) {
            for (int row = 0; row < m - 1; row++) {
                int sum_result = board[col][row] + board[col + 1][row] + board[col + 2][row] + board[col + 1][row + 1];
                result = Math.max(sum_result, result);
            }
        }
        // ㅓ
        for (int col = 0; col < n - 2; col++) {
            for (int row = 0; row < m - 1; row++) {
                int sum_result = board[col][row+1] + board[col + 1][row+1] + board[col + 2][row+1] + board[col+1][row];
                result = Math.max(sum_result, result);
            }
        }
        // ㅗ
        for (int col = 0; col < n - 1; col++) {
            for (int row = 0; row < m - 2; row++) {
                int sum_result = board[col + 1][row] + board[col + 1][row + 1] + board[col + 1][row + 2] + board[col][row + 1];
                result = Math.max(sum_result, result);
              //  System.out.println(sum_result);
            }
        }
        System.out.println(result);
    }

    static void dfs(int depth, int sum_result, int x, int y) {
        if (depth == 4) {
            result = Math.max(result, sum_result);
            return;
        }
        for (int i = 0; i < 4; i++) {
            int nearx = x + directionx[i];
            int neary = y + directiony[i];
            if (nearx < 0 || nearx > n - 1 || neary < 0 || neary > m - 1) continue;
            if (check[nearx][neary] == false) {
                check[nearx][neary] = true;
                dfs(depth + 1, sum_result + board[nearx][neary], nearx, neary);
                check[nearx][neary] = false;
            }
        }
    }

}
