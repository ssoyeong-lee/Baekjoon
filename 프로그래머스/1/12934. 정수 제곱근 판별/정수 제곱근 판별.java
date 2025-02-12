class Solution {
    public long solution(long n) {
        long i = 1;
        while (true) {
            long tmp = i * i;
            if (tmp > n)
                break;
            else if (tmp == n) {
                return (i + 1) * (i + 1);
            }
            i ++;
        }
        return -1;
    }
}