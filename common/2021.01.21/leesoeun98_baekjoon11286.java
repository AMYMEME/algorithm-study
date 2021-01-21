import java.util.PriorityQueue;
import java.util.Scanner;

public class baekjoon11286 {
    static class Number implements Comparable<Number> {
        int num;

        public Number(int num) {
            this.num = num;
        }

        @Override
        public int compareTo(Number N) {
            /*
             * Math.abs(this.num) > Math.abs(num) : 1 return
             * Math.abs(this.num) < Math.abs(num) : -1 return
             * Math.abs(this.num) == Math.abs(num) 이면 this.num < num
             * */
            if (Math.abs(this.num) > Math.abs(N.num)) {
                return 1;
            } else if (Math.abs(this.num) < Math.abs(N.num)) {
                return -1;
            } else if (Math.abs(this.num) == Math.abs(N.num)) {
                if(this.num < N.num){
                    return -1;
                }
                else if(this.num==N.num){
                    return 0;
                }
                else{
                    return 1;
                }
            }
            return Integer.compare(this.num, N.num);
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] numbers = new int[n];
        PriorityQueue<Number> pq = new PriorityQueue<Number>();

        for (int i = 0; i < n; i++) {
            int num=scan.nextInt();
            if(num==0){
                if(pq.isEmpty()){
                    System.out.println(0);
                }else{
                    System.out.println(pq.poll().num);
                }
            }else{
                numbers[i] = num;
                pq.add(new Number(num));
            }
        }

    }
}
