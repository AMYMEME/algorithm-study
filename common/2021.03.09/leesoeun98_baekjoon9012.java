import java.util.Scanner;
import java.util.Stack;

public class baekjoon9012 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int count = scan.nextInt();
        scan.nextLine();

        for (int i = 0; i < count; i++) {
            String ps = scan.next();
            Stack pstack = new Stack();
			boolean answer = true;

			/*
			 *  ( 면 stack에 넣기
			 *  ) 인데 비어져있으면 no
			 *    인데 ( 있으면 빼기
			 *  입력 종료 됐는데 스택에 뭐가 남아있으면 no
			 *
			 * */

            for (int j = 0; j < ps.length(); j++) {
                if (ps.charAt(j) == '(') {
                    pstack.add(ps.charAt(j));
                } else {
                    if (pstack.empty()) {
                    	answer = false;
                    	break;
                    }else{
                    	pstack.pop();
					}
                }
            }
            if(!pstack.empty()){
            	answer = false;
			}
            if(answer) System.out.println("YES");
            else System.out.println("NO");

        }
    }

}