package BOJ;

import java.util.Scanner;

public class baekjoon1463 {
    static int dp[];

    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        dp = new int[n + 1];
        dp[0]=0;
        dp[1]=0;
        for (int j = 2; j <= n; j++) {
            dp[j] = dp[j - 1] + 1;
            if (j % 3 == 0) dp[j] = Math.min(dp[j], dp[j / 3] + 1); //만약 j가 6이면, min(dp[5], dp[2]+1)로 후자가 선택된다.
            if (j % 2 == 0) dp[j] = Math.min(dp[j], dp[j / 2] + 1); //else if 쓰면 틀림..3으로 나누고 또 2로 나누는 경우가 존재하므로
        }
        System.out.println(dp[n]);
    }
}
