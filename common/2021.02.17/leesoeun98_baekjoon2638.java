package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class baekjoon2638 {
    static int n;
    static int m;
    static int cheese[][];
    static boolean visited[][];
    static int time = 0;
    static int count = 0;
    static int directionx[] = {-1, 1, 0, 0,};
    static int directiony[] = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        cheese = new int[n][m];

        for (int col = 0; col < n; col++) {
            for (int row = 0; row < m; row++) {
                int c = sc.nextInt();
                cheese[col][row] = c;
                if (c == 1) count++;
            }
        }

        while (count != 0) {
            visited = new boolean[n][m];
            for (int col = 0; col < n; col++) {
                for (int row = 0; row < m; row++) {
                    if (cheese[col][row] == 1 && !visited[col][row]) dfs(col, row);
                }
            }
            visited = new boolean[n][m];
            isOut(0,0);
            for (int col = 0; col < n; col++) {
                for (int row = 0; row < m; row++) {
                    cheese[col][row] = cheese[col][row] == 3 ? 2 : cheese[col][row];
                }
            }
            time++;
        }
        System.out.println(time-1);
    }

    static void dfs(int x, int y) {
        visited[x][y] = true;
        if (cheese[x][y] == 1 && isMelted(x, y)) {
            count--;
            //녹은 치즈는 3으로
            cheese[x][y] = 3;
        }
        for (int i = 0; i < 4; i++) {
            int nearx = x + directionx[i];
            int neary = y + directiony[i];
            if (nearx < 0 || nearx > n - 1 || neary < 0 || neary > m - 1) continue;
            if (cheese[nearx][neary] == 0 || visited[nearx][neary]) continue;
            dfs(nearx, neary);
        }
    }

    static void isOut(int x, int y) {
        visited[x][y] = true;
        //외부랑 접촉하는 곳은 2로
        cheese[x][y] = 2;
        for (int i = 0; i < 4; i++) {
            int nearx = x + directionx[i];
            int neary = y + directiony[i];
            if (nearx < 0 || nearx > n - 1 || neary < 0 || neary > m - 1) continue;
            if (cheese[nearx][neary] == 1 || visited[nearx][neary]) continue;
            cheese[nearx][neary] = 2;
            isOut(nearx, neary);
        }
    }

    static boolean isMelted(int x, int y) {
        int aircount = 0;
        for (int i = 0; i < 4; i++) {
            int nearx = x + directionx[i];
            int neary = y + directiony[i];
            if (nearx < 0 || nearx > n - 1 || neary < 0 || neary > m - 1) continue;
            if (cheese[nearx][neary] == 2) {
                aircount++;
            }
        }
        if (aircount >= 2) {
            return true;
        } else return false;
    }
}
