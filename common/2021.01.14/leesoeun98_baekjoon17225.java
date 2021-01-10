import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class baekjoon17225 {
	static class Pair implements Comparable<Pair> {
		int startTime;
		String color;

		public Pair(int startTime, String color) {
			this.startTime = startTime;
			this.color = color;
		}

		/*
		 * 우선순위 큐를 사용자지정 자료형으로 구현 시, compareTo를 오버라이드 해야 하는데 B가 R보다 우선순위가 높도록 작성해야 한다.
		 * this.color와 p.color를 비교해서 자기자신(B)-상대(R)이면 -1을, 반대면 1을, 같으면 0을 반환, -1일 때 우선순위가
		 * 높아서 자기자신이 앞에온다.
		 */
		@Override
		public int compareTo(Pair p) {
			if (this.startTime == p.startTime) {
				if (this.color.equals("B") && p.color.equals("R")) {
					return -1;
				} else if (this.color.equals("R") && p.color.equals("B")) {
					return 1;
				} else {
					return 0;
				}
			}
			return Integer.compare(this.startTime, p.startTime);
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		//
		int[] first = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

		int a = first[0];
		int b = first[1];
		int n = first[2];

		int gift = 1;

		int maxs = -1;
		int maxj = -1;

		PriorityQueue<Pair> pq = new PriorityQueue<>(Pair::compareTo);
		ArrayList<Integer> sangmingift = new ArrayList<Integer>();
		ArrayList<Integer> jisoogift = new ArrayList<Integer>();

		for (int i = 0; i < n; i++) {
			String[] line = br.readLine().split(" ");
			int time = Integer.parseInt(line[0]);
			int m = Integer.parseInt(line[2]);
			int cnt = 0;
			if (line[1].equals("B")) {
				// 앞의 선물 포장 끝나고 다음 포장 시작 고려
				if (maxs > time)
					time = maxs;
				for (int j = time; cnt < m; j += a) {
					pq.add(new Pair(j, "B"));
					cnt += 1;
				}
				maxs = time + m * a;
			} else {
				if (maxj > time)
					time = maxj;
				for (int j = time; cnt < m; j += b) {
					pq.add(new Pair(j, "R"));
					cnt += 1;
				}
				maxj = time + m * b;
			}

		}

		while (!pq.isEmpty()) {
			Pair pair = pq.poll();
			if (pair.color.equals("B")) {
				sangmingift.add(gift++);
			} else {
				jisoogift.add(gift++);
			}
		}

		// 정답 출력
		bw.write(sangmingift.size() + "\n");
		for (int i : sangmingift) {
			bw.write(i + " ");
		}
		bw.write("\n");
		bw.write(jisoogift.size() + "\n");
		for (int i : jisoogift) {
			bw.write(i + " ");
		}
		bw.flush();
		bw.close();
	}

}
