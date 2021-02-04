package BOJ;

import javax.swing.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class baekjoon17144 {
    static class Dust {
        int x;
        int y;
        int dust;

        public Dust(int x, int y, int dust) {
            this.x = x;
            this.y = y;
            this.dust = dust;
        }
    }

    static class CleanerLocation {
        int x;
        int y;

        public CleanerLocation(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int room[][];
    static int copiedmap[][];
    //위 아래 오 왼
    static int directionx[] = new int[]{0, 0, 1, -1};
    static int directiony[] = new int[]{-1, 1, 0, 0};
    static int[] ccw = {2, 0, 3, 1}; //반시계
    static int[] cw = {2, 1, 3, 0}; // 시계
    static ArrayList<CleanerLocation> cleaner = new ArrayList<>();
    static int r;
    static int c;

    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        r = sc.nextInt();
        c = sc.nextInt();
        int t = sc.nextInt();
        int sum = 0;
        room = new int[r][c];
        copiedmap=new int[r][c];
        for (int col = 0; col < r; col++) {
            for (int row = 0; row < c; row++) {
                room[col][row] = sc.nextInt();
                if (room[col][row] == -1) {
                    cleaner.add(new CleanerLocation(row, col));
                }
            }
        }

        for (int time = 0; time < t; time++) {
            //1. 미세먼지 확산
            spread();
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    copiedmap[i][j] = room[i][j];
                }
            }
            //반시계 회전
            circulate(cleaner.get(0).x, cleaner.get(0).y, ccw);
            //시계 회전
            circulate(cleaner.get(1).x, cleaner.get(1).y, cw);
        }

        for (int col = 0; col < r; col++) {
            for (int row = 0; row < c; row++) {
                if(room[col][row]!=-1) sum+=room[col][row];
            }
        }
        System.out.println(sum);
    }


    static void spread() {
        Queue<Dust> q = new LinkedList<>();
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (room[i][j] > 4) {
                    //x, y 헷갈리지 말기!!!
                    q.add(new Dust(j, i, room[i][j]));
                }
            }
        }
        while (!q.isEmpty()) {
            Dust dust = q.poll();
            int cnt = 0;
            int spreaddust = dust.dust / 5;
            for (int direction = 0; direction < 4; direction++) {
                int nearx = dust.x + directionx[direction];
                int neary = dust.y + directiony[direction];
                if (0 <= nearx && nearx < c && 0 <= neary && neary < r) {
                    //공기청정기 없으면 확산
                    if (room[neary][nearx] != -1) {
                        cnt++;
                        room[neary][nearx] += spreaddust;
                    }
                }
            }
            room[dust.y][dust.x] -= spreaddust * cnt;
        }
    }

    static void circulate(int cleanerx, int cleanery, int[] direction) {
        int y=cleanery;
        int x=cleanerx+1;
        //공기청정기에서 나온 바람은 먼지가 0
        room[y][x]=0;
        for (int k = 0; k < 4; k++) {
            while (true) {
                int nearx = x + directionx[direction[k]];
                int neary = y + directiony[direction[k]];
                if (!(0 <= nearx && nearx < c && 0 <= neary && neary < r)) break;
                //cleaner에 도달 시 회전 종료
                if(cleanerx==nearx && cleanery==neary) break;
                //copiedmap의 먼지가 room의 한 칸 이동한걸로 이동
                room[neary][nearx]=copiedmap[y][x];
                //한칸이동
                x=nearx;
                y=neary;
            }
        }
    }

}
