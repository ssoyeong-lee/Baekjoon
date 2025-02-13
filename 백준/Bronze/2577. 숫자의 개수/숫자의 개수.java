import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int total = 1;
        for (int i = 0; i < 3; i ++) {
            total *= Integer.parseInt(br.readLine());
        }

        int[] ret = new int[10];
        while (total > 0) {
            ret[total % 10] += 1;
            total /= 10;
        }
        for(int r: ret) {
            bw.write(r + '0');
            bw.newLine();
        }
        bw.flush();
        br.close(); bw.close();
    }
}