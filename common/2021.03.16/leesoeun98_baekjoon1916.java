package BOJ;

import java.util.Arrays;
import java.util.Scanner;

public class baekjoon1916 {
    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int v = sc.nextInt(); // 노드 수 == 도시 수
        int e = sc.nextInt(); // 간선 수 == 버스 수
        int[][] adj = new int[v+1][v+1];
        for (int i = 0; i < e; i++) {
            adj[sc.nextInt()][sc.nextInt()] = sc.nextInt();
        }
        int start = sc.nextInt();
        int end = sc.nextInt();

        int distance[] = new int[v+1];
        boolean check[] = new boolean[v+1];
        Arrays.fill(distance, Integer.MAX_VALUE);

        //시작 노드 값 초기화
        distance[start] = 0;
        check[start] = true;

        //distance 갱신
        for(int i=1;i<v+1;i++){
            if(!check[i] && adj[start][i]!=0){
                distance[i]=adj[start][i];
            }
        }

        for (int a = 0; a < v - 1; a++) {
            int min = Integer.MAX_VALUE;
            int min_index = -1;
            //최소값 찾기
            for (int i = 1; i < v + 1; i++) {
                if (!check[i] && distance[i] < min) {
                        min = distance[i];
                        min_index = i;
                }
            }
            //check를 true로
            check[min_index]=true;
            //distance 배열 갱신
            for (int i = 1; i < v + 1; i++) {
                if (!check[i] && adj[min_index][i]!=Integer.MAX_VALUE && adj[min_index][i]!=0 && distance[i] > distance[min_index]+adj[min_index][i]) {
                    distance[i] = distance[min_index]+adj[min_index][i];
                }
            }
        }
        System.out.println(distance[end]);
    }
}
