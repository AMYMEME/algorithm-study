package BOJ;

import java.util.ArrayList;
import java.util.Scanner;

public class baekjoon12865 {
    static class Bag {
        int weight;
        int value;

        Bag(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }

    static int n;
    static int k;
    static Bag elements[];
    static boolean isSelected[];
    static int maxResult = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        elements = new Bag[n];
        isSelected = new boolean[n];
        k = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int weight = sc.nextInt();
            int value = sc.nextInt();
            elements[i] = new Bag(weight, value);
        }
        dfs(0, 0, 0);
        System.out.println(maxResult);
    }

    static void dfs(int current_weight, int current_value, int index) {
        if (current_weight > k) {
            maxResult = Math.max(maxResult, current_value-elements[index].value);
            return;
        }
        for (int i = 0; i < n; i++) {
            isSelected[i] = true;
            dfs(current_weight + elements[i].weight, current_value + elements[i].value, i);
            isSelected[i] = false;
        }
    }
}
