import java.util.Arrays;
import java.util.Scanner;

// https://fbtmdwhd33.tistory.com/21 참고 - 분할정복 문제
/*
* 일단 가장 작은 3*3부터 생각한다.
* 이후 크기를 늘려가면서 다음 블록으로 넘어가는 것도 고려한다.
* */

public class baekjoon2447 {
    static char[][] stars;

    static public void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        stars = new char[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(stars[i], ' ');
        }
        printStar(0,0,n);
        for (int i = 0; i < n; i++) {
            System.out.println(stars[i]);
        }


    }

    static void printStar(int x, int y, int n) {
        int div = 0;
        //크기가 1이면 별찍기 (3*3 별에서)
        if (n == 1) {
            stars[x][y] = '*';
            return;
        }
        div = n / 3;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 1 && j == 1) continue;
                // 다음 블록으로 넘어가야 함
                printStar(x+(div*i), y+(div*j), div);
            }
        }

    }

}

