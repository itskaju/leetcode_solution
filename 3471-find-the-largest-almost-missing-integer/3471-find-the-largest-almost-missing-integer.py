class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        freq = defaultdict(int)

        for i in range(n-k+1):
            window = set(nums[i:i+k])
            for num in window:
                freq[num] += 1

        ans = -1
        for num in freq:
            if freq[num] == 1:
                ans = max(ans, num)
        return ans               







        