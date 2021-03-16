package BOJ;

import java.util.Scanner;

public class baekjoon9251 {
    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String first = sc.next();
        String second = sc.next();
        int dp[][] = new int[first.length() + 1][second.length() + 1];

        //문자열의 각 문자를 비교하다가 문자가 같으면 이전거의 +1
        //같지 않으면 이전행, 이전 열 중에서 최대를 갖고 오면 된다.
        // => 이런 문제는 표를 그려서 점화식을 찾는다.
        for (int i = 1; i <= first.length(); i++) {
            for (int j = 1; j <= second.length(); j++) {
                if (first.charAt(i - 1) == second.charAt(j - 1)){
                    dp[i][j]=dp[i-1][j-1]+1;
                } else {
                    dp[i][j]=Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        System.out.println(dp[first.length()][second.length()]);
    }
}
