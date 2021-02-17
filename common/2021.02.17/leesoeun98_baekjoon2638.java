package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class baekjoon2638 {
    static int n;
    static int m;
    static int cheese[][];
    static int copied[][];
    static int time = 0;
    static int directionx[] = {-1, 1, 0, 0,};
    static int directiony[] = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        cheese = new int[n][m];
        copied = new int[n][m];

        for (int col = 0; col < n; col++) {
            for (int row = 0; row < m; row++) {
                int c = sc.nextInt();
                cheese[col][row] = c;
                copied[col][row] = c;
            }
        }

        while (true) {
            boolean flag = false;

            for (int col = 0; col < n; col++) {
                for (int row = 0; row < m; row++) {
                    if (copied[col][row] == 1 && isMelted(col, row)) {
                        copied[col][row] = 0;
                        flag = true;
                    }
                }
            }
            time++;
            if (!flag) {
                System.out.println(time);
                break;
            }
        }

    }

    static boolean isMelted(int x, int y) {
        int count = 0;
        for (int i = 0; i < 4; i++) {
            int nearx = x + directionx[i];
            int neary = y + directiony[i];
            if (nearx < 0 || nearx > n - 1 || neary < 0 || neary > m - 1) continue;
            if (cheese[nearx][neary] == 0) {
                int countIsIn = 0;
                for (int j = 0; j < 4; j++) {
                    int nearxx = nearx + directionx[j];
                    int nearyy = neary + directiony[j];
                    if (nearxx < 0 || nearxx > n - 1 || nearyy < 0 || nearyy > m - 1) continue;
                    if (cheese[nearxx][nearyy] == 1) countIsIn++;
                }
                // countIsIn이 1보다 작으면 외부 0 인것
                if (countIsIn < 1) count++;
                count++;
            }
        }
        if (count >= 2) {
            return true;
        } else return false;
    }

}
