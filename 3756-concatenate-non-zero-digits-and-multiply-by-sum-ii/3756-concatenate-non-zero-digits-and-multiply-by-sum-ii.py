from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # Prefix arrays
        val = [0] * (n + 1)       # concatenated non-zero digits modulo MOD
        cnt = [0] * (n + 1)       # count of non-zero digits
        sumPre = [0] * (n + 1)    # sum of digits

        # Precompute
        for i in range(n):
            d = int(s[i])
            val[i+1] = val[i]
            cnt[i+1] = cnt[i]
            sumPre[i+1] = sumPre[i] + d
            if d != 0:
                val[i+1] = (val[i] * 10 + d) % MOD
                cnt[i+1] += 1

        results = []
        for l, r in queries:
            k = cnt[r+1] - cnt[l]  # number of non-zero digits in substring
            if k == 0:
                results.append(0)
                continue
            # compute x = substring number
            x = (val[r+1] - val[l] * pow(10, k, MOD)) % MOD
            digit_sum = sumPre[r+1] - sumPre[l]
            results.append((x * digit_sum) % MOD)

        return results
