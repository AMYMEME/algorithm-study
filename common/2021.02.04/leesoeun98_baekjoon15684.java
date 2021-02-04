package BOJ;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class baekjoon15684 {
    static int ladder[][];

    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int h = sc.nextInt();
        ladder = new int[h + 1][n];
        for (int i = 0; i < m; i++) {
            int col = sc.nextInt();
            int row = sc.nextInt();
            //오른쪽에 가로선이면 1, 왼쪽에 가로선이면 -1
            ladder[col - 1][row - 1] = 1;
            ladder[col - 1][row] = -1;
        }
        if (ladderCount(n, h) > 3) {
            System.out.println("-1");
            return;
        } else {
            for (int i = 0; i <= 3; i++) {
                if (dfs(0, 0, 0, i, n, h)) return;
            }
        }
        System.out.println("-1");
    }

    static boolean dfs(int x, int y, int depth, int size, int n, int h) {
        if (depth == size) {
            if (ladderCheck(n, h)) {
                System.out.println(size);
                return true;
            }
            return false;
        }
        for (int i = y; i < n - 1; i++) {
            for (int j = x; j < h; j++) {
                //이미 사다리 있으면 가로선 못 그으므로 continue
                if (ladder[j][i] != 0 || ladder[j][i + 1] != 0) continue;
                else {
                    ladder[j][i] = 1;
                    ladder[j][i + 1] = -1;
                    //다음 실행도 true라면 true반환
                    if (dfs(i + 2, j, depth + 1, size, n, h)) return true;
                    ladder[j][i] = 0;
                    ladder[j][i + 1] = 0;
                }
            }
            y = 0; //맨 위부터 탐색해야 하므로
        }
        return false;
    }

    static boolean ladderCheck(int n, int h) {
        //각자 번호가 자기 자신으로 가는지
        for (int i = 0; i < n; i++) {
            int neary=i;
            for (int nearx = 0; nearx <= h; nearx++) {
                //오른쪽에 선이 있으면 다음 세로선으로 이동
                if(ladder[nearx][neary]==1) neary++;
                else if(ladder[nearx][neary]==-1) neary--;
            }
            //사다리 다 탔는데 자기 자신이면 true
            if(neary==i) return true;
        }
        return false;
    }

    static int ladderCount(int n, int h) {
        //각 세로선에 대해 가로선의 개수가 홀수인 것이 3개보다 많으면
        //그어야 할 가로선이 3개 초과이므로 불가
        int count = 0;
        for (int i = 0; i < n - 1; i++) {
            int cnt = 0;
            for (int j = 0; j < h; j++) {
                if (ladder[j][i] == 1) cnt++;
            }
            if (cnt % 2 == 1) count++;
        }
        return count;
    }
}
