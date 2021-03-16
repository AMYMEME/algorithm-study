package BOJ;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class baekjoon1874 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num = 1;
        Stack<Integer> numStack = new Stack();
        boolean isPossible = true;
        int numarray[] = new int[n];
        ArrayList<Character> answer = new ArrayList<>();

        /*
         * num이 numarray[i]보다 작으면 +, push
         * stack의 top이 numarray[i]보다 크거나 같으면 -, pop
         * stack이 empty면 불가 (같은 수가 두번 나왔거나...)
         * */

        for (int i = 0; i < n; i++) {
            numarray[i] = sc.nextInt();
            if (isPossible) {
                if (num <= numarray[i]) {
                    while(num<=numarray[i]){
                        numStack.push(num++);
                        answer.add('+');
                    }
                }
                if(numStack.isEmpty()) isPossible=false;
                else{
                    while(numStack.peek()>=numarray[i]){
                        numStack.pop();
                        answer.add('-');
                        if(numStack.isEmpty()) break;
                    }
                }
            }
        }
        if(isPossible){
            for(Character c: answer) System.out.println(c);
        }
        if(!isPossible) System.out.println("NO");
    }
}
