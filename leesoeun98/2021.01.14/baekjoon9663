import java.util.Scanner;

public class baekjoon9663 {
	static int n;
	static int[] board;
	static int count = 0;

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		n = scan.nextInt();
		board = new int[n];

		nQueen(0);
		System.out.println(count);
	}

	// column 당 퀸 1개, row 당 퀸 1개 board n번째 col까지 퀸을 다 뒀으면 재귀 종료, 경우의 수 1 증가
	public static void nQueen(int col) {
		if (col == n) {
			count++;
			return;
		}
		// board[col]에서 0부터 n-1까지 모든 행에 퀸을 뒀을 때 isPossible하면 다음 col로 이동
		for (int i = 0; i < n; i++) {
			// 각 열에 대해 모든 행(0~n-1)에 퀸 둬보기
			board[col] = i;
			// 각 열에서 해당 행이 가능하면, 다음 열로 이동
			if (isPossible(col)) {
				nQueen(col + 1);
			}

		}

	}

	// row에서 겹치는 퀸이 있는지, 대각선에서 겹치는 퀸이 있는지 판별
	public static boolean isPossible(int col) {
		for (int j = 0; j < col; j++) {
			// board[col]=i 이므로, board[0~col-1]까지 i가 있으면 안된다.
			// row 겹치면 false
			if (board[col] == board[j]) {
				return false;
			}
			// 대각선 (열의 차, 행의 차 같으면)에 겹치면 false
			else if (Math.abs(col - j) == Math.abs(board[col] - board[j])) {
				return false;
			}
		}

		return true;
	}
}
