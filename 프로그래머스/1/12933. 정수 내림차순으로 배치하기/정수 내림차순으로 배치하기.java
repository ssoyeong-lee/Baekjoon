import java.util.*;
import java.util.stream.*;

class Solution {
    public long solution(long n) {
        List<Long> list = new ArrayList<>();
        while (n > 0) {
            list.add(n % 10);
            n /= 10;
        }
        List<Long> tmp = list.stream().sorted(Collections.reverseOrder())
            .collect(Collectors.toList());

        long ret = 0;
        for (long l : tmp) {
            ret *= 10;
            ret += l;
        }
        return ret;
    }
}