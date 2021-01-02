package leesoeun98;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class baekjoon10828_20210106 {

	public static void main(String[] args) throws NumberFormatException, IOException {
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
