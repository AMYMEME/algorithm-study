package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class baekjoon1916 {

    static int v, e;
    static int[][] adj;
    static long distance[];
    static boolean check[];
    static int start, end;

    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        v = sc.nextInt(); // 노드 수 == 도시 수
        e = sc.nextInt(); // 간선 수 == 버스 수
        adj = new int[v + 1][v + 1];
        for (int[] arr : adj) Arrays.fill(arr, -1);
        for (int i = 0; i < e; i++) {
            int from = sc.nextInt();
            int to = sc.nextInt();
            int price = sc.nextInt();
            //여기 중요, 동일한 경로에 다양한 price 들어옴
            if (adj[from][to] == -1) {
                adj[from][to] = price;
            } else if (adj[from][to] > price) {
                adj[from][to] = price;
            }
        }
        start = sc.nextInt();
        end = sc.nextInt();

        distance = new long[v + 1];
        check = new boolean[v + 1];
        for(int i=1;i<=v;i++){
            //-1 해야함
            distance[i]=Integer.MAX_VALUE-1;
            check[i]=false;
        }
        dijkstra();
        System.out.println(distance[end]);
    }

    public static void dijkstra() {
        distance[start] = 0;

        for (int i = 0; i < v - 1; i++) {
            long min = Integer.MAX_VALUE;
            int from = -1;

            //min, minIndex 갱신
            for (int j = 1; j <= v; j++) {
                if (!check[j] && min > distance[j]) {
                    min = distance[j];
                    from = j;
                }
            }
            check[from] = true;

            for (int to = 1; to <= v; to++) {
                //-1 해야함
                if(distance[from]!=Integer.MAX_VALUE-1 && adj[from][to]!=-1 && distance[to]>distance[from]+adj[from][to]){
                    distance[to]=distance[from]+adj[from][to];
                }
            }
        }
    }
}
