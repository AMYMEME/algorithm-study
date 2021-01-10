import java.util.Scanner;
import java.util.Stack;

public class leesoeun98 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int count = scan.nextInt();
		scan.nextLine();

		for (int i = 0; i < count; i++) {
			// 스택 반복문 실마다 초기화되도록 여기에 선언 필요
			Stack<Character> stack = new Stack<Character>();
			String pstring = scan.nextLine();
			int isVPS = 0;
			int j = 0;
			/*
			 * 각 괄호마다 ( 면 push ) 인데 스택이 비워져있으면 no ) 인데 스택에 뭐가 있으면 pop => 모든 괄호에 대한 판단 이후에
			 * stack이 안비어져있으면 no 비어져있으면 yes
			 */
			while (j < pstring.length()) {
				if (pstring.charAt(j) == '(') {
					stack.push('(');
				} else if (pstring.charAt(j) == ')' && !stack.empty()) {
					stack.pop();
				} else if (pstring.charAt(j) == ')' && stack.empty()) {
					isVPS = 1;
					break;
				}
				j++;
			}
			if (!stack.empty()) {
				isVPS = 1;
			}
			if (isVPS == 0) {
				System.out.println("YES");
			} else {
				System.out.println("NO");
			}
		}

	}

}
