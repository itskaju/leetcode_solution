class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = Counter(nums)

        # cnt_g[g] = number of pairs whose gcd is exactly g
        cnt_g = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            total = 0

            for multiple in range(g, mx + 1, g):
                total += freq[multiple]
                cnt_g[g] -= cnt_g[multiple]

            cnt_g[g] += total * (total - 1) // 2

        prefix = list(accumulate(cnt_g))

        return [bisect_right(prefix, q) for q in queries]