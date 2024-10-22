import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        if (a > b){
            long tmp = a;
            a = b;
            b = tmp;
        }

        long size = 0;
        if (a != b)
            size = b - a - 1;
        bw.write(size + "\n");

        for (long i = a + 1; i < b; i ++){
            bw.write(i + " ");
        }
        bw.write("\n");

        br.close();
        bw.flush();
        bw.close();
    }
}
