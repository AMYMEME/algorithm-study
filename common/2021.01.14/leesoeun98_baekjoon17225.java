import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class leesoeun98_baekjoon17225 {
	static class Pair implements Comparable<Pair> {
		int startTime;
		String color;

		public Pair(int startTime, String color) {
			this.startTime = startTime;
			this.color = color;
		}

		/*
		 * �슦�꽑�닚�쐞 �걧瑜� �궗�슜�옄吏��젙 �옄猷뚰삎�쑝濡� 援ы쁽 �떆, compareTo瑜� �삤踰꾨씪�씠�뱶 �빐�빞 �븯�뒗�뜲 B媛� R蹂대떎 �슦�꽑�닚�쐞媛� �넂�룄濡� �옉�꽦�빐�빞 �븳�떎.
		 * this.color�� p.color瑜� 鍮꾧탳�빐�꽌 �옄湲곗옄�떊(B)-�긽��(R)�씠硫� -1�쓣, 諛섎�硫� 1�쓣, 媛숈쑝硫� 0�쓣 諛섑솚, -1�씪 �븣 �슦�꽑�닚�쐞媛�
		 * �넂�븘�꽌 �옄湲곗옄�떊�씠 �븵�뿉�삩�떎.
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
				// �븵�쓽 �꽑臾� �룷�옣 �걹�굹怨� �떎�쓬 �룷�옣 �떆�옉 怨좊젮
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

		// �젙�떟 異쒕젰
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
