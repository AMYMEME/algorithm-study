package BOJ;

import java.util.Scanner;

public class baekjoon10830 {
    static int n;
    static long b;
    static int[][] arr;
    static long[][] newarr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        b = sc.nextLong();
        arr = new int[n][n];
        newarr = new long[n][n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        newarr = multipleMatrix(b);
        for(long[] ar:newarr){
            for(long a: ar){
                System.out.print(a+" ");
            }
            System.out.println();
        }
    }

    static long[][] multipleMatrix(long b) {
        long[][] rMatrix = new long[n][n];
        long[][] temp = new long[n][n];
        //b가1이면 그대로
        if (b == 1) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    rMatrix[i][j] = arr[i][j] % 1000;
                }
            }
        }
        //b가 짝수면 b/2 행렬을 곱한다.
        else if (b % 2 == 0) {
            temp = multipleMatrix(b / 2);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < n; k++) {
                        rMatrix[i][j] += (temp[i][k] * temp[k][j]) % 1000;
                    }
                    rMatrix[i][j] %= 1000;
                }
            }
        }
        //b가 홀수면 ^b-1 행렬과 ^1 행렬을 곱한다.
        else {
            temp = multipleMatrix(b - 1);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < n; k++) {
                        rMatrix[i][j] += (temp[i][k] * arr[k][j]) % 1000;
                    }
                    rMatrix[i][j] %= 1000;
                }
            }
        }
        return rMatrix;
    }
}
