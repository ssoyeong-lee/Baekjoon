import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String word = br.readLine();
        int[] ret = new int[26];

        for (char c: word.toCharArray()) {
            ret[c - 'a'] += 1;
        }
        for (int r: ret) {
            bw.write(r + " ");
        }
        bw.flush();
        br.close(); bw.close();
    }
}