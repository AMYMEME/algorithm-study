package BOJ;

import java.util.Scanner;

public class baekjoon4256 {
    static int preorder[];
    static int inorder[];

    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            preorder = new int[n];
            inorder = new int[n];
            for (int j = 0; j < n; j++) {
                preorder[j] = sc.nextInt();
            }
            for (int j = 0; j < n; j++) {
                inorder[j] = sc.nextInt();
            }
            postorder(0, n, 0);
            System.out.println();
        }
    }

    // left -> right -> root 순
    static void postorder(int start, int end, int root) {
        for (int i = start; i < end; i++) {
            if (inorder[i] == preorder[root]) {
                postorder(start, i, root + 1); //left subtree
                postorder(i + 1, end, i + root - start + 1); //right subtree
                System.out.print(preorder[root] + " ");// root 출력
            }
        }
    }
}
