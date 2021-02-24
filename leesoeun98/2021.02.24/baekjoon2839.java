package BOJ;

import java.util.Scanner;

public class baekjoon2839 {
    static int weight[] = {3, 5};
    static int dp[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        dp = new int[n + 1];
        for(int i=1;i<=n;i++){ //dp[0]=0이 되도록 
            dp[i]=987654321;
        }
        for (int i = 0; i < 2; i++) {
            for (int j = weight[i]; j <= n; j++) {
                dp[j]=Math.min(dp[j], dp[j-weight[i]]+1);
            }
        }
        if(dp[n]==987654321) System.out.println(-1);
        else System.out.println(dp[n]);
    }
}
