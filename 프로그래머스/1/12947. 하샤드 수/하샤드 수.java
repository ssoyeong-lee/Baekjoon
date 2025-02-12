import java.util.function.*;
import java.util.stream.*;

class Solution {
    public boolean solution(int y) {
        Predicate<Integer> isHashadNumber = x -> x % String.valueOf(x).chars().map(z -> z - '0').sum() == 0;
        return isHashadNumber.test(y);
    }
}