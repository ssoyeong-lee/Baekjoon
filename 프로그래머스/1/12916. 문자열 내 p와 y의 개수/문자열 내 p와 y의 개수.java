class Solution {
    boolean solution(String s) {
        int cntP = 0;
        int cntY = 0;
        
        for (char c : s.toCharArray()) {
            switch (c) {
                case 'P':
                case 'p':
                    cntP += 1;
                    break;
                case 'Y':
                case 'y':
                    cntY += 1;
                    break;
            }
        }
        
        return cntP == cntY;
    }
}