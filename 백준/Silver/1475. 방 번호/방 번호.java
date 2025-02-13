import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] ret = new int[10];
        String num = br.readLine();
        for (char n: num.toCharArray()) {
            int idx = n != '9' ? n - '0' : 6;
            ret[idx] += 1;
        }
        ret[6] = (int)Math.round((double)ret[6] / 2);

        int maxCnt = 0;
        for (int r : ret) {
            maxCnt = Math.max(maxCnt, r);
        }
        bw.write(maxCnt + '0');
        bw.flush();
        br.close(); bw.close();
    }
}