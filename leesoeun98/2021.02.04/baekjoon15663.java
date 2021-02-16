package BOJ;

import java.lang.reflect.Array;
import java.util.*;

public class baekjoon15663 {
    static int result[];
    static ArrayList<Integer> numarray;
    static int isVisited[]=new int[10001];
    static int n;
    static int m;

    static public void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        HashSet<Integer> numset = new HashSet<>();
        for (int i = 0; i < n; i++) {
            int num =sc.nextInt();
            numset.add(num);
            isVisited[num]++;
        }
        result = new int[m];
        numarray = new ArrayList<>(numset);
        Collections.sort(numarray);
        printcombi(0);
    }

    static void printcombi(int depth) {
        if (depth == m) {
            for (int r : result) {
                System.out.print(r + " ");
            }
            System.out.println();
            return;
        }
        for(int i=0;i<numarray.size();i++){
            if(isVisited[numarray.get(i)]>0){
                isVisited[numarray.get(i)]-=1;
                result[depth]=numarray.get(i);
                printcombi(depth+1);
                isVisited[numarray.get(i)]+=1;
            }
        }

    }
}
