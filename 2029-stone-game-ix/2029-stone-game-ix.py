class Solution:
    def stoneGameIX(self, stones):
        cnt = [0, 0, 0]

        # Count stones by remainder
        for x in stones:
            cnt[x % 3] += 1

        # Case 1: number of 0-remainder stones is even
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # Case 2: number of 0-remainder stones is odd
        return abs(cnt[1] - cnt[2]) > 2