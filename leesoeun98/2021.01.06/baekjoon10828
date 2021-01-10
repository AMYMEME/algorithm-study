import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

//제출 시 Main
public class baekjoon10828 {

	public static void main(String[] args) throws IOException {
		//scanner 사용 시 시간초과남
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int count = Integer.parseInt(br.readLine());
		StringTokenizer st;
		
		ArrayList<Integer> stack = new ArrayList<Integer>();
		
		for(int i=0;i<count;i++) {
			st = new StringTokenizer(br.readLine(), " ");
			switch(st.nextToken()) {
			case "push":
				 int num = Integer.parseInt(st.nextToken());
				 push(num, stack);
				break;
			case "top":
				System.out.println(top(stack));
				break;
			case "size":
				System.out.println(size(stack));
				break;
			case "empty":
				System.out.println(empty(stack));
				break;
			case "pop":
				System.out.println(pop(stack));		
				break;
				
			}
		}
		/*
		 * ArrayList 말고 내장된 Stack 사용하면 더 간단하다.
		 * 예로 Stack<Integer> stack = new Stack<Integer>();
		 * 위와 같이 사용하면 별도로 함수 안만들고 main 함수 분기처리 시 가능  
		 * 
		 * Stack<Integer> stack = new Stack<Integer>();
		 * 
		 * for(int i=0;i<count;i++) {
			st = new StringTokenizer(br.readLine(), " ");
			switch(st.nextToken()) {
			case "push":
			 	int num = Integer.parseInt(st.nextToken());
				stack.push(num);
				break;
			case "top":
				if(stack.size()<1){
				System.out.println(-1);
				}
				else{
					System.out.println(stack.peek());
				}
				break;
			case "size":
				System.out.println(stack.size());
				break;
			case "empty":
				if(stack.size()<1){
				System.out.println(1);
				}
				else{
					System.out.println(0);
				}
				break;
			case "pop":
				if(stack.size()<1){
				System.out.println(-1);
				}
				else{
					int top = stack.pop();
					System.out.println(top);
				}break;
				
			}
		}
		 * */
	}
	
	static void push(int x, ArrayList stack) {
		stack.add(x);
	}
	
	static int pop(ArrayList stack) {
		if(empty(stack)==1) {
			return -1;	
		}
		else {
			int popnum= (int) stack.get(size(stack)-1);
			stack.remove(size(stack)-1);
			return popnum;
		}
	}
	
	static int size(ArrayList stack) {
		return stack.size();
	}
	
	static int empty(ArrayList stack) {
		if(size(stack)==0) {
			return 1;
		}
		else {
			return 0;
		}
	}
	
	static int top(ArrayList stack) {
		if(empty(stack)==1) {
			return -1;	
		}
		else {
			return (int) stack.get(stack.size()-1);
		}
	}

}