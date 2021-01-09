package leesoeun98;

import java.util.*;

public class baekjoon14888 {
	static int n;
	static ArrayList<Integer> arr;
	static int[] nums;
	static int[] operations;
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		n=scan.nextInt();
		arr = new ArrayList<Integer>();
		
		nums = new int[n];
		
		operations = new int[4];
		
		for(int i=0; i<n; i++) {
			nums[i]=scan.nextInt();
		}
		for(int i=0; i<4; i++) {
			operations[i]=scan.nextInt();
		}
		//모든 경우의 수를 다 탐색하기 위헤 dfs
		// 계산결과인 result와 number의 idx가 인자 
		dfs(nums[0],1);
		
		System.out.println(Collections.max(arr));
		System.out.println(Collections.min(arr));
		
	}
	
	static void dfs(int result, int nidx) {
		//종료 조건 => number 다 썼으면 종료 (최종 계산결과를 arraylist에 저장)
		if(nidx==n) {
			arr.add(result);
			return;
		}
		for(int i=0; i<4; i++) {
			if(operations[i]>0) {
				operations[i]--;
				switch(i) {
				case 0:
					dfs(result+nums[nidx], nidx+1);
					break;
				case 1:
					dfs(result-nums[nidx], nidx+1);
					break;
				case 2:
					dfs(result*nums[nidx], nidx+1);
					break;
				case 3:
					dfs(result/nums[nidx], nidx+1);
					break;
				}
				operations[i]++;
			}
		}
	}

}
