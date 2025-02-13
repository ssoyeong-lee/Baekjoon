import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int[] numbers = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++){
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int x = Integer.parseInt(br.readLine());

        Arrays.sort(numbers);
        int start = 0;
        int end = numbers.length - 1;

        long cnt = 0;
        while (start < end) {
            int sum = numbers[start] + numbers[end];
            if (sum == x) {
                cnt += 1;
                start += 1;
                end -= 1;
            } else if (sum > x) {
                end -= 1;
            } else {
                start += 1;
            }
        }
        bw.write(String.valueOf(cnt));
        bw.newLine();

        bw.flush();
        br.close(); bw.close();
    }
}