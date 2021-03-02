package BOJ;

import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class baekjoon11000 {
    static class Lecture {
        int startTime;
        int endTime;

        public Lecture(int startTime, int endTime) {
            this.startTime = startTime;
            this.endTime = endTime;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Lecture lectures[] = new Lecture[n];
        for (int i = 0; i < n; i++) {
            int startTime = sc.nextInt();
            int endTime = sc.nextInt();
            lectures[i] = new Lecture(startTime, endTime);
        }
        /*
         * 강의 시작시간 종료시간
         * 시작시간 순으로 정렬 시작시간이 같으면 종료시간이 더 늦은걸 나중으로 => 정렬
         * 가장 앞에 있는 강의를 큐에 넣음
         * 큐에 있는 종료시간 vs 그 다음 (큐에 안들어간) 시작시간 => 시작시간이 종료보다 늦으면 큐에 있는거 pop 하고 다음거를 큐에 새로 넣음
         * => 만약 시작시간이 더 빠르면 새로 큐에 넣음 (강의실을 새로 배정한 것)
         * 큐의 크기가 강의실의 개수
         * */
        Arrays.sort(lectures, (l1, l2) -> l1.startTime == l2.startTime ? l1.endTime - l2.endTime : l1.startTime - l2.startTime);

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(lectures[0].endTime);

        for (int i = 1; i < n; i++) {
            if(pq.peek()>lectures[i].startTime){ //여기선 peek (큐에서 삭제 안되게)
                pq.add(lectures[i].endTime);
            }
            else{
                pq.poll();
                pq.add(lectures[i].endTime);
            }
        }
        System.out.println(pq.size());
    }
}
