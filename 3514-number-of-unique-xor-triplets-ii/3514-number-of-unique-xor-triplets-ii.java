class Solution {
    public int uniqueXorTriplets(int[] nums) {
        // Find maximum element in nums
        int m = 0;
        for (int num : nums) {
            m = Math.max(m, num);
        }

        // Find next power of 2 greater than max element
        int u = 1;
        while (u <= m) {
            u <<= 1;
        }

        // Boolean arrays to track XOR combinations
        boolean[] one = new boolean[u];
        boolean[] two = new boolean[u];
        boolean[] three = new boolean[u];

        // Build all possible XOR pairs
        for (int v : nums) {
            one[v] = true;
            for (int x = 0; x < u; x++) {
                if (one[x]) {
                    two[x ^ v] = true;
                }
            }
        }

        // Build all possible XOR triplets
        for (int v : nums) {
            for (int x = 0; x < u; x++) {
                if (two[x]) {
                    three[x ^ v] = true;
                }
            }
        }

        // Count unique XOR triplet results
        int ans = 0;
        for (boolean b : three) {
            if (b) ans++;
        }

        return ans;
    }

    // Example usage
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1, 2, 3};
        System.out.println(sol.uniqueXorTriplets(nums)); // Output: number of unique XOR triplets
    }
}
