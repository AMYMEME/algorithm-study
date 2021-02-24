package BOJ;

import java.util.Scanner;

public class baekjoon12865 {

    static int n;
    static int k;
    static int weight[];
    static int value[];
    static int dp[][];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        weight = new int[n];
        value = new int[n];
        dp = new int[n + 1][k + 1];

        for (int i = 0; i < n; i++) {
            weight[i] = sc.nextInt();
            value[i] = sc.nextInt();
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                if (weight[i-1] <= j) dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - weight[i-1]] + value[i-1]);
                else dp[i][j] = dp[i - 1][j];
            }
        }
        System.out.println(dp[n][k]);
    }
}
