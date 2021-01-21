import java.util.*;

public class baekjoon14502 {
    static class VirusDot {
        int x;
        int y;

        public VirusDot(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int n;
    static int m;
    static int center[][];
    static int copiedmap[][];
    static ArrayList<Integer> safezone;
    static ArrayList<VirusDot> virusList = new ArrayList<VirusDot>();
    static int x[] = {-1, 1, 0, 0};
    static int y[] = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        m = scan.nextInt();
        safezone = new ArrayList<Integer>();
        center = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                center[i][j] = scan.nextInt();
                if (center[i][j] == 2) {
                    virusList.add(new VirusDot(i, j));
                }
            }
        }
        wall(0, 0);
        System.out.println(Collections.max(safezone));

    }

    static void wall(int wall_count, int start) {
        if (wall_count == 3) {
            //새로운 맵에 바이러스 퍼뜨리기 (기존 연구소에 영향 안가게)
            copiedmap = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    copiedmap[i][j] = center[i][j];
                }
            }
            //바이러스 퍼뜨리기
            for (VirusDot virus : virusList) {
                spreadVirus(virus.x, virus.y);
            }

            safezone.add(safeCount());
            return;
        }
        for (int i = start; i < n * m; i++) {
            //x행 y열 
            int x = i / m;
            int y = i % m;
            if (center[x][y] == 0) {
                center[x][y] = 1;
                //depth 3번될때까지
                wall(wall_count + 1, i + 1);
                //한 번 safezone계산 완료 후에 다시 계산하기 위해 center원상 복귀
                center[x][y] = 0;
            }
        }
    }

    static void spreadVirus(int i, int j) {
        for (int direction = 0; direction < 4; direction++) {
            int nearx = i + x[direction];
            int neary = j + y[direction];
            if (0 <= nearx && nearx < n && 0 <= neary && neary < m) {
                if (copiedmap[nearx][neary] == 0) {
                    copiedmap[nearx][neary] = 2;
                    spreadVirus(nearx, neary);
                }
            }
        }
    }

    static int safeCount() {
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (copiedmap[i][j] == 0) {
                    count++;
                }
            }
        }
        return count;
    }

}
