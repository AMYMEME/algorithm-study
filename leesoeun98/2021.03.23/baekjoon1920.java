package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class baekjoon1920 {
    static int n, m;
    static int[] numbers;
    static int[] finds;

    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = sc.nextInt();
        }
        Arrays.sort(numbers);

        m = sc.nextInt();
        finds = new int[m];
        for (int i = 0; i < m; i++) {
            finds[i] = sc.nextInt();
            System.out.println(binarySearch(finds[i]));
        }
    }

    static int binarySearch(int x) {
        int left = 0;
        int right = n - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (x == numbers[mid]) return 1;
            else {
                if (x < numbers[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        return 0;
    }
}
