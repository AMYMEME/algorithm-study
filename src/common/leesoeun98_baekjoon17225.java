package common;

import java.util.ArrayList;
import java.util.Scanner;

public class leesoeun98_baekjoon17225 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		int n = scan.nextInt();
		int jgift = 0;
		int sgift = 0;
		int scount = 0;
		int jcount = 0;
		int gift = 1;
		int maxs = -1;
		int maxj = -1;

		ArrayList<Integer> sangmin = new ArrayList<Integer>();
		ArrayList<Integer> jisoo = new ArrayList<Integer>();
		ArrayList<Integer> sangmingift = new ArrayList<Integer>();
		ArrayList<Integer> jisoogift = new ArrayList<Integer>();

		for (int i = 0; i < n; i++) {
			int time = scan.nextInt();
			String color = scan.next();
			int m = scan.nextInt();
			int cnt = 0;
			if (color.equals("B")) {
				// 앞의 선물 포장 끝나고 다음 포장 시작 고려
				if (maxs > time)
					time = maxs;
				for (int j = time; cnt < m; j += a) {
					sangmin.add(j);
					cnt += 1;
					sgift += 1;
				}
				maxs = time + m * a;
			} else {
				if (maxj > time)
					time = maxj;
				for (int j = time; cnt < m; j += b) {
					jisoo.add(j);
					cnt += 1;
					jgift += 1;
				}
				maxj = time + m * b;
			}

		}

		// 시간 순대로 선물 순서 정하는 부분
		while (jgift - 1 >= jcount && sgift - 1 >= scount) {

			if (sangmin.get(scount) == jisoo.get(jcount)) {
				sangmingift.add(gift);
				gift++;
				scount++;
				jisoogift.add(gift);
				gift++;
				jcount++;
			} else if (sangmin.get(scount) > jisoo.get(jcount)) {
				jisoogift.add(gift);
				gift++;
				jcount++;
			} else {
				// 나중이므로 상민이 선물이 먼저
				sangmingift.add(gift);
				gift++;
				scount++;
			}
		}
		// 마지막 값 출력
		while (jcount < jgift) {
			jisoogift.add(gift);
			jcount++;
			gift++;
		}
		while (scount < sgift) {
			sangmingift.add(gift);
			scount++;
			gift++;
		}

		// 정답 출력
		System.out.println(scount);
		for (int i : sangmingift) {
			System.out.print(i + " ");
		}
		System.out.println();
		System.out.println(jcount);
		for (int i : jisoogift) {
			System.out.print(i + " ");
		}

	}

}
