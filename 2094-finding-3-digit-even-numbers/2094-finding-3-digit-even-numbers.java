import java.util.*;

class Solution {
    public int[] findEvenNumbers(int[] digits) {
        int[] cnt = new int[10];
        for (int d : digits) cnt[d]++;
        List<Integer> ans = new ArrayList<>();
        
        for (int x = 100; x < 1000; x += 2) {
            int[] cnt1 = new int[10];
            int y = x;
            while (y > 0) {
                cnt1[y % 10]++;
                y /= 10;
            }
            boolean ok = true;
            for (int i = 0; i < 10; i++) {
                if (cnt1[i] > cnt[i]) {
                    ok = false;
                    break;
                }
            }
            if (ok) ans.add(x);
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
}
