package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class baekjoon1339 {

    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] arr = new String[n];
        int[] alpha = new int[26];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.next();
            int temp = (int) Math.pow(10, arr[i].length() - 1); // 예로 10^4
            for (int j = 0; j < arr[i].length(); j++) {
                alpha[arr[i].charAt(j) - 65] += temp;
                temp /= 10;
            }
        }
        Arrays.sort(alpha); // 오름차순 정렬
        int num=9;
        int sum=0;
        for (int i = 25; i >= 0; i--) {
            if (alpha[i] == 0) {
                break;
            } else {
                sum+=alpha[i]*num;
                num--;
            }
        }
        System.out.println(sum);
    }
}
