package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class baekjoon11047 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int dp[] = new int[k + 1];
        int coin[] = new int[n];
        for (int i = 0; i < n; i++) {
            coin[i] = sc.nextInt();
        }
        Arrays.fill(dp, 987654321);
        for (int i = 0; i < n; i++) {
            for (int j = coin[i]; j < k + 1; j++) {
                if (j == coin[i]) dp[j] = 1;
                    //j원을 만드는데 드는 동전 개수와 dp[j-coin[i]]원을 만드는데 드는 동전 +1 개중 작은걸 택하기
                else dp[j] = Math.min(dp[j - coin[i]] + 1, dp[j]);
            }
        }
            System.out.println(dp[k]);
    }
}
