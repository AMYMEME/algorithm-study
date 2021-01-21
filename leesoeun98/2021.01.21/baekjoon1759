import java.util.Arrays;
import java.util.Scanner;

public class baekjoon1759 {
    static int l;
    static int c;
    static String[] alphabet;

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        l = scan.nextInt();
        c = scan.nextInt();
        alphabet = new String[c];
        for (int i = 0; i < c; i++) {
            alphabet[i] = scan.next();
        }
        //오름차순 정렬
        Arrays.sort(alphabet);
        password(0, "");
    }

    static void password(int idx, String result) {
        // l과 문자열 길이 동일 + 조건 만족 시 출력
        if (result.length() == l) {
            if (isPossible(result)) {
                System.out.println(result);
            }
            return;
        }
        if (idx >= c) {
            return;
        }
        // 그게 아니면(문자열 길이 짧으면), for 문 c번 돌려서 백트래킹
        password(idx + 1, result + alphabet[idx]); //해당문자 포함
        password(idx + 1, result); //해당문자 안 포함
    }

    static boolean isPossible(String result) {
        int vowel = 0;
        int consonant = 0;
        //모음 1개, 자음 2개 이상으로 구성되어있으면 true 이니면 false
        for (int i = 0; i < result.length(); i++) {
            if (isVowel(result.charAt(i))) {
                vowel++;
            } else {
                consonant++;
            }
        }
        if (vowel >= 1 && consonant >= 2) {
            return true;
        } else {
            return false;
        }
    }

    static boolean isVowel(char alp) {
        if (alp == 'a' || alp == 'e' || alp == 'i' || alp == 'o' || alp == 'u') {
            return true;
        } else {
            return false;
        }
    }
}
